"""Google Flow Automation MCP Server.
Exposes Model Context Protocol (MCP) tools for Google Flow video generation,
queue management, and local media retrieval in Antigravity and VS Code.
"""

import sys
import json
from pathlib import Path
try:
    from mcp.server.mcpserver import MCPServer as FastMCP
except ImportError:
    from mcp.server.fastmcp import FastMCP

from config import OUTPUT_DIR, LOGS_DIR
from prompt_manager import PromptManager

# Initialize FastMCP Server
mcp = FastMCP("google-flow-automation")
pm = PromptManager()


@mcp.tool()
def add_video_prompt(prompt: str) -> str:
    """Add a new video generation prompt to the Google Flow queue.

    Args:
        prompt: Detailed description of the video to generate.
    """
    clean = prompt.strip()
    if not clean:
        return "Error: Prompt cannot be empty."
    item = pm.add_prompt(clean)
    return f"Successfully queued prompt [{item['id']}]: '{item['prompt'][:60]}...'"


@mcp.tool()
def get_queue_status() -> str:
    """Get the current Google Flow prompt queue status and item counts."""
    summary = pm.get_summary()
    lines = [
        f"Total: {summary['Total']} | Pending: {summary['Pending']} | Processing: {summary['Processing']} | Completed: {summary['Completed']} | Failed: {summary['Failed']}",
        "-" * 60,
    ]
    for i, it in enumerate(pm.items, 1):
        status = it.get("status", "Pending")
        err = f" (Error: {it['error']})" if it.get("error") else ""
        out = f" -> {it['output_file']}" if it.get("output_file") else ""
        lines.append(f"{i}. [{status}] [{it['id']}] {it['prompt'][:70]}...{out}{err}")
    return "\n".join(lines)


@mcp.tool()
def list_brand_characters(category: str = "", state: str = "") -> str:
    """List characters available in B.S Organic brand universe.

    Args:
        category: Optional filter: 'Hero', 'Vegetable', 'Fruit', 'Flower', 'Cash Crop'.
        state: Optional state filter: e.g. 'Maharashtra', 'Punjab', 'Gujarat', 'Himachal', 'UP'.
    """
    from character_manager import CharacterManager
    cm = CharacterManager()
    chars = cm.list_characters(category=category, state=state)
    if not chars:
        filter_str = f"category='{category}', state='{state}'"
        return f"No characters found for filters: {filter_str}"
    lines = [f"B.S Organic Characters ({len(chars)} found):"]
    for c in chars:
        lines.append(f"- [{c['category']}] [{c.get('state', 'Pan-India')}] {c['name']} (ID: {c['id']}): {c['tagline']}")
    return "\n".join(lines)


@mcp.tool()
def queue_character_image(character_id: str) -> str:
    """Queue a high-definition 9:16 portrait prompt for a B.S Organic character to Google Flow.

    Args:
        character_id: ID of the character (e.g. 'captain_wiggly', 'tommy_tomato', 'rozy_rose').
    """
    from character_manager import CharacterManager
    cm = CharacterManager()
    c = cm.get_character(character_id)
    if not c:
        return f"Error: Character ID '{character_id}' not found."
    results = cm.queue_character_images([character_id], pm=pm)
    return f"Successfully queued 9:16 reference image prompt for {c['name']} into Google Flow.\nQueue items: {results}"


@mcp.tool()
def queue_all_character_images() -> str:
    """Queue 9:16 portrait image prompts for all 14 B.S Organic characters into Google Flow."""
    from character_manager import CharacterManager
    cm = CharacterManager()
    results = cm.queue_character_images(pm=pm)
    return f"Queued {len(results)} character prompts into Google Flow:\n" + "\n".join(results)


