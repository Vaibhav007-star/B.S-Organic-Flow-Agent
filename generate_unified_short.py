"""Unified Short Generator for B.S Organic Flow Agent.
Integrates:
1. Character Database (33 regional crops/fruits/vegetables/flowers in characters.json).
2. Gemini Story Engine (5-beat 40s narrative + Hindi voice-over script).
3. Authentic Product Bag Reference (assets/bs_organic_bag_reference.jpg).
4. Google Flow Automation Queue (prompts_state.json).
5. Master 40s Short Builder & FFmpeg Stitcher (build_story_short.py).
"""

import sys
import os
import json
import argparse
from pathlib import Path
from typing import Dict, Any, Optional

from config import BASE_DIR, OUTPUT_DIR
from character_manager import CharacterManager
from gemini_story_engine import GeminiStoryEngine
from prompt_manager import PromptManager
from build_story_short import build_story_master, render_sample_preview_short

ASSET_BAG_REF = BASE_DIR / "assets" / "bs_organic_bag_reference.jpg"


def execute_flow_generation(story_id: str, max_clips: int = 5, headless: bool = False) -> Dict[str, Any]:
    """Drives Google Flow automation to generate clips for a story, and then stitches them into a 40s Master Short."""
    from browser_manager import BrowserManager
    from downloader import VideoDownloader
    from flow_automation import GoogleFlowAutomation
    from prompt_manager import PromptManager
    from character_manager import CharacterManager

    pm = PromptManager()
    bm = BrowserManager(headless=headless)
    dl = VideoDownloader()
    automation = GoogleFlowAutomation(browser_manager=bm, prompt_manager=pm, downloader=dl)

    print("\n" + "=" * 65)
    print(f"🚀 LAUNCHING GOOGLE FLOW GENERATION FOR STORY: [{story_id}]")
    print(f"Browser mode: {'Headless' if headless else 'Visible'}")
    print("=" * 65)

    try:
        summary = automation.run_queue(max_items=max_clips, story_id=story_id)
        print(f"Generation run completed. Summary: {summary}")
    finally:
        bm.close()

    # Check if clips are ready to stitch
    cm = CharacterManager()
    status = cm.check_story_completion(story_id, pm=pm)
    print(f"\nStory Status for [{story_id}]: {status['completed']}/{status['total_clips']} clips ready.")

    if status["ready_to_stitch"]:
        print(f"🎉 All {status['completed']} clips downloaded! Stitching 40-Second Master Short...")
        out_master = build_story_master(story_id, sample_if_missing=False)
        print(f"Master Short Created: {out_master.name}")
        return {"story_id": story_id, "status": "completed", "master_video": str(out_master)}
    else:
        print(f"Waiting for remaining clips ({status['pending']} pending, {status['failed']} failed).")
        return {"story_id": story_id, "status": "in_progress", "clips_ready": status["completed"]}


def run_character_story_pipeline(character_id: str, theme_hint: Optional[str] = None, render_sample: bool = False, generate_flow: bool = False) -> Dict[str, Any]:
    """Generates a complete 5-beat story using Gemini, queues prompts for Google Flow,

    and optionally renders the 40-second master preview short.
    """
    cm = CharacterManager()
    c = cm.get_character(character_id)
    if not c:
        raise ValueError(f"Character '{character_id}' not found in database. Use --list-characters to inspect options.")

    print("\n" + "=" * 65)
    print(f"🌿 B.S ORGANIC UNIFIED SHORT PIPELINE: [{c['name'].upper()}]")
    print(f"Region: {c.get('state', 'Pan-India')} | Category: {c['category']}")
    print(f"Reference Bag: {ASSET_BAG_REF.name} ({'EXISTS ✓' if ASSET_BAG_REF.exists() else 'MISSING ✗'})")
    print("=" * 65)

    engine = GeminiStoryEngine()
    print("\nStep 1: Calling Gemini API for 5-Beat Story & Hindi Voice-Over...")
    res = engine.generate_and_queue(character_id, theme_hint=theme_hint)

    print(f"🎉 Story Generated via {res['generated_by']}!")
    print(f"Title: {res['story_title']}")
    print(f"Story ID: {res['story_id']}")
    print(f"Target Video: {res['target_master_video']}")
    print(f"Queued Prompt IDs: {', '.join(res['queued_prompt_ids'])}")
    print(f"\nSocial Caption:\n{res['caption']}\n")

    if generate_flow:
        print("\nStep 2: Starting Google Flow Automation to Generate 5 Video Clips...")
        execute_flow_generation(res["story_id"], max_clips=5, headless=False)
    elif render_sample:
        print("\nStep 2: Rendering 40.0s Master Short Preview via FFmpeg...")
        out_video = OUTPUT_DIR / res["target_master_video"]
        render_sample_preview_short(out_video, character_name=c["name"])
        print(f"Master Short Ready: {out_video.name}")
        res["master_video_path"] = str(out_video)

    print("=" * 65)
    print("Next Steps:")
    print(f"1. Generate clips on Google Flow: python generate_unified_short.py --character {c['id']} --generate-flow")
    print(f"2. Check status: python -c \"from character_manager import CharacterManager; print(CharacterManager().check_story_completion('{res['story_id']}'))\"")
    print(f"3. Stitch final short: python build_story_short.py --story-id {res['story_id']}")
    print("=" * 65 + "\n")
    return res


