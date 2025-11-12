#!/usr/bin/env python3
"""
EA Aura Wellness Games Launcher
Integrates all Python wellness games with the HTML interface
"""

import pygame
import sys
import json
import subprocess
import os
from datetime import datetime
import importlib.util

# Initialize Pygame for the launcher
pygame.init()

# Launcher settings
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 200)
GREEN = (0, 200, 0)
GOLD = (255, 215, 0)
LIGHT_BLUE = (173, 216, 230)

class GameLauncher:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("EA Aura Wellness Games Hub")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.ui_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Available games
        self.games = [
            {
                'name': 'Wellness Snake',
                'file': 'wellness_snake.py',
                'description': 'Focus training game with breathing exercises',
                'benefits': 'Improves focus, hand-eye coordination, stress relief',
                'icon': '🐍',
                'coins': '25-75'
            },
            {
                'name': 'Memory Cards',
                'file': 'memory_cards.py',
                'description': 'Cognitive wellness memory matching game',
                'benefits': 'Enhances memory, concentration, cognitive flexibility',
                'icon': '🧠',
                'coins': '30-80'
            },
            {
                'name': 'Sudoku Puzzle',
                'file': 'sudoku_puzzle.py',
                'description': 'Logical thinking and problem-solving challenge',
                'benefits': 'Improves logic, pattern recognition, mental focus',
                'icon': '🧩',
                'coins': '20-70'
            },
            {
                'name': 'Zen Garden',
                'file': 'zen_garden.py',
                'description': 'Mindfulness and relaxation through digital raking',
                'benefits': 'Reduces stress, promotes mindfulness, inner peace',
                'icon': '🧘',
                'coins': '40-100'
            }
        ]
        
        self.selected_game = 0
        self.total_sessions = self.load_session_stats()
        
    def load_session_stats(self):
        try:
            with open('wellness_games_stats.json', 'r') as f:
                return json.load(f)
        except:
            return {
                'total_games_played': 0,
                'total_coins_earned': 0,
                'total_play_time': 0,
                'games_completed': 0,
                'wellness_benefits_gained': []
            }
            
    def save_session_stats(self, game_result):
        self.total_sessions['total_games_played'] += 1
        if 'coins_earned' in game_result:
            self.total_sessions['total_coins_earned'] += game_result['coins_earned']
        if 'time' in game_result:
            self.total_sessions['total_play_time'] += game_result['time']
        elif 'session_time' in game_result:
            self.total_sessions['total_play_time'] += game_result['session_time']
            
        if game_result.get('completed', False):
            self.total_sessions['games_completed'] += 1
            
        # Add wellness benefits
        benefits = []
        if game_result.get('cognitive_benefit'):
            benefits.append('Cognitive Enhancement')
        if game_result.get('logical_benefit'):
            benefits.append('Logical Thinking')
        if game_result.get('mindfulness_benefit'):
            benefits.append('Mindfulness & Relaxation')
        if game_result.get('focus_benefit'):
            benefits.append('Focus Training')
            
        for benefit in benefits:
            if benefit not in self.total_sessions['wellness_benefits_gained']:
                self.total_sessions['wellness_benefits_gained'].append(benefit)
                
        with open('wellness_games_stats.json', 'w') as f:
            json.dump(self.total_sessions, f, indent=2)
            
    def export_coins_to_html(self, coins_earned):
        """Export coins to JSON file that HTML can read"""
        coin_data = {
            'coins_earned': coins_earned,
            'timestamp': datetime.now().isoformat(),
            'source': 'python_games'
        }
        
        with open('python_game_coins.json', 'w') as f:
            json.dump(coin_data, f)
            
    def launch_game(self, game_index):
        """Launch the selected game"""
        if 0 <= game_index < len(self.games):
            game = self.games[game_index]
            game_file = game['file']
            
            # Check if game file exists
            if not os.path.exists(game_file):
                print(f"Game file {game_file} not found!")
                return None
                
            try:
                # Import and run the game module
                spec = importlib.util.spec_from_file_location("game_module", game_file)
                game_module = importlib.util.module_from_spec(spec)
                
                # Hide launcher window
                pygame.display.iconify()
                
                # Execute the game
                spec.loader.exec_module(game_module)
                
                # Game should return result data
                # For now, we'll create a simple result
                result = {
                    'game': game['name'],
                    'completed': True,
                    'coins_earned': 50,  # Default coins
                    'time': 180  # Default 3 minutes
                }
                
                return result
                
            except Exception as e:
                print(f"Error launching game: {e}")
                return None
                
        return None
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_game = (self.selected_game - 1) % len(self.games)
                elif event.key == pygame.K_DOWN:
                    self.selected_game = (self.selected_game + 1) % len(self.games)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    result = self.launch_game(self.selected_game)
                    if result:
                        self.save_session_stats(result)
                        self.export_coins_to_html(result.get('coins_earned', 0))
                elif event.key == pygame.K_q:
                    return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    # Check if clicking on a game
                    mouse_y = event.pos[1]
                    game_start_y = 150
                    game_height = 120
                    
                    for i in range(len(self.games)):
                        game_y = game_start_y + i * game_height
                        if game_y <= mouse_y <= game_y + game_height - 10:
                            self.selected_game = i
                            result = self.launch_game(i)
                            if result:
                                self.save_session_stats(result)
                                self.export_coins_to_html(result.get('coins_earned', 0))
                            break
                            
        return True
        
    def draw_launcher(self):
        # Background
        self.screen.fill(WHITE)
        
        # Title
        title = self.font.render("🎮 EA Aura Wellness Games Hub", True, BLUE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 40))
        self.screen.blit(title, title_rect)
        
        # Subtitle
        subtitle = self.ui_font.render("Choose your wellness gaming experience", True, BLACK)
        subtitle_rect = subtitle.get_rect(center=(WINDOW_WIDTH // 2, 80))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Game list
        game_start_y = 150
        game_height = 120
        
        for i, game in enumerate(self.games):
            y_pos = game_start_y + i * game_height
            
            # Game card background
            card_rect = pygame.Rect(50, y_pos, WINDOW_WIDTH - 100, game_height - 10)
            
            if i == self.selected_game:
                pygame.draw.rect(self.screen, LIGHT_BLUE, card_rect)
                pygame.draw.rect(self.screen, BLUE, card_rect, 3)
            else:
                pygame.draw.rect(self.screen, (245, 245, 245), card_rect)
                pygame.draw.rect(self.screen, BLACK, card_rect, 1)
                
            # Game info
            icon_text = self.font.render(game['icon'], True, BLACK)
            name_text = self.ui_font.render(game['name'], True, BLACK)
            desc_text = self.small_font.render(game['description'], True, BLACK)
            benefits_text = self.small_font.render(f"Benefits: {game['benefits']}", True, GREEN)
            coins_text = self.small_font.render(f"Coins: {game['coins']}", True, GOLD)
            
            # Position text
            self.screen.blit(icon_text, (70, y_pos + 10))
            self.screen.blit(name_text, (120, y_pos + 10))
            self.screen.blit(desc_text, (120, y_pos + 40))
            self.screen.blit(benefits_text, (120, y_pos + 65))
            self.screen.blit(coins_text, (120, y_pos + 85))
            
        # Stats panel
        stats_y = WINDOW_HEIGHT - 120
        stats_rect = pygame.Rect(50, stats_y, WINDOW_WIDTH - 100, 100)
        pygame.draw.rect(self.screen, (250, 250, 250), stats_rect)
        pygame.draw.rect(self.screen, BLACK, stats_rect, 2)
        
        # Stats title
        stats_title = self.ui_font.render("🏆 Your Wellness Journey", True, BLUE)
        self.screen.blit(stats_title, (70, stats_y + 10))
        
        # Stats data
        stats_data = [
            f"Games Played: {self.total_sessions['total_games_played']}",
            f"Total Coins: {self.total_sessions['total_coins_earned']}",
            f"Play Time: {self.total_sessions['total_play_time'] // 60}m {self.total_sessions['total_play_time'] % 60}s",
            f"Completed: {self.total_sessions['games_completed']}"
        ]
        
        for i, stat in enumerate(stats_data):
            stat_text = self.small_font.render(stat, True, BLACK)
            x_pos = 70 + (i % 2) * 200
            y_pos = stats_y + 40 + (i // 2) * 25
            self.screen.blit(stat_text, (x_pos, y_pos))
            
        # Instructions
        instructions = "Use ↑↓ arrow keys or click to select • Enter/Space to launch • Q to quit"
        inst_text = self.small_font.render(instructions, True, BLACK)
        inst_rect = inst_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 15))
        self.screen.blit(inst_text, inst_rect)
        
        pygame.display.flip()
        
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.draw_launcher()
            self.clock.tick(60)
            
        pygame.quit()
        return self.total_sessions

def run_specific_game(game_name):
    """Run a specific game directly (for HTML integration)"""
    games_map = {
        'snake': 'wellness_snake.py',
        'memory': 'memory_cards.py',
        'sudoku': 'sudoku_puzzle.py',
        'zen': 'zen_garden.py'
    }
    
    if game_name.lower() in games_map:
        game_file = games_map[game_name.lower()]
        if os.path.exists(game_file):
            try:
                # Run the game as a subprocess
                result = subprocess.run([sys.executable, game_file], 
                                      capture_output=True, text=True)
                print(f"Game output: {result.stdout}")
                if result.stderr:
                    print(f"Game errors: {result.stderr}")
                return True
            except Exception as e:
                print(f"Error running game: {e}")
                return False
    return False

if __name__ == "__main__":
    print("🎮 EA Aura Wellness Games Hub")
    print("Launching the wellness gaming experience...")
    
    # Check if we should run a specific game (for HTML integration)
    if len(sys.argv) > 1:
        game_name = sys.argv[1]
        print(f"Running specific game: {game_name}")
        success = run_specific_game(game_name)
        if success:
            print(f"Game {game_name} completed successfully!")
        else:
            print(f"Failed to run game {game_name}")
    else:
        # Run the launcher
        launcher = GameLauncher()
        final_stats = launcher.run()
        
        print(f"\n🎯 Final Wellness Gaming Stats:")
        print(f"Total Games Played: {final_stats['total_games_played']}")
        print(f"Total Coins Earned: {final_stats['total_coins_earned']}")
        print(f"Total Play Time: {final_stats['total_play_time'] // 60}m {final_stats['total_play_time'] % 60}s")
        print(f"Games Completed: {final_stats['games_completed']}")
        
        if final_stats['wellness_benefits_gained']:
            print(f"Wellness Benefits: {', '.join(final_stats['wellness_benefits_gained'])}")
            
        print("Thank you for prioritizing your wellness through gaming! 🎮✨")