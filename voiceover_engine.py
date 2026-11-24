"""Voice-Over Engine for B.S Organic Flow Agent.
Generates neural Hindi voiceovers (using Edge-TTS Neural Voices)
and mixes them seamlessly into videos with background audio ducking.
"""

import sys
import os
import asyncio
from pathlib import Path
from typing import List, Tuple, Optional
import edge_tts
import subprocess

from config import OUTPUT_DIR
from merge_clips import get_ffmpeg_path, get_video_duration

DEFAULT_HINDI_VOICE = "hi-IN-MadhurNeural"  # Friendly, natural Indian male narrator
FEMALE_HINDI_VOICE = "hi-IN-SwaraNeural"   # Expressive Indian female narrator


class VoiceoverEngine:
    """Handles neural TTS generation and multi-track audio mixing for shorts."""

    def __init__(self, voice: str = DEFAULT_HINDI_VOICE, temp_dir: Optional[Path] = None):
        self.voice = voice
        self.temp_dir = temp_dir or (OUTPUT_DIR / "_temp_voice")
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self.ffmpeg = get_ffmpeg_path()

    async def generate_beat_clips(self, beats_script: List[Tuple[str, str]]) -> List[Path]:
        """Generates individual audio clips for each story beat with custom rate.
        beats_script: List of (text, rate_str), e.g. [("line 1", "+15%"), ...]
        """
        generated_paths = []
        for idx, (text, rate) in enumerate(beats_script, 1):
            out_file = self.temp_dir / f"vo_beat_{idx:02d}.mp3"
            comm = edge_tts.Communicate(text, self.voice, rate=rate)
            await comm.save(str(out_file))
            generated_paths.append(out_file)
        return generated_paths

    def concatenate_audio_clips(self, audio_paths: List[Path], output_path: Path) -> Path:
        """Losslessly concatenates sequential audio clips into one full track."""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        concat_txt = self.temp_dir / "_concat_list.tmp.txt"
        with open(concat_txt, "w", encoding="utf-8") as f:
            for p in audio_paths:
                f.write(f"file '{p.resolve().as_posix()}'\n")

        cmd = [
            self.ffmpeg, "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(concat_txt),
            "-c", "copy",
            str(output_path),
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        if concat_txt.exists():
            concat_txt.unlink()
        return output_path

    def mix_voiceover_into_video(
        self,
        video_path: Path,
        voiceover_path: Path,
        output_video_path: Path,
        bg_volume: float = 0.25,
        vo_volume: float = 1.0,
    ) -> Path:
        """Mixes voiceover onto video with ambient background ducking."""
        output_video_path.parent.mkdir(parents=True, exist_ok=True)
        cmd = [
            self.ffmpeg, "-y",
            "-i", str(video_path.resolve()),
            "-i", str(voiceover_path.resolve()),
            "-filter_complex",
            f"[0:a]volume={bg_volume}[bg];[1:a]volume={vo_volume}[vo];[bg][vo]amix=inputs=2:duration=first:dropout_transition=2[outa]",
            "-map", "0:v",
            "-map", "[outa]",
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            str(output_video_path.resolve()),
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        return output_video_path

    def cleanup(self):
        """Cleans temporary voice files."""
        import shutil
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)
