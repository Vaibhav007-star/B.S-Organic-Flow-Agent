"""Gemini Story Engine for B.S Organic Video Pipeline.
Uses the Gemini API to write high-retention 40-second organic transformation stories
(5 beats x 8.0s) tailored to any character from the B.S Organic character database.
"""

import os
import json
import time
import logging
from typing import Dict, Any, List, Optional
import requests

from config import GEMINI_API_KEY, GEMINI_MODEL
from character_manager import CharacterManager
from prompt_manager import PromptManager

logger = logging.getLogger("flow_automation.gemini")
logger.setLevel(logging.INFO)


class GeminiStoryEngine:
    """Generates 5-beat viral story arcs and compiles Google Flow prompts using Gemini API."""

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key or GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")
        self.model = model or GEMINI_MODEL or "gemini-3.5-flash"
        self.cm = CharacterManager()
        self.client = None
        self._init_client()

    def _init_client(self):
        """Initializes google-genai Client if API key is present."""
        if not self.api_key:
            logger.warning("GEMINI_API_KEY is not set. Stories will use built-in template beats.")
            return

        try:
            from google import genai
            self.client = genai.Client(api_key=self.api_key)
            logger.info(f"Initialized Gemini Client with model: {self.model}")
        except Exception as e:
            logger.warning(f"Could not initialize google-genai client: {e}. Will use REST API fallback.")
            self.client = None

    def generate_story(self, character_id: str, theme_hint: Optional[str] = None) -> Dict[str, Any]:
        """Generates a complete 5-beat 40-second transformation story for the specified character."""
        c = self.cm.get_character(character_id)
        if not c:
            raise ValueError(f"Character ID '{character_id}' not found in database.")

        ctx = self.cm.get_character_story_context(character_id)

        # Fallback to local template if no API key is provided
        if not self.api_key:
            logger.info(f"No API key provided, compiling template 5-beat story for {c['name']}...")
            template_beats = self.cm.generate_template_5beat_story(character_id)
            return {
                "story_title": f"{c['name']}'s B.S Organic Transformation",
                "character_id": c["id"],
                "character_name": c["name"],
                "category": c["category"],
                "state": c.get("state", "Pan-India"),
                "caption": (
                    f"Watch {c['name']} transform from wilting to super-harvest with B.S Organic Vermicompost! 🌿✨ "
                    f"100% pure organic manure made with love by earthworms. "
                    f"Which crop should we revive next? 👇\n\n"
                    f"#BSOrganic #Vermicompost #OrganicFarming #TerraceGardening #KitchenGarden #GrowYourOwn #Reels #Shorts"
                ),
                "beats": template_beats,
                "generated_by": "template_engine",
            }

        # Build prompt for Gemini
        system_instruction = (
            "You are the Lead Creative Director & AI Cinematographer for 'B.S Organic', a premium organic vermicompost and manure brand. "
            "Your mission is to write a high-velocity, emotional, visually stunning 40.0-second short-form video story titled 'किसान से एक विनती' "
            "consisting of EXACTLY 5 sequential 8.0-second beats for vertical 9:16 video generation in Google Flow (Veo / Gemini Omni 1.2). "
            "The style is 3D Pixar-DreamWorks animated crop mascot integrated into photorealistic Indian farm rows with an authentic Indian farmer. "
            "Every story follows the crop's heartfelt emotional appeal to the farmer, subterranean root cross-sections, B.S Organic nutrition, and bumper harvest. "
            "Output MUST be strict JSON matching the requested schema."
        )

        user_prompt = f"""
Character Context:
{json.dumps(ctx, indent=2, ensure_ascii=False)}

Theme / Special Setting: {theme_hint or 'Authentic rural Indian farm rows with farmer'}

Story Requirements:
1. Exactly 5 beats (each representing an 8.0-second clip, totaling 40.0 seconds).
   - Beat 1 (0-8s): The Hook / Peeking Out. Crop mascot peeks out of dry cracked soil, rubbing sleepy eyes, calling out to farmer (अरे किसान भैया!).
   - Beat 2 (8-16s): The Struggle / Underground Cross-Section. Split view: Crop folds hands in Namaste pleading for natural care above ground, while underground cross-section shows roots suffocating in hard compacted chemical soil.
   - Beat 3 (16-24s): B.S Organic Nutrition. Hero reveal of authentic dark green B.S Organic vermicompost bag, dark crumbly manure mixes into soil, golden glowing nutrients surge into roots.
   - Beat 4 (24-32s): The Transformation / Tears of Gratitude. Rapid healthy surge into massive juicy produce, mascot weeping tears of joy with hand on heart looking at the smiling Indian farmer.
   - Beat 5 (32-40s): Bumper Harvest Celebration & Brand CTA. Mascot celebrating atop overflowing rustic wicker harvest baskets with hero B.S Organic bag on rich dark soil, with clean bold text '₹150 / 25 kg'.
2. In each beat, write:
   - 'title': Short descriptive title.
   - 'timing': Exact seconds range.
   - 'action': Specific 3D animated visual action.
   - 'camera': Lens, lighting, cinematography.
   - 'audio': Close-mic diegetic ASMR sounds only (no background music).
3. Generate a viral social media caption with clean hashtags.

Return ONLY a valid JSON object with keys:
'story_title', 'caption', 'beats' (list of 5 objects with keys: 'beat', 'title', 'timing', 'action', 'camera', 'audio').
"""

        # Call Gemini via google-genai SDK or REST API
        raw_text = ""
        candidate_models = [self.model, "gemini-3.7-flash", "gemini-3.5-flash-lite"]
        # Remove duplicates while preserving order
        candidate_models = list(dict.fromkeys(candidate_models))

        for m in candidate_models:
            try:
                if self.client:
                    from google.genai import types
                    response = self.client.models.generate_content(
                        model=m,
                        contents=user_prompt,
                        config=types.GenerateContentConfig(
                            system_instruction=system_instruction,
                            response_mime_type="application/json",
                            temperature=0.7,
                        ),
                    )
                    raw_text = response.text
                else:
                    raw_text = self._call_rest_api(system_instruction, user_prompt, model_override=m)

                if raw_text:
                    logger.info(f"Generated story successfully with model: {m}")
                    break
            except Exception as e:
                logger.warning(f"Generation attempt with {m} failed: {e}. Trying next fallback...")
                time.sleep(1)

        # Parse JSON output
        parsed = self._clean_and_parse_json(raw_text) if raw_text else None
        if not parsed or "beats" not in parsed:
            logger.warning("Could not parse valid story JSON from Gemini. Falling back to template.")
            template_beats = self.cm.generate_template_5beat_story(character_id)
            return {
                "story_title": f"{c['name']}'s B.S Organic Transformation",
                "character_id": c["id"],
                "character_name": c["name"],
                "category": c["category"],
                "state": c.get("state", "Pan-India"),
                "caption": f"Watch {c['name']} transform with B.S Organic Vermicompost! 🌿✨ #BSOrganic #OrganicFarming",
                "beats": template_beats,
                "generated_by": "template_fallback",
            }

        return {
            "story_title": parsed.get("story_title", f"{c['name']}'s Organic Story"),
            "character_id": c["id"],
            "character_name": c["name"],
            "category": c["category"],
            "state": c.get("state", "Pan-India"),
            "caption": parsed.get("caption", ""),
            "beats": parsed.get("beats", []),
            "generated_by": f"gemini_{self.model}",
        }

    def _call_rest_api(self, system_inst: str, user_prompt: str, model_override: Optional[str] = None) -> str:
        """Direct REST API fallback to generativelanguage.googleapis.com."""
        target_model = model_override or self.model
        endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{target_model}:generateContent?key={self.api_key}"
        payload = {
            "system_instruction": {"parts": [{"text": system_inst}]},
            "contents": [{"parts": [{"text": user_prompt}]}],
            "generationConfig": {"response_mime_type": "application/json", "temperature": 0.7},
        }
        res = requests.post(endpoint, json=payload, timeout=45)
        if res.status_code != 200:
            raise RuntimeError(f"Gemini REST API error {res.status_code}: {res.text}")
        data = res.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]

    def _clean_and_parse_json(self, text: str) -> Optional[Dict[str, Any]]:
        """Cleans code blocks and extracts JSON object."""
        if not text:
            return None
        cleaned = text.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        elif cleaned.startswith("```"):
            cleaned = cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()

        try:
            return json.loads(cleaned)
        except Exception:
            start = cleaned.find("{")
            end = cleaned.rfind("}")
            if start != -1 and end != -1:
                try:
                    return json.loads(cleaned[start : end + 1])
                except Exception:
                    pass
        return None

    def generate_and_queue(self, character_id: str, theme_hint: Optional[str] = None, pm: Optional[PromptManager] = None) -> Dict[str, Any]:
        """Generates a Gemini story and queues all 5 beats into Google Flow prompt queue."""
        story_data = self.generate_story(character_id, theme_hint)
        c = self.cm.get_character(character_id)
        if not c:
            raise ValueError(f"Character ID '{character_id}' not found.")

        story_id = f"story_{c['id']}_{int(time.time())}"
        prompt_mgr = pm or PromptManager()

        queued_items = []
        for idx, b in enumerate(story_data["beats"], 1):
            full_prompt = self.cm.compile_beat_prompt(character_id, b)
            item = prompt_mgr.add_prompt(full_prompt)
            item["story_id"] = story_id
            item["character_id"] = c["id"]
            item["character_name"] = c["name"]
            item["beat"] = idx
            item["beat_title"] = b.get("title", f"Beat {idx}")
            item["output_file"] = f"{story_id}_clip_0{idx}.mp4"
            queued_items.append(item)

        prompt_mgr.save()

        return {
            "story_id": story_id,
            "story_title": story_data["story_title"],
            "character_id": c["id"],
            "character_name": c["name"],
            "caption": story_data["caption"],
            "total_beats": len(queued_items),
            "queued_prompt_ids": [it["id"] for it in queued_items],
            "target_master_video": f"{story_id}_master_40s.mp4",
            "generated_by": story_data.get("generated_by", "unknown"),
        }


if __name__ == "__main__":
    import sys
    char_arg = sys.argv[1] if len(sys.argv) > 1 else "himachali_seb"
    engine = GeminiStoryEngine()
    print("=" * 65)
    print(f"  B.S ORGANIC GEMINI STORY GENERATOR ({char_arg})")
    print("=" * 65)
    story = engine.generate_story(char_arg)
    print(f"Title: {story['story_title']}")
    print(f"Character: {story['character_name']} ({story['state']})")
    print(f"Engine: {story['generated_by']}")
    print(f"Caption: {story['caption'][:100]}...")
    print(f"\nBeat 1: {story['beats'][0]['title']}")
    print(f"Action: {story['beats'][0]['action']}")
    print("=" * 65)
