import pygame
import math
import random
import sys
import json
from datetime import datetime, timedelta

# Initialize Pygame
pygame.init()

# Game settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SAND_COLOR = (245, 245, 220)  # Beige sand
ROCK_COLOR = (105, 105, 105)  # Dark gray
RAKE_COLOR = (139, 69, 19)    # Brown
PATTERN_COLOR = (210, 210, 190)  # Lighter sand for patterns

class ZenRock:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(x - size//2, y - size//2, size, size)
        
    def draw(self, screen):
        pygame.draw.circle(screen, ROCK_COLOR, (int(self.x), int(self.y)), self.size)
        # Add highlight for 3D effect
        highlight_color = (130, 130, 130)
        pygame.draw.circle(screen, highlight_color, 
                          (int(self.x - self.size//4), int(self.y - self.size//4)), 
                          self.size//3)

class SandPattern:
    def __init__(self):
        self.lines = []
        self.circles = []
        self.fade_timer = 0
        
    def add_line(self, start_pos, end_pos):
        self.lines.append({
            'start': start_pos,
            'end': end_pos,
            'created': datetime.now()
        })
        
    def add_circle(self, center, radius):
        self.circles.append({
            'center': center,
            'radius': radius,
            'created': datetime.now()
        })
        
    def update(self):
        # Fade patterns over time (optional)
        current_time = datetime.now()
        self.lines = [line for line in self.lines 
                     if (current_time - line['created']).seconds < 300]  # 5 minutes
        self.circles = [circle for circle in self.circles 
                       if (current_time - circle['created']).seconds < 300]
                       
    def draw(self, screen):
        # Draw lines
        for line in self.lines:
            pygame.draw.line(screen, PATTERN_COLOR, line['start'], line['end'], 2)
            
        # Draw circles
        for circle in self.circles:
            pygame.draw.circle(screen, PATTERN_COLOR, circle['center'], circle['radius'], 2)
            # Add inner circles for ripple effect
            if circle['radius'] > 20:
                pygame.draw.circle(screen, PATTERN_COLOR, circle['center'], circle['radius']//2, 1)
            if circle['radius'] > 40:
                pygame.draw.circle(screen, PATTERN_COLOR, circle['center'], circle['radius']//3, 1)

class WellnessZenGarden:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Zen Garden - Mindfulness & Relaxation")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Garden elements
        self.rocks = []
        self.sand_pattern = SandPattern()
        
        # Rake (cursor)
        self.rake_pos = (0, 0)
        self.raking = False
        self.last_rake_pos = None
        
        # Game state
        self.session_start = datetime.now()
        self.total_strokes = 0
        self.patterns_created = 0
        self.meditation_time = 0
        self.coins_earned = 0
        
        # Meditation tracking
        self.is_meditating = False
        self.meditation_start = None
        self.total_meditation_time = 0
        
        # Wellness quotes for meditation
        self.meditation_quotes = [
            "Breathe in peace, breathe out stress",
            "Find stillness in the motion of raking",
            "Each stroke brings inner calm",
            "Let your mind flow like sand",
            "Embrace the present moment",
            "Zen is found in simple actions",
            "Create beauty through mindful movement",
            "Peace comes from within"
        ]
        self.current_quote = random.choice(self.meditation_quotes)
        
        self.initialize_garden()
        self.wellness_stats = self.load_wellness_stats()
        
    def initialize_garden(self):
        # Place some rocks randomly
        for _ in range(random.randint(3, 6)):
            x = random.randint(100, WINDOW_WIDTH - 100)
            y = random.randint(150, WINDOW_HEIGHT - 100)
            size = random.randint(25, 50)
            # Make sure rocks don't overlap too much
            valid_position = True
            for rock in self.rocks:
                if math.sqrt((x - rock.x)**2 + (y - rock.y)**2) < (size + rock.size):
                    valid_position = False
                    break
            if valid_position:
                self.rocks.append(ZenRock(x, y, size))
                
    def load_wellness_stats(self):
        try:
            with open('zen_garden_stats.json', 'r') as f:
                return json.load(f)
        except:
            return {
                'total_sessions': 0,
                'total_meditation_time': 0,
                'total_strokes': 0,
                'longest_session': 0,
                'patterns_created': 0
            }
            
    def save_wellness_stats(self):
        session_time = (datetime.now() - self.session_start).seconds
        self.wellness_stats['total_sessions'] += 1
        self.wellness_stats['total_meditation_time'] += self.total_meditation_time
        self.wellness_stats['total_strokes'] += self.total_strokes
        self.wellness_stats['patterns_created'] += self.patterns_created
        
        if session_time > self.wellness_stats['longest_session']:
            self.wellness_stats['longest_session'] = session_time
            
        with open('zen_garden_stats.json', 'w') as f:
            json.dump(self.wellness_stats, f)
            
    def calculate_coins(self):
        # Coins based on meditation time and mindful actions
        session_time = (datetime.now() - self.session_start).seconds
        base_coins = min(50, session_time // 10)  # 1 coin per 10 seconds, max 50
        meditation_bonus = min(30, self.total_meditation_time // 5)  # Bonus for meditation
        pattern_bonus = self.patterns_created * 5
        stroke_bonus = min(20, self.total_strokes // 10)
        
        return base_coins + meditation_bonus + pattern_bonus + stroke_bonus
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    # Clear patterns
                    self.sand_pattern = SandPattern()
                elif event.key == pygame.K_m:
                    # Toggle meditation mode
                    self.toggle_meditation()
                elif event.key == pygame.K_r:
                    # Reset garden
                    self.reset_garden()
                elif event.key == pygame.K_q:
                    return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.raking = True
                    self.last_rake_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.raking = False
                    self.last_rake_pos = None
            elif event.type == pygame.MOUSEMOTION:
                self.rake_pos = event.pos
                if self.raking and self.last_rake_pos:
                    self.create_rake_pattern()
                    
        return True
        
    def create_rake_pattern(self):
        if self.last_rake_pos:
            # Create line pattern
            self.sand_pattern.add_line(self.last_rake_pos, self.rake_pos)
            self.total_strokes += 1
            
            # Check if we're making circular motions for circle pattern
            if len(self.sand_pattern.lines) > 10:
                recent_lines = self.sand_pattern.lines[-10:]
                if self.is_circular_motion(recent_lines):
                    center = self.calculate_center(recent_lines)
                    radius = self.calculate_average_radius(recent_lines, center)
                    self.sand_pattern.add_circle(center, int(radius))
                    self.patterns_created += 1
                    
        self.last_rake_pos = self.rake_pos
        
    def is_circular_motion(self, lines):
        # Simple heuristic to detect circular motion
        if len(lines) < 5:
            return False
            
        # Check if the lines form roughly a circular pattern
        points = [line['start'] for line in lines] + [lines[-1]['end']]
        
        # Calculate if points roughly form a circle
        center_x = sum(p[0] for p in points) / len(points)
        center_y = sum(p[1] for p in points) / len(points)
        center = (center_x, center_y)
        
        distances = [math.sqrt((p[0] - center[0])**2 + (p[1] - center[1])**2) for p in points]
        avg_distance = sum(distances) / len(distances)
        
        # Check if distances are relatively consistent (circular)
        variance = sum((d - avg_distance)**2 for d in distances) / len(distances)
        return variance < (avg_distance * 0.3)**2  # Low variance indicates circle
        
    def calculate_center(self, lines):
        points = [line['start'] for line in lines] + [lines[-1]['end']]
        center_x = sum(p[0] for p in points) / len(points)
        center_y = sum(p[1] for p in points) / len(points)
        return (int(center_x), int(center_y))
        
    def calculate_average_radius(self, lines, center):
        points = [line['start'] for line in lines] + [lines[-1]['end']]
        distances = [math.sqrt((p[0] - center[0])**2 + (p[1] - center[1])**2) for p in points]
        return sum(distances) / len(distances)
        
    def toggle_meditation(self):
        if self.is_meditating:
            # Stop meditation
            if self.meditation_start:
                self.total_meditation_time += (datetime.now() - self.meditation_start).seconds
            self.is_meditating = False
            self.meditation_start = None
        else:
            # Start meditation
            self.is_meditating = True
            self.meditation_start = datetime.now()
            self.current_quote = random.choice(self.meditation_quotes)
            
    def reset_garden(self):
        self.rocks.clear()
        self.sand_pattern = SandPattern()
        self.initialize_garden()
        self.patterns_created = 0
        
    def update_game(self):
        self.sand_pattern.update()
        
        # Update meditation time
        if self.is_meditating and self.meditation_start:
            current_meditation = (datetime.now() - self.meditation_start).seconds
            self.meditation_time = self.total_meditation_time + current_meditation
        else:
            self.meditation_time = self.total_meditation_time
            
        # Calculate current coins
        self.coins_earned = self.calculate_coins()
        
    def draw_game(self):
        # Background (sand)
        self.screen.fill(SAND_COLOR)
        
        # Draw sand patterns
        self.sand_pattern.draw(self.screen)
        
        # Draw rocks
        for rock in self.rocks:
            rock.draw(self.screen)
            
        # Draw rake (cursor)
        rake_color = RAKE_COLOR if self.raking else (100, 50, 0)
        pygame.draw.circle(self.screen, rake_color, self.rake_pos, 8)
        if self.raking:
            # Draw rake lines for visual feedback
            pygame.draw.circle(self.screen, rake_color, self.rake_pos, 12, 2)
            
        # UI Elements
        self.draw_ui()
        
    def draw_ui(self):
        # Title
        title = self.font.render("🧘 Zen Garden - Mindfulness & Relaxation", True, (100, 50, 0))
        self.screen.blit(title, (20, 20))
        
        # Session stats
        session_time = (datetime.now() - self.session_start).seconds
        time_text = self.small_font.render(f"Session: {session_time // 60}:{session_time % 60:02d}", True, (100, 50, 0))
        meditation_text = self.small_font.render(f"Meditation: {self.meditation_time // 60}:{self.meditation_time % 60:02d}", True, (100, 50, 0))
        strokes_text = self.small_font.render(f"Strokes: {self.total_strokes}", True, (100, 50, 0))
        patterns_text = self.small_font.render(f"Patterns: {self.patterns_created}", True, (100, 50, 0))
        coins_text = self.small_font.render(f"Wellness Coins: {self.coins_earned}", True, (100, 50, 0))
        
        self.screen.blit(time_text, (20, 60))
        self.screen.blit(meditation_text, (150, 60))
        self.screen.blit(strokes_text, (320, 60))
        self.screen.blit(patterns_text, (420, 60))
        self.screen.blit(coins_text, (520, 60))
        
        # Meditation mode indicator
        if self.is_meditating:
            med_bg = pygame.Surface((WINDOW_WIDTH, 100))
            med_bg.set_alpha(180)
            med_bg.fill((255, 255, 255))
            self.screen.blit(med_bg, (0, WINDOW_HEIGHT - 100))
            
            med_text = self.font.render("🧘 Meditation Mode Active", True, (50, 100, 50))
            quote_text = self.small_font.render(f'"{self.current_quote}"', True, (80, 80, 80))
            
            med_rect = med_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 70))
            quote_rect = quote_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 40))
            
            self.screen.blit(med_text, med_rect)
            self.screen.blit(quote_text, quote_rect)
            
        # Instructions
        if not self.is_meditating:
            instructions = [
                "Click and drag to rake patterns in the sand",
                "Press M to enter meditation mode | C to clear | R to reset | Q to quit"
            ]
            
            for i, instruction in enumerate(instructions):
                inst_text = self.small_font.render(instruction, True, (120, 80, 40))
                self.screen.blit(inst_text, (20, WINDOW_HEIGHT - 50 + i * 25))
                
        # Lifetime stats (top right)
        if self.wellness_stats['total_sessions'] > 0:
            stats_text = [
                f"Sessions: {self.wellness_stats['total_sessions']}",
                f"Total meditation: {self.wellness_stats['total_meditation_time'] // 60}m",
                f"Longest session: {self.wellness_stats['longest_session'] // 60}m"
            ]
            
            for i, stat in enumerate(stats_text):
                stat_surface = self.small_font.render(stat, True, (80, 80, 80))
                self.screen.blit(stat_surface, (WINDOW_WIDTH - 200, 80 + i * 20))
        
        # Wellness tip
        tip_text = self.small_font.render("💡 Zen gardening reduces stress, improves focus, and promotes mindfulness!", True, (50, 100, 50))
        self.screen.blit(tip_text, (20, WINDOW_HEIGHT - 25))
        
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update_game()
            self.draw_game()
            pygame.display.flip()
            self.clock.tick(60)
            
        # Save stats before closing
        self.save_wellness_stats()
        pygame.quit()
        
        # Return wellness data
        session_time = (datetime.now() - self.session_start).seconds
        return {
            'game': 'Zen Garden',
            'session_time': session_time,
            'meditation_time': self.total_meditation_time,
            'strokes': self.total_strokes,
            'patterns_created': self.patterns_created,
            'coins_earned': self.coins_earned,
            'mindfulness_benefit': True
        }

if __name__ == "__main__":
    print("🧘 Zen Garden - Mindfulness & Relaxation")
    print("Create beautiful patterns in the sand to achieve inner peace!")
    print("This meditative game reduces stress and promotes mindfulness!")
    
    game = WellnessZenGarden()
    result = game.run()
    
    print(f"\n🎯 Wellness Results:")
    print(f"Session Time: {result['session_time'] // 60}:{result['session_time'] % 60:02d}")
    print(f"Meditation Time: {result['meditation_time'] // 60}:{result['meditation_time'] % 60:02d}")
    print(f"Patterns Created: {result['patterns_created']}")
    print(f"Total Strokes: {result['strokes']}")
    print(f"Coins Earned: {result['coins_earned']}")
    print(f"Beautiful mindfulness session! Your inner peace is growing! 🧘✨")