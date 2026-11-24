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


def build_commercial_40s_master(output_file: Optional[Path] = None) -> Path:
    """Builds the official 40.0s photoreal B.S Organic Commercial Master Short (1080x1920 @ 60fps)."""
    ffmpeg = get_ffmpeg_path()
    out_master = output_file or (OUTPUT_DIR / "bs_organic_commercial_40s_master.mp4")
    bag_ref = BASE_DIR / "assets" / "bs_organic_bag_reference.jpg"
    flow_clip = OUTPUT_DIR / "google_flow_sample_tomato_omni.mp4"

    filter_complex = (
        "[0:v]split=2[bag1][bag2];"
        "color=c=0x5A4A3E:s=1080x1920:d=8:r=60[b1];"
        "[b1]drawtext=text='01. HOOK - DRY CRACKED SOIL':fontsize=52:fontcolor=white:x=(w-text_w)/2:y=240:box=1:boxcolor=black@0.7:boxborderw=18,"
        "drawtext=text='Kya aapki mitti bhi thaki aur bejaan ho gayi hai?':fontsize=46:fontcolor=yellow:x=(w-text_w)/2:y=1560:box=1:boxcolor=black@0.85:boxborderw=20,"
        "drawtext=text='Kya fasal mein woh dam nahi raha?':fontsize=40:fontcolor=white:x=(w-text_w)/2:y=1640:box=1:boxcolor=black@0.8:boxborderw=16[v1];"
        "color=c=0x3D2C1E:s=1080x1920:d=8:r=60[b2];"
        "[b2]drawtext=text='02. PROBLEM TO HOPE':fontsize=52:fontcolor=white:x=(w-text_w)/2:y=240:box=1:boxcolor=black@0.7:boxborderw=18,"
        "drawtext=text='Rasayanik khaad se zameen kamzor hoti jati hai':fontsize=44:fontcolor=coral:x=(w-text_w)/2:y=1560:box=1:boxcolor=black@0.85:boxborderw=20,"
        "drawtext=text='Ab waqt hai mitti ko phir se jaan dene ka!':fontsize=44:fontcolor=gold:x=(w-text_w)/2:y=1640:box=1:boxcolor=black@0.8:boxborderw=18[v2];"
        "[bag1]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=60,trim=duration=8,"
        "drawtext=text='03. PRODUCT REVEAL':fontsize=52:fontcolor=white:x=(w-text_w)/2:y=200:box=1:boxcolor=0x0E3A1A@0.85:boxborderw=18,"
        "drawtext=text='B.S. ORGANIC VERMICOMPOST':fontsize=64:fontcolor=gold:x=(w-text_w)/2:y=290:box=1:boxcolor=black@0.8:boxborderw=22,"
        "drawtext=text='Pesh hai B.S. Organic Vermicompost!':fontsize=46:fontcolor=white:x=(w-text_w)/2:y=1560:box=1:boxcolor=0x0E3A1A@0.9:boxborderw=20,"
        "drawtext=text='Kenchuo dwara bani prakritik khaad, 100 Percent Chemical Free!':fontsize=36:fontcolor=gold:x=(w-text_w)/2:y=1640:box=1:boxcolor=black@0.85:boxborderw=16[v3];"
        "[1:v]scale=1080:1920:flags=lanczos,fps=60,trim=duration=8,"
        "drawtext=text='04. BENEFIT - LIVING SOIL NUTRITION':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=200:box=1:boxcolor=0x0E3A1A@0.85:boxborderw=18,"
        "drawtext=text='Mitti bane upjaau, jadein hon mazboot...':fontsize=44:fontcolor=white:x=(w-text_w)/2:y=1560:box=1:boxcolor=black@0.85:boxborderw=20,"
        "drawtext=text='Aur fasal hari-bhari, bharpoor paidawar ke saath!':fontsize=40:fontcolor=gold:x=(w-text_w)/2:y=1640:box=1:boxcolor=black@0.85:boxborderw=16[v4];"
        "[bag2]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=60,trim=duration=8,"
        "drawtext=text='B.S. ORGANIC':fontsize=76:fontcolor=white:x=(w-text_w)/2:y=180:box=1:boxcolor=0x0E3A1A@0.9:boxborderw=24,"
        "drawtext=text='Prakriti Ke Liye Prakritik':fontsize=44:fontcolor=gold:x=(w-text_w)/2:y=280:box=1:boxcolor=black@0.8:boxborderw=16,"
        "drawtext=text='Sirf Rs 150 mein 25 Kilo! Aaj hi order karein.':fontsize=42:fontcolor=white:x=(w-text_w)/2:y=1460:box=1:boxcolor=black@0.85:boxborderw=18,"
        "drawtext=text='Rs 150 / 25 kg':fontsize=92:fontcolor=gold:x=(w-text_w)/2:y=1580:box=1:boxcolor=0x0E3A1A@0.95:boxborderw=28,"
        "drawtext=text='100 Percent CHEMICAL FREE':fontsize=46:fontcolor=white:x=(w-text_w)/2:y=1710:box=1:boxcolor=black@0.85:boxborderw=16[v5];"
        "[v1][v2][v3][v4][v5]concat=n=5:v=1:a=0[vout]"
    )

    flow_input = str(flow_clip) if flow_clip.exists() else str(bag_ref)
    cmd = [
        ffmpeg,
        "-y",
        "-loop", "1", "-i", str(bag_ref),
        "-i", flow_input,
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
        "-filter_complex", filter_complex,
        "-map", "[vout]",
        "-map", "2:a",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-r", "60",
        "-c:a", "aac",
        "-t", "40.0",
        str(out_master),
    ]

    subprocess.run(cmd, check=True, capture_output=True)
    return out_master


def build_story_master(story_id: str, sample_if_missing: bool = True) -> Path:
    """Finds clips for story_id, stitches them into a 40s Master Short, and extracts best thumbnail."""
    from prompt_manager import PromptManager
    pm = PromptManager()

    if story_id in ("bs_organic_master_commercial_40s", "bs_organic_commercial_40s"):
        out_master = OUTPUT_DIR / f"{story_id}_master_40s.mp4"
        print(f"Building official 40.0s Commercial Master for {story_id}...")
        build_commercial_40s_master(out_master)
        gen = ThumbnailGenerator()
        best_thumb, info = gen.get_best_thumbnail(out_master)
        print(f"Hero Thumbnail: {best_thumb.name} (Score: {info.get('score', 0)})")
        return out_master

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
