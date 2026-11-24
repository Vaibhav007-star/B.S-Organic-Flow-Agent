"""Master 40-Second Story Short Builder for B.S Organic Flow Agent.
Stitches 5 sequential 8-second clips into a 40.0-second vertical 9:16 Full HD Short/Reel,
burns high-retention subtitles via FFmpeg, extracts the hero thumbnail, and prepares metadata.
Supports generating a sample preview short instantly via FFmpeg filter graphs.
"""

import sys
import os
import re
import json
import time
import subprocess
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional

import imageio_ffmpeg
from config import OUTPUT_DIR, BASE_DIR, TARGET_WIDTH, TARGET_HEIGHT
from merge_clips import merge_clips_with_subtitles, get_video_duration, get_ffmpeg_path, purge_raw_clips
from thumbnail_generator import ThumbnailGenerator
from character_manager import CharacterManager

SUBTITLES_DEFAULT = [
    "1. CHEMICAL SOIL STRUGGLE",
    "2. CAPTAIN WIGGLY'S RESCUE",
    "3. ROOT NUTRITION SURGE",
    "4. SUPER HARVEST BLOOM",
    "5. B.S ORGANIC VERMICOMPOST",
]


def render_sample_preview_short(output_file: Path, character_name: str = "Tommy Tomato") -> Path:
    """Renders a complete 40.0-second 9:16 1080x1920 60fps sample Short using FFmpeg synthetic generators.

    Demonstrates the exact 5-beat rhythm, typography, color grading, and timing.
    """
    ffmpeg = get_ffmpeg_path()
    output_file.parent.mkdir(parents=True, exist_ok=True)

    print("=" * 65)
    print(f"🎬 RENDERING 40.0s SAMPLE MASTER SHORT FOR [{character_name}]")
    print(f"Resolution: 1080x1920 (9:16 Full HD) @ 60fps")
    print(f"Output: {output_file.name}")
    print("=" * 65)

    # 5 beats x 8 seconds = 40.0 seconds
    # Beat 1: Dry grey/brown clay (Struggle)
    # Beat 2: Rich dark brown compost pour (Arrival)
    # Beat 3: Deep black subterranean root surge with golden glow
    # Beat 4: Vibrant bright organic emerald & ruby harvest
    # Beat 5: Deep emerald B.S Organic branding hero frame

    filter_complex = (
        # Beat 1: 0-8s Dry Pale Soil
        "color=c=0x6B584E:s=1080x1920:d=8:r=60[b1];"
        "[b1]drawtext=text='BEAT 1\\: THE STRUGGLE':fontsize=56:fontcolor=white:x=(w-text_w)/2:y=300:box=1:boxcolor=black@0.6:boxborderw=20,"
        "drawtext=text='Pale and Dying in Dry Chemical Soil':fontsize=44:fontcolor=white:x=(w-text_w)/2:y=400:box=1:boxcolor=black@0.5:boxborderw=15,"
        f"drawtext=text='{character_name}':fontsize=72:fontcolor=gold:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.7:boxborderw=25[v1];"

        # Beat 2: 8-16s Arrival of Vermicompost
        "color=c=0x382A22:s=1080x1920:d=8:r=60[b2];"
        "[b2]drawtext=text='BEAT 2\\: THE ARRIVAL':fontsize=56:fontcolor=white:x=(w-text_w)/2:y=300:box=1:boxcolor=black@0.6:boxborderw=20,"
        "drawtext=text='Captain Wiggly Brings B.S Organic Gold':fontsize=44:fontcolor=green:x=(w-text_w)/2:y=400:box=1:boxcolor=black@0.5:boxborderw=15,"
        "drawtext=text='Black Gold Compost Applied':fontsize=64:fontcolor=yellow:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.7:boxborderw=25[v2];"

        # Beat 3: 16-24s Subterranean Root Surge
        "color=c=0x1E1815:s=1080x1920:d=8:r=60[b3];"
        "[b3]drawtext=text='BEAT 3\\: UNDERGROUND MAGIC':fontsize=56:fontcolor=white:x=(w-text_w)/2:y=300:box=1:boxcolor=black@0.6:boxborderw=20,"
        "drawtext=text='Roots Drinking Living Microbes':fontsize=44:fontcolor=cyan:x=(w-text_w)/2:y=400:box=1:boxcolor=black@0.5:boxborderw=15,"
        "drawtext=text='Deep Spongy Moisture Retained':fontsize=64:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.7:boxborderw=25[v3];"

        # Beat 4: 24-32s Grand Bloom & Harvest
        "color=c=0x1C4A27:s=1080x1920:d=8:r=60[b4];"
        "[b4]drawtext=text='BEAT 4\\: SUPER HARVEST':fontsize=56:fontcolor=white:x=(w-text_w)/2:y=300:box=1:boxcolor=black@0.6:boxborderw=20,"
        "drawtext=text='Explosion of Color and Plump Juicy Fruit':fontsize=44:fontcolor=yellow:x=(w-text_w)/2:y=400:box=1:boxcolor=black@0.5:boxborderw=15,"
        f"drawtext=text='{character_name} Glorious Bloom':fontsize=68:fontcolor=coral:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.7:boxborderw=25[v4];"

        # Beat 5: 32-40s B.S Organic Brand Hero
        "color=c=0x0E2C17:s=1080x1920:d=8:r=60[b5];"
        "[b5]drawtext=text='B.S ORGANIC VERMICOMPOST':fontsize=64:fontcolor=gold:x=(w-text_w)/2:y=320:box=1:boxcolor=black@0.7:boxborderw=25,"
        "drawtext=text='100 Percent Pure Earthworm Manure':fontsize=46:fontcolor=white:x=(w-text_w)/2:y=430:box=1:boxcolor=black@0.5:boxborderw=15,"
        "drawtext=text='Grow Organic. Eat Pure.':fontsize=58:fontcolor=green:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.7:boxborderw=25,"
        "drawtext=text='Seamless Loop Reset':fontsize=36:fontcolor=white:x=(w-text_w)/2:y=1600:box=1:boxcolor=black@0.5:boxborderw=12[v5];"

        # Concat 5 video streams
        "[v1][v2][v3][v4][v5]concat=n=5:v=1:a=0[vout]"
    )

    cmd = [
        ffmpeg,
        "-y",
        "-f", "lavfi",
        "-i", "anullsrc=r=48000:cl=stereo",
        "-filter_complex", filter_complex,
        "-map", "[vout]",
        "-map", "0:a",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-t", "40.0",
        str(output_file),
    ]

    subprocess.run(cmd, check=True, capture_output=True)

    dur = get_video_duration(output_file)
    print(f"🎉 Generated sample Master Short successfully: {output_file.name} ({dur:.2f}s, {output_file.stat().st_size / (1024*1024):.2f} MB)")
    return output_file


