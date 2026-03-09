# Aura - Standalone Wellness Hub

This folder contains a **standalone version** of the Aura Wellness Hub that works without a backend server.

## Relationship to Main Project

| Component | Location | Description |
|-----------|----------|-------------|
| **Main Project** | Root folder | Full-stack with Flask + Azure OpenAI |
| **Standalone Aura** | This folder | Browser-only, local fallback responses |

## When to Use This Version

- **No Python/Server** - Works by opening HTML directly
- **Offline Demo** - No internet required (except voice features)
- **Quick Preview** - Instant access without setup

## Files

```
Aura/
├── aura_wellness_hub.html    # Standalone wellness app
├── games/                    # Wellness game collection
│   ├── wellness_snake.html
│   ├── memory_cards.html
│   ├── sudoku_puzzle.html
│   └── zen_garden.html
└── README.md                 # This file
```

## Quick Start

Simply open `aura_wellness_hub.html` in a web browser.

## Comparison

| Feature | Standalone (This) | Full Stack (Root) |
|---------|-------------------|-------------------|
| AI Responses | Local fallback | Azure OpenAI GPT-4 |
| Server Required | No | Yes (Flask) |
| Analytics | Browser localStorage | Streamlit Dashboard |
| Voice | Web Speech API | Web Speech API |
| Games | Included | Included |

## For Full Features

Use the main project in the root folder:

```bash
cd ..
pip install -r requirements.txt
python app.py
```

Access at http://localhost:5000

---

**Part of EA Aura Wellness Hub - EA Hackathon 2025**
