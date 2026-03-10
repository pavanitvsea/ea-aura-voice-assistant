# EA Aura - AI Wellness Hub

<div align="center">

![EA Aura](Aura_Logo.png)

**AI-Powered Wellness Platform for EA Employees**

[![GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-blue)](https://pavanitvsea.github.io/ea-aura-voice-assistant/)
[![Python](https://img.shields.io/badge/Python-3.9+-green)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)](https://streamlit.io)

</div>

---

## Overview

EA Aura is a comprehensive wellness platform combining AI-powered health and wealth coaching, voice interaction, gamification, and analytics. Built for EA Hackathon 2025.

### Key Features

| Feature | Description |
|---------|-------------|
| 🤖 **AI Assistant** | Health & wealth advice powered by Azure OpenAI (with smart fallback) |
| 🎙️ **Voice Control** | Speech recognition + Text-to-speech (Male/Female/Other voices) |
| 🪙 **Coin System** | Animated coin jar with falling coins effect |
| 🧮 **Financial Tools** | Budget calculator (50/30/20) & Emergency fund planner |
| 🎮 **Wellness Games** | Snake, Memory Cards, Sudoku, Zen Garden |
| 📊 **KPI Dashboard** | Interactive Streamlit analytics dashboard |
| 🎭 **AI Characters** | Nova, Veda, Kai, Iris - personalized wellness coaches |

---

## Live Demo

**GitHub Pages:** [https://pavanitvsea.github.io/ea-aura-voice-assistant/](https://pavanitvsea.github.io/ea-aura-voice-assistant/)

The static version works directly in your browser with smart AI fallback responses.

---

## Quick Start

### Option 1: Static Site (No Setup Required)
```bash
# Just open in browser
open index.html
```

### Option 2: Streamlit Dashboard
```bash
# Install dependencies
pip install -r requirements.txt

# Generate dashboard data (REQUIRED!)
python Hackathon_Dashboard.py

# Run dashboard
python -m streamlit run dashboard_app.py
```
Access at: http://localhost:8501

### Option 3: Full Stack (Flask + Azure OpenAI)
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables (optional - uses fallback if not set)
# Create .env file with:
# AZURE_OPENAI_ENDPOINT=your-endpoint
# AZURE_OPENAI_API_KEY=your-key
# AZURE_OPENAI_DEPLOYMENT=gpt-4o

# Generate data & run
python Hackathon_Dashboard.py
python app.py
```
Access at: http://localhost:5000

---

## Project Structure

```
EA Hackathon 2025/
├── index.html                  # Main wellness app (all features)
├── app.py                      # Flask backend server
├── config_openAI.py            # Azure OpenAI configuration
├── dashboard_app.py            # Streamlit KPI dashboard
├── Hackathon_Dashboard.py      # Data generator script
├── requirements.txt            # Python dependencies
│
├── games/                      # Wellness game collection
│   ├── index.html              # Game hub
│   ├── wellness_snake.html     # Snake game
│   ├── memory_cards.html       # Memory matching
│   ├── sudoku_puzzle.html      # Sudoku puzzle
│   └── zen_garden.html         # Mindfulness activity
│
├── Aura/                       # Standalone version (no backend)
│   ├── aura_wellness_hub.html
│   └── games/
│
├── Character Images
│   ├── nova_orange.png         # Nova - Habit Tracker
│   ├── veda_red.png            # Veda - Focus & Energy
│   ├── kai_blue.png            # Kai - Calm & Breath
│   └── iris_green.png          # Iris - Relax & Recover
│
├── Asset Images
│   ├── Jar.png                 # Coin jar
│   ├── Aura_Jar_and_Coin.png   # Jar with coins
│   ├── coin.png                # Coin image
│   └── Aura_Logo.png           # Logo
│
└── Documentation
    ├── README.md               # This file
    ├── PROJECT_SUMMARY.md      # Technical summary
    └── AI_Coaching_Pillars_Guide.md
```

---

## Features in Detail

### AI Wellness Coaches

| Character | Image | Focus Area | Personality |
|-----------|-------|------------|-------------|
| **Nova** | ![Nova](nova_orange.png) | Habit Tracking | Energetic, motivational |
| **Veda** | ![Veda](veda_red.png) | Focus & Energy | Analytical, strategic |
| **Kai** | ![Kai](kai_blue.png) | Calm & Breath | Peaceful, mindful |
| **Iris** | ![Iris](iris_green.png) | Relax & Recover | Gentle, nurturing |

### Voice Controls

- **👩 Female Voice** - Higher pitch, default
- **👨 Male Voice** - Lower pitch
- **🤖 Other Voice** - Robot-like
- **🎤 Speech Input** - Click mic to speak

### Financial Tools

| Tool | Description |
|------|-------------|
| **Budget Calculator** | Enter income → Get 50/30/20 split (Needs/Wants/Savings) |
| **Emergency Fund** | Calculate 3/6/12 month savings goal |

### Wellness Games

| Game | Benefits | Coins |
|------|----------|-------|
| 🐍 Snake | Focus, coordination | 50 |
| 🧠 Memory | Cognitive training | 30 |
| 🔢 Sudoku | Logic, problem-solving | 40 |
| 🌸 Zen Garden | Mindfulness, relaxation | 25 |

### Coin System

- Animated coins fall into jar when earned
- Jar shakes and glows on coin collection
- Sound effect plays on earning
- Track progress with visual feedback

---

## Streamlit Dashboard

The KPI dashboard provides analytics on:

- **Daily/Monthly Active Users** - Growth trends
- **Satisfaction Rate** - User happiness metrics
- **Voice Adoption** - Voice feature usage
- **User Retention** - Day 0 to Day 30 funnel
- **Average Rating** - Star ratings over time

### Dashboard Tabs

| Tab | Content |
|-----|---------|
| 📈 Overview | DAU/MAU trends, session activity |
| 👥 User Metrics | Retention funnel, interactions |
| 💬 Feedback | Satisfaction gauge, ratings |
| 📚 About | Documentation |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | HTML5, CSS3, JavaScript ES6+ |
| **Voice** | Web Speech API (Recognition + Synthesis) |
| **Audio** | Web Audio API (coin sounds) |
| **Backend** | Python 3.9+, Flask |
| **AI** | Azure OpenAI (GPT-4o) |
| **Dashboard** | Streamlit, Plotly |
| **Data** | Pandas, NumPy, OpenPyXL |

---

## Browser Compatibility

| Feature | Chrome | Edge | Firefox | Safari |
|---------|--------|------|---------|--------|
| Wellness Hub | ✅ | ✅ | ✅ | ✅ |
| Voice Recognition | ✅ | ✅ | ⚠️ | ⚠️ |
| Voice Synthesis | ✅ | ✅ | ✅ | ✅ |
| Games | ✅ | ✅ | ✅ | ✅ |
| Animations | ✅ | ✅ | ✅ | ✅ |

---

## Environment Variables

Create a `.env` file for Azure OpenAI (optional):

```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=gpt-4o
```

If not configured, the app uses intelligent local fallback responses.

---

## API Endpoints (Flask)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main wellness app |
| `/api/chat` | POST | AI conversation |
| `/api/chat/clear` | POST | Clear chat history |
| `/api/wellness/tips` | GET | Get wellness tips |
| `/api/health` | GET | Health check |

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## License

This project was created for EA Hackathon 2025.

---

<div align="center">

**Built with ❤️ for EA Employee Wellness**

*EA Hackathon 2025*

</div>
