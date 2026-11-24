"""Post-processing script for B.S Organic 40s Master Short.
Scales to Full HD 1080x1920 @ 60fps with Lanczos multi-tap scaling,
burns native high-impact Hindi typography & CTA pricing on Beat 5,
and generates the hero thumbnail via engagement scoring.
"""

import sys
import subprocess
from pathlib import Path
from merge_clips import get_ffmpeg_path, get_video_duration, get_subtitle_font_path
from thumbnail_generator import ThumbnailGenerator
from config import OUTPUT_DIR

input_video = OUTPUT_DIR / "story_kisan_appeal_master_40s_master_40s.mp4"
final_master = OUTPUT_DIR / "kisan_appeal_40s_master_1080p.mp4"

if not input_video.exists():
    print(f"Error: {input_video} not found.")
    sys.exit(1)

total_dur = get_video_duration(input_video)
print(f"Input Master Duration: {total_dur:.2f}s")

ffmpeg = get_ffmpeg_path()
font_path = get_subtitle_font_path().replace(":", r"\:")

# Filter graph:
# 1. Lanczos scaling to 1080x1920, unsharp mask for crystalline clarity, 60fps fps conversion
# 2. Burn CTA typography in the last 6 seconds (t >= 34.0s)
cta_start = max(0.0, total_dur - 6.0)

filter_complex = (
    f"[0:v]scale=1080:1920:flags=lanczos,unsharp=3:3:0.5:3:3:0.0,fps=60,"
    f"drawtext=fontfile='{font_path}':text='B.S ORGANIC':fontcolor=white:fontsize=80:borderw=5:bordercolor=black:"
    f"shadowcolor=black@0.6:shadowx=3:shadowy=3:x=(w-text_w)/2:y=240:enable='gte(t,{cta_start})',"
    f"drawtext=fontfile='{font_path}':text='Rs. 150 / 25 kg':fontcolor=#FFE000:fontsize=120:borderw=6:bordercolor=black:"
    f"shadowcolor=black@0.7:shadowx=4:shadowy=4:x=(w-text_w)/2:y=1550:enable='gte(t,{cta_start})',"
    f"drawtext=fontfile='{font_path}':text='100 PERCENT CHEMICAL FREE':fontcolor=white:fontsize=55:borderw=4:bordercolor=black:"
    f"shadowcolor=black@0.6:shadowx=3:shadowy=3:x=(w-text_w)/2:y=1700:enable='gte(t,{cta_start})'[outv]"
)

cmd = [
    ffmpeg,
    "-y",
    "-i", str(input_video.resolve()),
    "-filter_complex", filter_complex,
    "-map", "[outv]",
    "-map", "0:a?",
    "-c:v", "libx264",
    "-preset", "slow",
    "-crf", "17",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    str(final_master.resolve()),
]

print("Executing 1080x1920 @ 60fps Lanczos master render with native CTA...")
subprocess.run(cmd, check=True)

out_dur = get_video_duration(final_master)
print(f"🎉 Render Complete: {final_master.name} ({out_dur:.2f}s, {final_master.stat().st_size} bytes)")

# Generate hero thumbnail
tg = ThumbnailGenerator(output_dir=OUTPUT_DIR / "thumbnails")
sample_timestamps = [1.5, 4.0, 9.5, 13.0, 17.5, 21.0, 25.5, 29.0, 33.5, 37.0, 39.0]
hero_thumb = tg.pick_best_thumbnail(final_master, timestamps=sample_timestamps)
print(f"🌟 Hero Thumbnail Selected: {hero_thumb.name} ({hero_thumb.stat().st_size} bytes)")

# Clean intermediate 720p master per GEMINI.md Rule 5
try:
    input_video.unlink()
    print(f"🧹 Cleaned intermediate 720p master to preserve disk space: {input_video.name}")
except Exception as e:
    print(f"Notice cleaning intermediate master: {e}")
