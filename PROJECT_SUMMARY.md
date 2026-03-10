# EA Aura - Project Summary

## EA Hackathon 2025

---

## Executive Summary

EA Aura is an AI-powered wellness platform that combines health coaching, financial wellness tools, gamification, and analytics to support EA employees' holistic well-being.

### Innovation Highlights

- **Azure OpenAI Integration** - GPT-4 powered wellness coaching
- **Voice Interaction** - Speech recognition with customizable voices
- **Animated Coin System** - Gamified rewards with visual feedback
- **Real-time Analytics** - Streamlit dashboard with KPI tracking
- **Multi-Character AI** - Nova, Kai, Veda, Iris personalized coaches

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      EA AURA PLATFORM                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌────────────────┐   ┌────────────────┐   ┌────────────┐  │
│   │   index.html   │   │    app.py      │   │ dashboard  │  │
│   │   (Frontend)   │   │    (Flask)     │   │  _app.py   │  │
│   │                │   │                │   │ (Streamlit)│  │
│   │ • AI Chat      │   │ • REST API     │   │            │  │
│   │ • Voice        │   │ • OpenAI       │   │ • KPIs     │  │
│   │ • Calculators  │   │ • Sessions     │   │ • Charts   │  │
│   │ • Games        │   │                │   │ • Export   │  │
│   │ • Coin Jar     │   │                │   │            │  │
│   └───────┬────────┘   └───────┬────────┘   └─────┬──────┘  │
│           │                    │                   │         │
│           └────────────────────┼───────────────────┘         │
│                                │                             │
│                    ┌───────────┴───────────┐                 │
│                    │   config_openAI.py    │                 │
│                    │   (Azure OpenAI)      │                 │
│                    └───────────────────────┘                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Core Components

### 1. Wellness Hub (`index.html`)

**Features:**
| Tab | Functionality |
|-----|---------------|
| Wellness | Track steps, sleep, mood, focus; select AI coach |
| Wealth | Budget calculator, emergency fund planner |
| Games | Snake, Memory, Sudoku, Zen Garden (embedded) |
| Help | Medical insurance, FoodBook, fitness videos |

**Interactive Elements:**
- Animated coin jar with falling coins
- Voice controls (Male/Female/Other)
- Character selection with real images
- Quick action buttons

### 2. Flask Backend (`app.py`)

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Serve main app |
| `/api/chat` | POST | AI conversation |
| `/api/chat/clear` | POST | Reset session |
| `/api/wellness/tips` | GET | Get tips by category |
| `/api/health` | GET | Health check |

### 3. Streamlit Dashboard (`dashboard_app.py`)

| Tab | Visualizations |
|-----|----------------|
| Overview | DAU/MAU area charts, session distribution |
| User Metrics | Retention funnel, interaction histogram |
| Feedback | Satisfaction gauge, rating scatter |
| About | Documentation, metrics guide |

### 4. Data Generator (`Hackathon_Dashboard.py`)

Generates 30 days of realistic KPI data:
- Daily/Monthly Active Users
- Satisfaction & Ratings
- Voice Feature Adoption
- User Retention
- Session Metrics

---

## AI Wellness Coaches

| Coach | Focus | Style |
|-------|-------|-------|
| **Nova** | Habits & Goals | Energetic, motivational |
| **Veda** | Focus & Energy | Analytical, strategic |
| **Kai** | Calm & Breath | Peaceful, mindful |
| **Iris** | Rest & Recovery | Gentle, nurturing |

### 5 Wellness Pillars

1. **Physical** - Movement, nutrition, sleep
2. **Mental** - Stress management, mindfulness
3. **Productivity** - Focus, time management
4. **Social** - Connection, relationships
5. **Purpose** - Goals, growth, meaning

---

## Gamification

### Coin Rewards

| Action | Coins |
|--------|-------|
| Update wellness metric | 10 |
| Use budget calculator | 5 |
| Play wellness game | 20-50 |
| Complete breathing exercise | 5/cycle |

### Visual Effects

- Coins animate falling into jar
- Jar shakes on coin collection
- Golden glow effect
- Sound effect plays

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Frontend | HTML5, CSS3, JavaScript ES6+ |
| Voice | Web Speech API |
| Audio | Web Audio API |
| Backend | Python 3.9+, Flask, Flask-CORS |
| AI | Azure OpenAI (GPT-4o) |
| Dashboard | Streamlit, Plotly |
| Data | Pandas, NumPy, OpenPyXL |

---

## File Reference

| File | Purpose | Key Functions |
|------|---------|---------------|
| `index.html` | Main app | UI, voice, games |
| `app.py` | Backend | API endpoints |
| `config_openAI.py` | AI config | OpenAI client, prompts |
| `dashboard_app.py` | Analytics | KPI visualization |
| `Hackathon_Dashboard.py` | Data gen | Generate test data |
| `requirements.txt` | Dependencies | Python packages |

---

## Quick Demo

1. **Open** `index.html` in browser
2. **Try** Budget Calculator → See coins fall
3. **Select** different AI coaches
4. **Use Voice** → Click 🎤 to speak
5. **Play Games** → Embedded in Games tab
6. **View Dashboard** → `python -m streamlit run dashboard_app.py`

---

## Future Enhancements

- [ ] Team wellness leaderboards
- [ ] Wearable device integration
- [ ] Slack/Teams bot
- [ ] Mobile PWA
- [ ] ML-based predictions

---

**EA Hackathon 2025** | Innovation Meets Wellness