def build_story_master(story_id: str, sample_if_missing: bool = True) -> Path:
    """Finds clips for story_id, stitches them into a 40s Master Short, and extracts best thumbnail."""
    from prompt_manager import PromptManager
    pm = PromptManager()

    story_items = [it for it in pm.items if it.get("story_id") == story_id]
    char_name = story_items[0].get("character_name", "B.S Organic Character") if story_items else "Tommy Tomato"
    out_master = OUTPUT_DIR / f"{story_id}_master_40s.mp4"

    # Check if raw clip files exist on disk
    clip_paths = []
    for it in sorted(story_items, key=lambda x: x.get("beat", 1)):
        fn = it.get("output_file")
        if fn:
            p = OUTPUT_DIR / fn
            if p.exists() and p.stat().st_size > 10000:
                clip_paths.append(p)

    if len(clip_paths) == 5:
        print(f"Found all 5 generated clips for {story_id}. Stitching with subtitles...")
        subtitles = [it.get("beat_title", SUBTITLES_DEFAULT[i]) for i, it in enumerate(story_items)]
        clip_items = [{"path": p, "subtitle": subtitles[i]} for i, p in enumerate(clip_paths)]
        success = merge_clips_with_subtitles(clip_items, out_master, target_res="1080p")
        if not success:
            raise RuntimeError(f"Failed to stitch clips for {story_id}")
        purge_raw_clips(clip_paths)
    elif sample_if_missing:
        print(f"Clips for {story_id} not yet downloaded ({len(clip_paths)}/5 found). Creating 40s sample preview...")
        render_sample_preview_short(out_master, character_name=char_name)
    else:
        raise FileNotFoundError(f"Story {story_id} has only {len(clip_paths)}/5 clips available.")

    # Extract high engagement thumbnail
    print("Extracting hero thumbnail frame...")
    gen = ThumbnailGenerator()
    best_thumb, info = gen.get_best_thumbnail(out_master)
    print(f"Hero Thumbnail: {best_thumb.name} (Score: {info.get('score', 0)})")

    return out_master


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build 40s Master Short for B.S Organic")
    parser.add_argument("--story-id", type=str, default="story_tommy_tomato_sample", help="Story ID to build")
    parser.add_argument("--sample", action="store_true", help="Force render a 40s sample preview short")
    parser.add_argument("--character", type=str, default="Tommy Tomato", help="Character name for demo preview")
    args = parser.parse_args()

    out_file = OUTPUT_DIR / f"{args.story_id}_master_40s.mp4"
    if args.sample or not out_file.exists():
        render_sample_preview_short(out_file, character_name=args.character)
        gen = ThumbnailGenerator()
        best_thumb, info = gen.get_best_thumbnail(out_file)
        print(f"Best Thumbnail: {best_thumb.name}")
    else:
        build_story_master(args.story_id)
