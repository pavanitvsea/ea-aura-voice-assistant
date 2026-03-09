# EA Aura - Project Summary

## EA Hackathon 2025

### Overview

EA Aura is an AI-powered wellness platform combining health coaching, financial wellness tools, gamification, and analytics in one seamless experience.

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    EA AURA PLATFORM                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │  index.html  │  │   app.py     │  │ dashboard_   │   │
│  │  (Frontend)  │  │   (Flask)    │  │  app.py      │   │
│  │              │  │              │  │  (Streamlit) │   │
│  │ • AI Chat    │  │ • API Server │  │ • KPI Charts │   │
│  │ • Voice      │  │ • OpenAI     │  │ • Analytics  │   │
│  │ • Budget     │  │ • Wellness   │  │ • Export     │   │
│  │ • Games      │  │   Tips       │  │              │   │
│  └──────────────┘  └──────────────┘  └──────────────┘   │
│                           │                              │
│                    ┌──────┴──────┐                       │
│                    │ config_     │                       │
│                    │ openAI.py   │                       │
│                    │ (Azure AI)  │                       │
│                    └─────────────┘                       │
└─────────────────────────────────────────────────────────┘
```

---

## Core Features

### Wellness Hub (`index.html`)

| Tab | Features |
|-----|----------|
| **Wellness** | Track steps, sleep, mood, focus; earn coins |
| **Wealth** | Budget calculator, emergency fund planner |
| **Games** | Link to cognitive wellness game hub |
| **Help** | Medical insurance, FoodBook app, fitness videos |

### Voice Controls
- **🔊 Voice On/Off** - Toggle spoken AI responses
- **🎤 Speech Input** - Ask questions by voice

### Financial Tools
- **Budget Calculator** - Enter income, see 50/30/20 split
- **Emergency Fund** - Calculate 3/6/12 month savings goal

### AI Assistant (Aura)
- Health and wellness advice
- Financial wellness guidance
- Smart fallback when offline

---

## Streamlit Dashboard

Run: `streamlit run dashboard_app.py`

| Tab | Content |
|-----|---------|
| Overview | DAU/MAU trends, session activity |
| User Metrics | Retention funnel, interaction stats |
| Feedback | Satisfaction gauge, rating distribution |
| About | Platform documentation |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML5, CSS3, JavaScript ES6+ |
| Voice | Web Speech API |
| Backend | Python, Flask |
| AI | Azure OpenAI (GPT-4o) |
| Dashboard | Streamlit, Plotly |
| Data | Pandas, NumPy |

---

## Files

| File | Purpose |
|------|---------|
| `index.html` | Main wellness app (all features) |
| `app.py` | Flask API server |
| `config_openAI.py` | Azure OpenAI config |
| `dashboard_app.py` | Streamlit KPI dashboard |
| `Hackathon_Dashboard.py` | Generate sample data |
| `requirements.txt` | Python dependencies |
| `games/index.html` | Game Hub |

---

## Quick Demo

1. **Open** `index.html` in browser
2. **Try** the Budget Calculator in Wealth tab
3. **Chat** with Aura AI assistant
4. **Use Voice** - click 🎤 to speak
5. **Run Dashboard** - `streamlit run dashboard_app.py`

---

**EA Hackathon 2025** | Innovation Meets Wellness
