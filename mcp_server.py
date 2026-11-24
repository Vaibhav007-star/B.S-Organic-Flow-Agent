"""Google Flow Automation MCP Server.
Exposes Model Context Protocol (MCP) tools for Google Flow video generation,
queue management, and local media retrieval in Antigravity and VS Code.
"""

import sys
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
def list_brand_characters(category: str = "") -> str:
    """List characters available in B.S Organic brand universe.

    Args:
        category: Optional filter: 'Hero', 'Vegetable', 'Fruit', 'Flower', 'Cash Crop'.
    """
    from character_manager import CharacterManager
    cm = CharacterManager()
    chars = cm.list_characters(category=category)
    if not chars:
        return f"No characters found for category: '{category}'"
    lines = [f"B.S Organic Characters ({len(chars)} found):"]
    for c in chars:
        lines.append(f"- [{c['category']}] {c['name']} (ID: {c['id']}): {c['tagline']}")
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