def run_commercial_pipeline(render_sample: bool = False, generate_flow: bool = False) -> Dict[str, Any]:
    """Queues the official 40-second photoreal B.S Organic bag commercial (No characters/people)."""
    from prompt_manager import PromptManager
    pm = PromptManager()
    story_id = "bs_organic_master_commercial_40s"

    print("\n" + "=" * 65)
    print("🌿 B.S ORGANIC PHOTOREAL MASTER COMMERCIAL (40s)")
    print(f"Product Reference Bag: {ASSET_BAG_REF.name} ({'EXISTS ✓' if ASSET_BAG_REF.exists() else 'MISSING ✗'})")
    print("Style: 4K Photoreal Nature & Product Commercial (No characters, No people)")
    print("Offer: ₹150 / 25 kg")
    print("=" * 65)

    story_items = [it for it in pm.items if it.get("story_id") == story_id]
    print(f"Found {len(story_items)} beats already queued for {story_id}.")

    out_video = OUTPUT_DIR / f"{story_id}_master_40s.mp4"
    if generate_flow:
        print("\nStarting Google Flow Video Generation for Commercial...")
        execute_flow_generation(story_id, max_clips=5, headless=False)
    elif render_sample:
        print("\nRendering 40.0s Master Commercial Video...")
        render_sample_preview_short(out_video, character_name="B.S. Organic Official Bag")
        print(f"Master Commercial Ready: {out_video.name}")

    return {"story_id": story_id, "master_video": str(out_video), "beats_count": len(story_items)}


def main():
    parser = argparse.ArgumentParser(description="Unified B.S Organic Video Generation Pipeline")
    parser.add_argument("--character", type=str, default=None, help="Character ID (e.g. 'tommy_tomato', 'rozy_rose', 'himachali_seb')")
    parser.add_argument("--commercial", action="store_true", help="Generate the official photoreal B.S Organic bag commercial")
    parser.add_argument("--theme", type=str, default=None, help="Thematic setting hint for Gemini story")
    parser.add_argument("--render-sample", action="store_true", help="Render a 40.0s sample video via FFmpeg immediately")
    parser.add_argument("--generate-flow", action="store_true", help="Launch Google Flow browser automation to generate and download real Veo video clips")
    parser.add_argument("--list-characters", action="store_true", help="List all 33 regional characters")
    parser.add_argument("--state", type=str, default=None, help="Filter characters by state")
    args = parser.parse_args()

    cm = CharacterManager()
    if args.list_characters:
        chars = cm.list_characters(state=args.state)
        print("=" * 65)
        print(f"  B.S ORGANIC CHARACTERS ({len(chars)} found)")
        print("=" * 65)
        for c in chars:
            print(f"[{c['category']:<12}] [{c.get('state', 'Pan-India'):<25}] {c['name']} (ID: {c['id']})")
        print("=" * 65)
        return

    if args.commercial:
        run_commercial_pipeline(render_sample=args.render_sample, generate_flow=args.generate_flow)
    elif args.character:
        run_character_story_pipeline(args.character, theme_hint=args.theme, render_sample=args.render_sample, generate_flow=args.generate_flow)
    else:
        # Default run with Tommy Tomato
        run_character_story_pipeline("tommy_tomato", theme_hint=args.theme, render_sample=args.render_sample, generate_flow=args.generate_flow)


if __name__ == "__main__":
    main()
