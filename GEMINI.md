# 🚀 B.S ORGANIC FLOW AGENT — AUTONOMOUS VIDEO PIPELINE SPECIFICATION

These instructions are persistent operational rules for all video generation, prompt synthesis, video stitching, and multi-platform publishing tasks in this workspace.

---

## 1. ⏱️ VIDEO ARCHITECTURE & STANDARDS
- **Format**: Vertical 9:16 Full HD (`1080x1920` @ 60fps) with Lanczos multi-tap scaling. Never output in 720p.
- **Engine**: Google Flow (Veo) automated generation, high-fidelity downloading, and FFmpeg post-processing.
- **Audio Quality**: Close-mic diegetic ASMR audio or pristine sound design aligned with the chosen niche.
- **Clean Visuals**: AI generation prompts must include `no text, no captions, no logos, no watermark`. Typography and branding are burned natively via FFmpeg.

---

## 2. 🗄️ PROMPT MANAGEMENT & NICHES
- Prompts are queued in `prompts.txt` and tracked in `prompts_state.json`.
- State tracking records prompt lifecycle: `Pending` -> `Processing` -> `Completed` -> `Failed`.
- Niche templates are placed in `prompt_templates/`.

---

## 3. 🎯 ANTI-REPETITION & VARIETY ENFORCEMENT
- Check `generation_history.json` before triggering generations to ensure content variety and avoid duplicates.
- Conserve Google Flow generation capacity and API quotas.

---

## 4. 📅 SCHEDULING & PUBLISHING DISCIPLINE
- **Daily Peak Slots (IST)**:
  - **Slot A**: **1:30 PM IST** (`08:00:00Z`)
  - **Slot B**: **8:00 PM IST** (`14:30:00Z`)
- **Privacy**: Default to `private` with scheduled `publishAt` ISO 8601 timestamps.
- **Thumbnails**: Use `thumbnail_generator.py` to pick the frame with the highest engagement score.
- **SEO**: Clean all hashtags from YouTube Data API tags (API tags cannot contain `#`). Include `#Shorts` in the video title.

---

## 5. 🧹 AUTOMATIC CLEANLINESS & DISK MAINTENANCE
- Automatically delete intermediate raw clips (`clip_*.mp4`, `video_*.mp4`) once merged or uploaded.
- Clean temporary concat files (`*.tmp.txt`) and intermediate candidate thumbnails.
- Keep only final masters and the hero thumbnail (`*_best.jpg`) to preserve laptop disk space.

---

## 6. 🌿 MANDATORY B.S ORGANIC VERMICOMPOST BRANDING & PRODUCT RULE
- **Strict Brand Identity**: Whenever vermicompost, organic manure, or bio-fertilizer is referenced, depicted, or used anywhere in any prompt, story script, voice-over, or visual scene, it **MUST ALWAYS BE "B.S Organic"**. Generic or third-party fertilizer representations are strictly forbidden.
- **Official Product Reference**:
  - Always anchor vermicompost visuals to the authentic B.S Organic bag (`assets/bs_organic_bag_reference.jpg` and any upcoming product images provided by the user).
  - Locked packaging elements: Dark-green glossy woven poly bag tied with white string at the top, white cloud-shaped logo with leaf icon reading `"B.S. Organic"`, `"100% CHEMICAL FREE ✓"`, Hindi banner `"केंचुओ द्वारा निर्मित प्राकृतिक खाद"`, `"VERMICOMPOST"`, Hindi tagline `"प्रकृति के लिए प्राकृतिक"`, and round badge `"नीम व गाय मूत्र युक्त"`.
  - Canonical pricing CTA: `"₹150 / 25 kg"` (or `"Rs. 150 / 25 kg"`).
- **Future Product Image Updates**: Whenever the user uploads or specifies a new product packaging image, immediately adopt it as the canonical reference asset across all generation prompts, visual anchors, and FFmpeg composite overlays.
