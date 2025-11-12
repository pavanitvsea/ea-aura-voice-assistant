# EA Aura Python Games Collection

A comprehensive collection of wellness-focused Python games integrated with the EA Aura Enhanced Wellness Hub. These games are designed to promote cognitive health, stress relief, mindfulness, and overall well-being for EA employees.

## 🎮 Games Collection

### 1. Wellness Snake (wellness_snake.py)
**Focus Training & Stress Relief Game**

- **Objective**: Control a snake to collect wellness items while practicing breathing exercises
- **Benefits**: Improves focus, hand-eye coordination, stress relief through controlled breathing
- **Features**:
  - Color-coded breathing guide (inhale/exhale)
  - Focus mode with background blur
  - Wellness coins earned based on performance (25-75 coins)
  - High score tracking with statistics
  - Wellness benefits tracking (focus training, stress relief)

**Controls**:
- Arrow keys: Move snake
- Spacebar: Toggle focus mode
- Esc: Quit game

### 2. Memory Cards (memory_cards.py)
**Cognitive Enhancement Game**

- **Objective**: Find matching pairs of wellness-themed emoji cards
- **Benefits**: Enhances memory, concentration, cognitive flexibility
- **Features**:
  - 12 pairs of wellness-themed cards (24 total)
  - Move and time tracking
  - Best time records
  - Coin rewards based on efficiency (30-80 coins)
  - Neural pathway strengthening through memory exercises

**Controls**:
- Mouse click: Flip cards
- R: Restart game (when completed)
- Q: Quit

### 3. Sudoku Puzzle (sudoku_puzzle.py)
**Logical Thinking Game**

- **Objective**: Fill 9x9 grid with numbers 1-9 following Sudoku rules
- **Benefits**: Improves logical thinking, pattern recognition, mental focus
- **Features**:
  - Multiple difficulty levels (Easy, Medium, Hard)
  - Hint system (H key)
  - Mistake tracking
  - Best time records by difficulty
  - Coin rewards based on performance (20-70 coins)

**Controls**:
- Mouse click: Select cell
- Numbers 1-9: Place number
- H: Get hint
- Delete/Backspace: Clear cell
- R: New game (when completed)

### 4. Zen Garden (zen_garden.py)
**Mindfulness & Relaxation Game**

- **Objective**: Create beautiful patterns in a digital zen garden
- **Benefits**: Reduces stress, promotes mindfulness, brings inner peace
- **Features**:
  - Click and drag to rake sand patterns
  - Meditation mode with inspirational quotes
  - Pattern detection (lines and circles)
  - Session and lifetime statistics
  - Coin rewards based on time and engagement (40-100 coins)

**Controls**:
- Mouse drag: Rake patterns
- M: Toggle meditation mode
- C: Clear patterns
- R: Reset garden
- Q: Quit

### 5. Game Launcher (game_launcher.py)
**Central Gaming Hub**

- **Objective**: Access all wellness games from one interface
- **Benefits**: Easy game selection with progress tracking
- **Features**:
  - Visual game selection menu
  - Comprehensive statistics tracking
  - Coin data export for HTML integration
  - Wellness benefit tracking
  - Session history and achievements

**Controls**:
- Arrow keys: Navigate games
- Enter/Space: Launch selected game
- Mouse click: Select and launch games
- Q: Quit launcher

## 🛠️ Installation & Setup

