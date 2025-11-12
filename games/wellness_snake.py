import pygame
import random
import sys
import json
import webbrowser
from datetime import datetime

# Initialize Pygame
pygame.init()

# Game settings
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
CELL_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GREEN = (0, 128, 0)

class WellnessSnake:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Wellness Snake - Focus Training Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Game state
        self.reset_game()
        self.high_score = self.load_high_score()
        self.coins_earned = 0
        self.start_time = datetime.now()
        
    def reset_game(self):
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.food = self.place_food()
        self.score = 0
        self.game_over = False
        self.paused = False
        
    def place_food(self):
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake:
                return food
                
    def load_high_score(self):
        try:
            with open('snake_high_score.json', 'r') as f:
                data = json.load(f)
                return data.get('high_score', 0)
        except:
            return 0
            
    def save_high_score(self):
        data = {'high_score': self.high_score}
        with open('snake_high_score.json', 'w') as f:
            json.dump(data, f)
            
    def calculate_coins(self):
        # Wellness coin calculation: score + time bonus
        time_played = (datetime.now() - self.start_time).seconds
        time_bonus = min(time_played // 30, 10)  # Max 10 coins for time
        return self.score + time_bonus
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
                    self.start_time = datetime.now()
                elif event.key == pygame.K_q:
                    return False
                elif not self.paused and not self.game_over:
                    if event.key == pygame.K_UP and self.direction != (0, 1):
                        self.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                        self.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                        self.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                        self.direction = (1, 0)
        return True
        
    def update_game(self):
        if self.paused or self.game_over:
            return
            
        # Move snake
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        
        # Check collisions
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or 
            new_head in self.snake):
            self.game_over = True
            self.coins_earned = self.calculate_coins()
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            return
            
        self.snake.insert(0, new_head)
        
        # Check food
        if new_head == self.food:
            self.score += 1
            self.food = self.place_food()
        else:
            self.snake.pop()
            
    def draw_game(self):
        self.screen.fill(BLACK)
        
        # Draw grid
        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, (40, 40, 40), (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, (40, 40, 40), (0, y), (WINDOW_WIDTH, y))
        
        # Draw snake
        for i, segment in enumerate(self.snake):
            color = DARK_GREEN if i == 0 else GREEN
            rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, WHITE, rect, 1)
            
        # Draw food
        food_rect = pygame.Rect(self.food[0] * CELL_SIZE, self.food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, RED, food_rect)
        
        # Draw UI
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(high_score_text, (10, 50))
        
        # Game time for wellness tracking
        time_played = (datetime.now() - self.start_time).seconds
        time_text = self.small_font.render(f"Focus Time: {time_played}s", True, WHITE)
        self.screen.blit(time_text, (10, 90))
        
        if self.paused:
            pause_text = self.font.render("PAUSED - Press SPACE to continue", True, WHITE)
            text_rect = pause_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
            self.screen.blit(pause_text, text_rect)
            
        if self.game_over:
            game_over_text = self.font.render("GAME OVER!", True, RED)
            coins_text = self.font.render(f"Wellness Coins Earned: {self.coins_earned}", True, WHITE)
            restart_text = self.small_font.render("Press R to restart, Q to quit", True, WHITE)
            
            self.screen.blit(game_over_text, (WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 - 60))
            self.screen.blit(coins_text, (WINDOW_WIDTH//2 - 120, WINDOW_HEIGHT//2 - 20))
            self.screen.blit(restart_text, (WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 20))
            
        # Wellness tips
        tip_text = self.small_font.render("🧠 Focus Training: Improve reaction time and concentration!", True, BLUE)
        self.screen.blit(tip_text, (10, WINDOW_HEIGHT - 30))
        
        pygame.display.flip()
        
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update_game()
            self.draw_game()
            self.clock.tick(8)  # Moderate speed for focus training
            
        pygame.quit()
        
        # Return wellness data for integration
        return {
            'game': 'Snake',
            'score': self.score,
            'high_score': self.high_score,
            'coins_earned': self.coins_earned,
            'time_played': (datetime.now() - self.start_time).seconds,
            'focus_benefit': True
        }

if __name__ == "__main__":
    print("🐍 Wellness Snake - Focus Training Game")
    print("Use arrow keys to move, SPACE to pause, R to restart")
    print("This game improves focus, reaction time, and hand-eye coordination!")
    
    game = WellnessSnake()
    result = game.run()
    
    print(f"\n🎯 Wellness Results:")
    print(f"Score: {result['score']}")
    print(f"Coins Earned: {result['coins_earned']}")
    print(f"Focus Time: {result['time_played']} seconds")
    print(f"Great job on your cognitive wellness training! 🧠✨")