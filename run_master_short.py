"""Autonomous Runner for B.S Organic 'किसान से एक विनती' 40s Master Short.
Executes the 5 beats on Google Flow, monitors generation progress,
downloads clips, merges into a seamless 40s master short, and creates a hero thumbnail.
"""

import sys
import time
import logging
from pathlib import Path

from config import STATE_FILE, OUTPUT_DIR
from flow_automation import GoogleFlowAutomation
from prompt_manager import PromptManager
from merge_clips import auto_merge_sequence_from_state

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("run_master_short")


def main():
    story_id = "story_kisan_appeal_master_40s"
    logger.info("=" * 65)
    logger.info(f"🚀 INITIATING AUTONOMOUS GENERATION: {story_id}")
    logger.info("=" * 65)

    pm = PromptManager()
    pending = pm.get_pending_prompts(story_id=story_id)
    logger.info(f"Found {len(pending)} pending beats for {story_id}")

    if not pending:
        logger.info("No pending beats found. Checking if already completed...")
        merged = auto_merge_sequence_from_state(target_count=5, story_id=story_id)
        if merged:
            logger.info(f"Master video already merged: {merged}")
        return

    for idx, p in enumerate(pending, 1):
        logger.info(f"  Beat {p.get('beat', idx)}: {p['prompt'][:80]}...")

    # Launch Google Flow automation queue
    automation = GoogleFlowAutomation(prompt_manager=pm)
    summary = automation.run_queue(story_id=story_id)
    logger.info(f"Automation execution finished. Summary: {summary}")

    # Verify and merge
    merged_video = auto_merge_sequence_from_state(target_count=5, story_id=story_id)
    if merged_video and merged_video.exists():
        logger.info("=" * 65)
        logger.info(f"🎉 MASTER 40s SHORT PRODUCED SUCCESSFULLY: {merged_video.name}")
        logger.info("=" * 65)

        # Generate hero thumbnail
        try:
            from thumbnail_generator import ThumbnailGenerator
            tg = ThumbnailGenerator()
            hero_thumb = tg.pick_best_thumbnail(merged_video)
            logger.info(f"🌟 Hero thumbnail created: {hero_thumb}")
        except Exception as e:
            logger.warning(f"Thumbnail generation notice: {e}")
    else:
        logger.warning("Pipeline finished but master video was not merged. Check clip status.")


if __name__ == "__main__":
    main()
