"""Character Manager Module for B.S Organic Flow Agent.
Handles characters according to the story pipeline:
1. Formats character profiles and visual anchors for Gemini / Story Generator.
2. Compiles 5-beat sequential video prompts (40s Master Short = 5 x 8s clips).
3. Queues 5-beat stories into Google Flow automation.
4. Tracks story clip completion status for automated stitching.
"""

import json
import time
import uuid
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

from config import BASE_DIR, PROMPTS_FILE, OUTPUT_DIR
from prompt_manager import PromptManager

CHARACTERS_FILE = BASE_DIR / "characters.json"


class CharacterManager:
    """Manages B.S Organic characters and compiles story-driven prompts for Google Flow."""

    def __init__(self, char_file: Path = CHARACTERS_FILE):
        self.char_file = Path(char_file)
        self.data: Dict[str, Any] = {}
        self.characters: List[Dict[str, Any]] = []
        self.default_style = (
            "Vertical 9:16, high-end 3D animated Pixar-DreamWorks aesthetic, Octane 3D render, "
            "subsurface scattering, tactile organic textures, warm cinematic sunlight, shallow depth of field, 8K resolution"
        )
        self.negative_prompt = (
            "no text, no captions, no logos, no watermark, no human face, no 2D flat drawing, "
            "no grotesque realism, no low poly, no deformed eyes, no camera distortion"
        )
        self.load()

    def load(self) -> List[Dict[str, Any]]:
        """Load character database from characters.json."""
        if not self.char_file.exists():
            self.data = {"brand": "B.S Organic", "characters": []}
            self.characters = []
            return self.characters

        with open(self.char_file, "r", encoding="utf-8") as f:
            self.data = json.load(f)
            self.characters = self.data.get("characters", [])
            self.default_style = self.data.get("default_style", self.default_style)
            self.negative_prompt = self.data.get("negative_prompt", self.negative_prompt)
        return self.characters

    def list_characters(self, category: Optional[str] = None, state: Optional[str] = None) -> List[Dict[str, Any]]:
        """Return list of characters, optionally filtered by category and/or state."""
        results = self.characters
        if category:
            cat_lower = category.strip().lower()
            results = [c for c in results if cat_lower in c.get("category", "").lower()]
        if state:
            st_lower = state.strip().lower()
            results = [c for c in results if st_lower in c.get("state", "").lower()]
        return results

    def get_character(self, character_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a single character by ID."""
        clean_id = character_id.strip().lower()
        for c in self.characters:
            if c["id"].lower() == clean_id:
                return c
        return None

    def get_character_story_context(self, character_id: str) -> Dict[str, Any]:
        """Provides rich context for Gemini to synthesize a 5-beat 40-second organic transformation story."""
        c = self.get_character(character_id)
        if not c:
            raise ValueError(f"Character ID '{character_id}' not found.")

        wiggly = self.get_character("captain_wiggly")
        pack = self.get_character("bs_organic_gold")

        return {
            "brand": "B.S Organic Vermicompost & Manure",
            "featured_character": {
                "id": c["id"],
                "name": c["name"],
                "tagline": c["tagline"],
                "state_region": c.get("state", "Pan-India"),
                "category": c["category"],
                "visual_identity": c["visual_identity"],
                "before_organic_struggle": c["transformation"]["before_organic"],
                "after_organic_triumph": c["transformation"]["after_organic"],
            },
            "hero_companions": {
                "earthworm_mascot": wiggly["name"] if wiggly else "Captain Wiggly",
                "organic_solution": pack["name"] if pack else "B.S Organic Vermicompost Pack",
            },
            "story_guidelines": {
                "total_duration_sec": 40.0,
                "beat_count": 5,
                "beat_duration_sec": 8.0,
                "style_anchor": self.default_style,
                "negative_constraints": self.negative_prompt,
                "beats_structure": [
                    {"beat": 1, "timing": "0.0s - 8.0s", "phase": "The Hook / Peeking Out", "focus": "Crop mascot peeking out of dry cracked soil, rubbing eyes and calling out to farmer (अरे किसान भैया!)"},
                    {"beat": 2, "timing": "8.0s - 16.0s", "phase": "The Struggle / Underground Cross-Section", "focus": "Split view: Namaste pleading above ground while roots struggle in hard compacted chemical soil below"},
                    {"beat": 3, "timing": "16.0s - 24.0s", "phase": "The Solution / B.S Organic Nutrition", "focus": "Dark green B.S Organic bag reveal, dark crumbly vermicompost mixes in, golden glowing nutrients swirl into roots"},
                    {"beat": 4, "timing": "24.0s - 32.0s", "phase": "The Transformation / Tears of Joy", "focus": "Rapid time-lapse surge into bumper growth, mascot crying tears of joy with hand on heart looking at smiling farmer"},
                    {"beat": 5, "timing": "32.0s - 40.0s", "phase": "Bumper Harvest Celebration & CTA", "focus": "Mascot celebrating atop overflowing wicker baskets with B.S Organic bag and ₹150 / 25 kg CTA"},
                ],
            },
        }

    def generate_template_5beat_story(self, character_id: str) -> List[Dict[str, Any]]:
        """Generates standard, tested 5-beat story prompts for any character in B.S Organic roster."""
        c = self.get_character(character_id)
        if not c:
            raise ValueError(f"Character ID '{character_id}' not found.")

        name = c["name"]
        body = c["visual_identity"].get("body", "3D animated plant character")
        setting = c["visual_identity"].get("setting", "rural Indian farm rows")
        before = c["transformation"]["before_organic"]
        after = c["transformation"]["after_organic"]

        beats = [
            {
                "beat": 1,
                "title": f"{name}'s Hook: Peeking Out of Dry Soil",
                "timing": "0.0s - 8.0s",
                "action": f"{name} ({body}) peeking out of dry, pale, cracked soil crust in {setting}, rubbing large sleepy cartoon eyes, looking up earnestly at camera appealing to the farmer with tiny reaching hands. {before}.",
                "audio": "Close-mic ASMR dry wind whistle, brittle soil crack, weak sad sigh. No music.",
                "camera": "Ground-level low-angle push-in, warm early morning sunrise god-rays, soft shallow depth of field.",
            },
            {
                "beat": 2,
                "title": f"{name}'s Plea & Underground Struggle",
                "timing": "8.0s - 16.0s",
                "action": f"Split-level subterranean cross-section: Top half shows {name} standing on dry earth with hands folded in emotional Namaste pleading gesture; bottom half shows macro underground soil with hard compacted earth suffocating thin struggling white roots.",
                "audio": "ASMR muffled dry root stress, mournful wind chime, emotional plea murmur. No music.",
                "camera": "Split-level subterranean cross-section camera, dramatic high-contrast sunlight above and dark dense soil below.",
            },
            {
                "beat": 3,
                "title": "B.S Organic Vermicompost Nutrition & Root Magic",
                "timing": "16.0s - 24.0s",
                "action": f"Hero reveal of authentic dark green woven B.S Organic Vermicompost bag standing on rich soil. Dark, crumbly organic vermicompost cascades around {name}'s base. Underground split-view shows glowing golden biological nutrients swirling into roots which drink deeply and expand effortlessly.",
                "audio": "Velvety compost cascade whoosh, subterranean nutrient bubbling hum, root hydration clicks. No music.",
                "camera": "Slow 180-degree orbit around bag and crop, golden hour sparkle particles, subterranean macro lighting.",
            },
            {
                "beat": 4,
                "title": f"{name}'s Super-Growth & Gratitude",
                "timing": "24.0s - 32.0s",
                "action": f"Rapid time-lapse surge of healthy growth: {name} swells with vibrant energy into {after}. Leaves turn lush mirror-gloss emerald with sparkling dew drops. Mascot beams with tears of joy, hand on heart, looking affectionately at an Indian farmer in kurta and gamchha smiling in soft blurred background.",
                "audio": "Snappy stem surge pop, crisp leaf unfold, triumphant harmonious chime. No music.",
                "camera": "Dynamic low-angle pedestal shot rising with crop growth, golden hour backlighting, cinematic bokeh.",
            },
            {
                "beat": 5,
                "title": "Bumper Harvest Celebration & Brand CTA",
                "timing": "32.0s - 40.0s",
                "action": f"Triumphant harvest celebration: {name} happily waving atop overflowing rustic wicker harvest baskets filled with bumper crop in {setting}. Dark green woven B.S Organic bag stands proudly in center on rich dark soil with golden sparkles. Clean bold text: '₹150 / 25 kg'.",
                "audio": "Joyful rustle, harvest celebration chimes, crisp clean finish breath. No music.",
                "camera": "Wide panoramic pull-back and crane down to hero product bag, warm sunset glow over fertile farm.",
            },
        ]
        return beats

    def compile_beat_prompt(self, character_id: str, beat_info: Dict[str, Any]) -> str:
        """Assembles a single complete Google Flow prompt for one beat, guaranteeing visual consistency."""
        c = self.get_character(character_id)
        if not c:
            raise ValueError(f"Character ID '{character_id}' not found.")

        prompt_parts = [
            f"Vertical 9:16, 3D animated Pixar-DreamWorks style cinema.",
            f"Character: {c['name']} ({c['visual_identity']['body']}).",
            f"Scene Action: {beat_info['action']}",
            f"Cinematography: {beat_info.get('camera', 'Tactile macro shot, golden hour lighting, shallow depth of field, 8K resolution.')}",
            f"Audio: {beat_info.get('audio', 'Close-mic diegetic ASMR only, no background music.')}",
            f"Negative: {self.negative_prompt}",
        ]
        return " ".join(prompt_parts)

    def queue_character_story(
        self,
        character_id: str,
        custom_beats: Optional[List[Dict[str, Any]]] = None,
        pm: Optional[PromptManager] = None,
    ) -> Dict[str, Any]:
        """Compiles and queues all 5 beats of a character story into Google Flow prompt queue."""
        prompt_mgr = pm or PromptManager()
        c = self.get_character(character_id)
        if not c:
            raise ValueError(f"Character ID '{character_id}' not found.")

        beats = custom_beats or self.generate_template_5beat_story(character_id)
        story_id = f"story_{c['id']}_{int(time.time())}"

        queued_items = []
        for b in beats:
            beat_num = b.get("beat", len(queued_items) + 1)
            full_prompt = self.compile_beat_prompt(character_id, b)
            item = prompt_mgr.add_prompt(full_prompt)
            # Annotate prompt item with story metadata
            item["story_id"] = story_id
            item["character_id"] = c["id"]
            item["character_name"] = c["name"]
            item["beat"] = beat_num
            item["beat_title"] = b.get("title", f"Beat {beat_num}")
            item["output_file"] = f"{story_id}_clip_0{beat_num}.mp4"
            queued_items.append(item)

        prompt_mgr.save()

        return {
            "story_id": story_id,
            "character_id": c["id"],
            "character_name": c["name"],
            "category": c["category"],
            "state": c.get("state", "Pan-India"),
            "total_beats": len(queued_items),
            "queued_prompt_ids": [it["id"] for it in queued_items],
            "target_master_video": f"{story_id}_master_40s.mp4",
        }

    def check_story_completion(self, story_id: str, pm: Optional[PromptManager] = None) -> Dict[str, Any]:
        """Checks how many of the 5 beats for a story have completed generation."""
        prompt_mgr = pm or PromptManager()
        story_items = [it for it in prompt_mgr.items if it.get("story_id") == story_id]
        if not story_items:
            return {"story_id": story_id, "found": False, "ready_to_stitch": False}

        completed = [it for it in story_items if it.get("status") == "Completed"]
        failed = [it for it in story_items if it.get("status") == "Failed"]
        pending = [it for it in story_items if it.get("status") in ("Pending", "Processing")]

        ready = len(completed) >= 5 and len(failed) == 0

        return {
            "story_id": story_id,
            "found": True,
            "total_clips": len(story_items),
            "completed": len(completed),
            "failed": len(failed),
            "pending": len(pending),
            "ready_to_stitch": ready,
            "completed_files": [it.get("output_file") for it in completed if it.get("output_file")],
        }


if __name__ == "__main__":
    cm = CharacterManager()
    print("=" * 65)
    print("  B.S ORGANIC STORY-DRIVEN CHARACTER MANAGER")
    print("=" * 65)
    demo_char = "tommy_tomato"
    ctx = cm.get_character_story_context(demo_char)
    print(f"\nStory Context for [{ctx['featured_character']['name']}]:")
    print(f"Struggle: {ctx['featured_character']['before_organic_struggle']}")
    print(f"Triumph:  {ctx['featured_character']['after_organic_triumph']}")
    print("\nSample Beat 1 Prompt:")
    sample_beats = cm.generate_template_5beat_story(demo_char)
    print(cm.compile_beat_prompt(demo_char, sample_beats[0]))
    print("=" * 65)
