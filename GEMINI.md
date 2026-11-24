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