@mcp.tool()
def get_character_story_context(character_id: str) -> str:
    """Retrieve full story and visual anchor context for Gemini to write a 40s Shorts narrative.

    Args:
        character_id: ID of the character (e.g. 'tommy_tomato', 'rozy_rose', 'himachali_seb').
    """
    from character_manager import CharacterManager
    cm = CharacterManager()
    try:
        ctx = cm.get_character_story_context(character_id)
        return json.dumps(ctx, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def queue_character_story(character_id: str) -> str:
    """Queue all 5 sequential 8-second video beat prompts for a character into Google Flow (40s Master Short).

    Args:
        character_id: ID of the character (e.g. 'tommy_tomato', 'rozy_rose', 'captain_wiggly').
    """
    from character_manager import CharacterManager
    cm = CharacterManager()
    try:
        res = cm.queue_character_story(character_id, pm=pm)
        lines = [
            f"Successfully queued 5-beat story for {res['character_name']} ({res['category']}, {res['state']}):",
            f"- Story ID: {res['story_id']}",
            f"- Target Master Video: {res['target_master_video']}",
            f"- Queued Prompt IDs: {', '.join(res['queued_prompt_ids'])}",
        ]
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def check_story_status(story_id: str) -> str:
    """Check the generation progress of all 5 clips for a specific story.

    Args:
        story_id: The ID of the story (e.g. 'story_tommy_tomato_1729000000').
    """
    from character_manager import CharacterManager
    cm = CharacterManager()
    status = cm.check_story_completion(story_id, pm=pm)
    if not status.get("found"):
        return f"No clips found for story ID '{story_id}'."
    return (
        f"Story [{story_id}]: {status['completed']}/{status['total_clips']} clips completed | "
        f"Pending: {status['pending']} | Failed: {status['failed']} | "
        f"Ready to stitch: {status['ready_to_stitch']}"
    )


@mcp.tool()
def generate_gemini_story(character_id: str, theme_hint: str = "") -> str:
    """Use Gemini Free API to synthesize a 5-beat organic transformation story for a character.

    Args:
        character_id: ID of the character (e.g. 'himachali_seb', 'nagpur_santra', 'tommy_tomato').
        theme_hint: Optional thematic setting (e.g. 'Monsoon terrace garden', 'Punjab winter harvest').
    """
    from gemini_story_engine import GeminiStoryEngine
    engine = GeminiStoryEngine()
    try:
        story = engine.generate_story(character_id, theme_hint=theme_hint)
        return json.dumps(story, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def generate_and_queue_gemini_story(character_id: str, theme_hint: str = "") -> str:
    """Use Gemini API to generate a story and immediately queue all 5 beats into Google Flow.

    Args:
        character_id: ID of the character (e.g. 'himachali_seb', 'nagpur_santra', 'tommy_tomato').
        theme_hint: Optional theme (e.g. 'Apple orchard revival', 'Terrace rose bloom').
    """
    from gemini_story_engine import GeminiStoryEngine
    engine = GeminiStoryEngine()
    try:
        res = engine.generate_and_queue(character_id, theme_hint=theme_hint, pm=pm)
        lines = [
            f"Successfully generated & queued story via {res['generated_by']}:",
            f"Title: {res['story_title']}",
            f"Character: {res['character_name']} (ID: {res['character_id']})",
            f"Story ID: {res['story_id']}",
            f"Master Video Target: {res['target_master_video']}",
            f"Queued Prompts: {', '.join(res['queued_prompt_ids'])}",
            f"\nSocial Caption:\n{res['caption']}",
        ]
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def list_generated_videos() -> str:
    """List all completed video files downloaded from Google Flow in output_videos/."""
    files = list(OUTPUT_DIR.glob("*.mp4")) + list(OUTPUT_DIR.glob("*.webm"))
    if not files:
        return f"No completed videos found in {OUTPUT_DIR}."

    result = [f"Found {len(files)} completed videos in {OUTPUT_DIR}:"]
    for f in sorted(files, key=lambda x: x.stat().st_mtime, reverse=True):
        size_mb = f.stat().st_size / (1024 * 1024)
        result.append(f"- {f.name} ({size_mb:.2f} MB)")
    return "\n".join(result)


@mcp.tool()
def retry_failed_prompts() -> str:
    """Reset all Failed or interrupted prompts back to Pending status for retry."""
    count = pm.retry_failed()
    return f"Reset {count} failed/processing prompts to Pending."


@mcp.tool()
def trigger_video_generation(limit: int = 1) -> str:
    """Run Google Flow automation for up to `limit` pending prompts.

    Args:
        limit: Maximum number of prompts to generate in this run (default 1).
    """
    from browser_manager import BrowserManager
    from flow_automation import GoogleFlowAutomation
    from downloader import VideoDownloader

    bm = BrowserManager(headless=False)
    dl = VideoDownloader()
    automation = GoogleFlowAutomation(browser_manager=bm, prompt_manager=pm, downloader=dl)
    try:
        summary = automation.run_queue(max_items=limit)
        return f"Automation run completed. Results: {summary}"
    except Exception as e:
        return f"Automation error: {str(e)}"
    finally:
        bm.close()


if __name__ == "__main__":
    mcp.run()

