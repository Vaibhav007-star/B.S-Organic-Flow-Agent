"""Character Manager Module for B.S Organic Flow Agent.
Manages character profiles, visual consistency anchors, and generation queues
for Google Flow Image and Video generation.
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Optional

from config import BASE_DIR, PROMPTS_FILE
from prompt_manager import PromptManager

CHARACTERS_FILE = BASE_DIR / "characters.json"


class CharacterManager:
    """Handles querying and queuing characters for B.S Organic video & image generation."""

    def __init__(self, char_file: Path = CHARACTERS_FILE):
        self.char_file = Path(char_file)
        self.data: Dict[str, Any] = {}
        self.characters: List[Dict[str, Any]] = []
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
        return self.characters

    def list_characters(self, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Return list of characters, optionally filtered by category."""
        if not category:
            return self.characters
        cat_lower = category.strip().lower()
        return [c for c in self.characters if cat_lower in c.get("category", "").lower()]

    def get_character(self, character_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a single character by ID."""
        clean_id = character_id.strip().lower()
        for c in self.characters:
            if c["id"].lower() == clean_id:
                return c
        return None

    def queue_character_images(self, character_ids: Optional[List[str]] = None, pm: Optional[PromptManager] = None) -> List[str]:
        """Queue 9:16 reference image generation prompts for specified characters (or all)."""
        prompt_mgr = pm or PromptManager()
        target_chars = self.characters
        if character_ids:
            target_ids = {cid.strip().lower() for cid in character_ids}
            target_chars = [c for c in self.characters if c["id"].lower() in target_ids]

        queued_ids = []
        for c in target_chars:
            prompt_text = c.get("image_prompt_9_16")
            if prompt_text:
                item = prompt_mgr.add_prompt(prompt_text)
                queued_ids.append(f"[{c['name']}] -> Prompt ID {item['id']}")

        return queued_ids

    def queue_character_video_hooks(self, character_ids: Optional[List[str]] = None, pm: Optional[PromptManager] = None) -> List[str]:
        """Queue 8-second video hook prompts for specified characters (or all)."""
        prompt_mgr = pm or PromptManager()
        target_chars = self.characters
        if character_ids:
            target_ids = {cid.strip().lower() for cid in character_ids}
            target_chars = [c for c in self.characters if c["id"].lower() in target_ids]

        queued_ids = []
        for c in target_chars:
            prompt_text = c.get("video_prompt_hook_8s")
            if prompt_text:
                item = prompt_mgr.add_prompt(prompt_text)
                queued_ids.append(f"[{c['name']}] -> Prompt ID {item['id']}")

        return queued_ids


if __name__ == "__main__":
    cm = CharacterManager()
    print("=" * 60)
    print(f"  B.S ORGANIC - CHARACTER ROSTER ({len(cm.characters)} Characters)")
    print("=" * 60)
    for c in cm.characters:
        print(f"[{c['category']:<12}] {c['name']:<28} (ID: {c['id']})")
        print(f"   Tagline: {c['tagline']}")
    print("=" * 60)
