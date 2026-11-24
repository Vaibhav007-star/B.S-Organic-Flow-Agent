# 🚀 B.S Organic Flow Agent

Autonomous AI Video Pipeline for **Google Flow (Veo)**, **YouTube Shorts**, and **Instagram Reels**. Built with Python 3.12, Playwright persistent browser automation, multi-clip merging engine, and an interactive Streamlit management dashboard.

---

## 📑 Table of Contents
- [Architecture Overview](#architecture-overview)
- [Key Features](#key-features)
- [Prerequisites](#prerequisites)
- [Quick Start Guide](#quick-start-guide)
- [Project Structure](#project-structure)
- [Running the Automation](#running-the-automation)
  - [Web Dashboard (Streamlit)](#web-dashboard-streamlit)
  - [CLI & Autopilot](#cli--autopilot)
  - [YouTube Shorts Scheduling](#youtube-shorts-scheduling)
  - [Meta Business Suite (Instagram Reels)](#meta-business-suite-instagram-reels)

---

## 🏗️ Architecture Overview

The system automates the complete lifecycle of viral short-form videos for any chosen niche:

```
B.S-Organic-Flow-Agent/
├── app.py                     # Streamlit Web UI (Queue controls, Video Gallery, Logs)
├── config.py                  # Environment configuration & path resolution
├── flow_automation.py         # Google Flow UI interaction, adaptive selectors, generation watcher
├── browser_manager.py         # Playwright browser controller with persistent profile (.browser_data)
├── downloader.py              # Video download handler, blob exporter, file integrity verification
├── merge_clips.py             # Multi-clip FFmpeg stitcher (1080x1920 60fps, Lanczos, subtitles, transitions)
├── prompt_manager.py          # Prompt queue state management & JSON persistence
├── prompts.txt                # Plain-text queue of video prompts
├── thumbnail_generator.py     # Hero frame extraction and engagement scoring
├── yt_uploader.py             # YouTube Data API v3 uploader & peak slot scheduler
├── meta_reels_automation.py   # Meta Business Suite Instagram Reels automation
├── meta_browser_manager.py    # Playwright browser session for Meta
├── autopilot.py               # Autonomous end-to-end loop runner
├── requirements.txt           # Dependency specifications
├── .env.example               # Sample environment variables
└── output_videos/             # Destination folder for completed .mp4 videos
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- **Windows 10 / 11**
- **Python 3.11+**
- **FFmpeg** installed and in system `PATH`
- Active Google account with access to **Google Flow** (`flow.google.com`)

### 2. Setup Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

### 3. Log In to Google Flow (One-Time Setup)
```powershell
python main.py --login
```
Sign in to your Google Account. Once the Google Flow studio loads, close the browser window. Session data is safely preserved in `.browser_data/`.

---

## 🖥️ Running the Automation

### Web Dashboard (Streamlit)
```powershell
streamlit run app.py
```
Open `http://localhost:8501` to:
- Monitor and control video generation queue.
- Preview generated clips and merged Shorts in the Video Gallery.
- View live browser logs and diagnostic metrics.

### Command Line Autopilot
```powershell
python autopilot.py
```