### Prerequisites
1. **Python 3.8+**: Download from [python.org](https://python.org)
2. **pip**: Usually comes with Python installation

### Installation Steps

1. **Clone/Download** the EA Aura repository
2. **Navigate** to the games directory:
   ```bash
   cd "EA Hackathon 2025/games"
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or install pygame directly:
   ```bash
   pip install pygame
   ```

4. **Run games** individually or use the launcher:
   ```bash
   # Run individual games
   python wellness_snake.py
   python memory_cards.py
   python sudoku_puzzle.py
   python zen_garden.py
   
   # Or run the game launcher
   python game_launcher.py
   ```

## 🏆 Wellness Coin System

All games award wellness coins based on performance:

| Game | Coin Range | Factors |
|------|------------|---------|
| Wellness Snake | 25-75 | Score, focus mode usage, breathing exercises |
| Memory Cards | 30-80 | Moves efficiency, completion time |
| Sudoku | 20-70 | Difficulty level, mistakes, hints used |
| Zen Garden | 40-100 | Session time, meditation time, patterns created |

## 📊 Data Tracking & Integration

### Game Statistics
Each game tracks:
- Play time and session count
- Performance metrics (scores, completion times)
- Wellness benefits gained
- Coins earned
- Best achievements

### HTML Integration
Games can export coin data to `python_game_coins.json` for integration with the EA Aura web interface:

```json
{
    "coins_earned": 50,
    "timestamp": "2024-01-15T10:30:00",
    "source": "python_games"
}
```

### Wellness Benefits Tracked
- **Cognitive Enhancement**: Memory, attention, processing speed
- **Logical Thinking**: Problem-solving, pattern recognition
- **Focus Training**: Sustained attention, concentration
- **Mindfulness & Relaxation**: Stress reduction, inner peace
- **Hand-Eye Coordination**: Motor skills, reaction time

## 🎯 Wellness Framework Integration

These games are designed around the EA Coaching Pillars:

### Physical Health
- **Movement**: Hand-eye coordination, fine motor skills
- **Breathing**: Integrated breathing exercises in Snake game
- **Ergonomics**: Short, focused gaming sessions

### Mental Health
- **Stress Relief**: Zen garden meditation, focus training
- **Cognitive Health**: Memory and logic challenges
- **Mindfulness**: Meditation modes and breathing exercises

### Social Connection
- **Achievement Sharing**: Statistics and progress tracking
- **Wellness Community**: Integrated with EA Aura social features

### Purpose & Growth
- **Skill Development**: Cognitive abilities, focus, problem-solving
- **Goal Achievement**: Progressive difficulty, high scores
- **Personal Growth**: Mindfulness and stress management

## 🚀 Advanced Features

### Command Line Integration
Run specific games directly from HTML interface:
```bash
python game_launcher.py snake    # Launch Snake game
python game_launcher.py memory   # Launch Memory Cards
python game_launcher.py sudoku   # Launch Sudoku
python game_launcher.py zen      # Launch Zen Garden
```

### Configuration Files
Games save progress and settings in JSON files:
- `snake_high_score.json`: Snake game records
- `memory_best_time.json`: Memory cards best times
- `sudoku_best_times.json`: Sudoku records by difficulty
- `zen_garden_stats.json`: Zen garden session data
- `wellness_games_stats.json`: Overall gaming statistics

## 🔧 Troubleshooting

### Common Issues

1. **pygame not found**
   ```bash
   pip install pygame
   ```

2. **Permission errors**
   - Run as administrator (Windows)
   - Use `sudo` (Mac/Linux)

3. **Audio issues**
   - Check system audio settings
   - Some games use audio feedback for coins

4. **Display issues**
   - Ensure adequate screen resolution (minimum 800x600)
   - Update graphics drivers if needed

### Performance Tips
- Close other applications for smooth gameplay
- Use fullscreen mode for better immersion
- Take regular breaks between gaming sessions

## 📈 Future Enhancements

### Planned Features
- Multiplayer wellness challenges
- Advanced AI coaching integration  
- Biometric data integration (heart rate, stress levels)
- Virtual reality zen garden
- Team-based wellness competitions
- Advanced analytics and insights

### Integration Roadmap
- Real-time HTML-Python communication
- Cloud-based progress synchronization
- Mobile companion apps
- Wearable device integration
- AI-powered personalized recommendations

## 💡 Development Notes

### Architecture
- **Modular design**: Each game is self-contained
- **Common interfaces**: Standardized coin and statistics systems
- **Extensible framework**: Easy to add new games
- **Cross-platform**: Works on Windows, Mac, Linux

### Code Structure
```
games/
├── wellness_snake.py      # Snake game with breathing
├── memory_cards.py        # Memory matching game  
├── sudoku_puzzle.py       # Logic puzzle game
├── zen_garden.py          # Mindfulness sandbox
├── game_launcher.py       # Central hub
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
└── *.json                # Save files and statistics
```

### Wellness Psychology
Games are designed based on established wellness principles:
- **Flow State**: Optimal challenge-skill balance
- **Mindfulness**: Present-moment awareness
- **Progressive Enhancement**: Gradual skill building
- **Positive Reinforcement**: Coin rewards and achievements
- **Stress Reduction**: Calming visuals and audio

---

*Created for EA Hackathon 2025 - Prioritizing employee wellness through innovative gaming experiences.* 🎮✨