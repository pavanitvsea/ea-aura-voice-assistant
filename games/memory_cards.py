import pygame
import random
import sys
import json
from datetime import datetime
import time

# Initialize Pygame
pygame.init()

# Game settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CARD_WIDTH = 80
CARD_HEIGHT = 100
CARDS_PER_ROW = 6
ROWS = 4
MARGIN = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (128, 128, 128)
LIGHT_BLUE = (173, 216, 230)
GOLD = (255, 215, 0)

class MemoryCard:
    def __init__(self, x, y, emoji, pair_id):
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.emoji = emoji
        self.pair_id = pair_id
        self.flipped = False
        self.matched = False
        
    def draw(self, screen, font):
        if self.matched:
            color = GREEN
        elif self.flipped:
            color = LIGHT_BLUE
        else:
            color = BLUE
            
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        
        if self.flipped or self.matched:
            text = font.render(self.emoji, True, BLACK)
            text_rect = text.get_rect(center=self.rect.center)
            screen.blit(text, text_rect)

class WellnessMemoryGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Memory Cards - Cognitive Wellness Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.ui_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Memory game emojis (wellness themed)
        self.emojis = ['🧠', '💚', '🌟', '💪', '🧘', '🌿', '💎', '🌞', '🎯', '✨', '🏃', '🍎']
        
        # Game state
        self.reset_game()
        self.best_time = self.load_best_time()
        self.coins_earned = 0
        
    def reset_game(self):
        self.cards = []
        self.flipped_cards = []
        self.matches = 0
        self.moves = 0
        self.start_time = datetime.now()
        self.game_won = False
        self.current_time = 0
        
        # Create card pairs
        selected_emojis = self.emojis[:12]  # Use 12 different emojis for 24 cards
        card_emojis = selected_emojis * 2  # Create pairs
        random.shuffle(card_emojis)
        
        # Calculate card positions
        start_x = (WINDOW_WIDTH - (CARDS_PER_ROW * (CARD_WIDTH + MARGIN))) // 2
        start_y = 100
        
        for i, emoji in enumerate(card_emojis):
            row = i // CARDS_PER_ROW
            col = i % CARDS_PER_ROW
            x = start_x + col * (CARD_WIDTH + MARGIN)
            y = start_y + row * (CARD_HEIGHT + MARGIN)
            
            card = MemoryCard(x, y, emoji, selected_emojis.index(emoji))
            self.cards.append(card)
            
    def load_best_time(self):
        try:
            with open('memory_best_time.json', 'r') as f:
                data = json.load(f)
                return data.get('best_time', float('inf'))
        except:
            return float('inf')
            
    def save_best_time(self):
        data = {'best_time': self.current_time}
        with open('memory_best_time.json', 'w') as f:
            json.dump(data, f)
            
    def calculate_coins(self):
        # Coins based on performance: fewer moves = more coins
        base_coins = 30
        move_bonus = max(0, (50 - self.moves) // 2)  # Bonus for efficiency
        time_bonus = max(0, (120 - self.current_time) // 10)  # Bonus for speed
        return base_coins + move_bonus + time_bonus
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_won:
                    self.reset_game()
                elif event.key == pygame.K_q:
                    return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.game_won:  # Left click
                    self.handle_card_click(event.pos)
        return True
        
    def handle_card_click(self, pos):
        if len(self.flipped_cards) >= 2:
            return
            
        for card in self.cards:
            if (card.rect.collidepoint(pos) and 
                not card.flipped and not card.matched):
                
                card.flipped = True
                self.flipped_cards.append(card)
                
                if len(self.flipped_cards) == 2:
                    self.moves += 1
                    pygame.time.set_timer(pygame.USEREVENT + 1, 1000)  # Check match after 1 second
                break
                
    def check_match(self):
        if len(self.flipped_cards) == 2:
            card1, card2 = self.flipped_cards
            
            if card1.pair_id == card2.pair_id:
                # Match found!
                card1.matched = True
                card2.matched = True
                self.matches += 1
                
                # Check if game is won
                if self.matches == 12:  # All 12 pairs matched
                    self.game_won = True
                    self.current_time = (datetime.now() - self.start_time).seconds
                    self.coins_earned = self.calculate_coins()
                    
                    if self.current_time < self.best_time:
                        self.best_time = self.current_time
                        self.save_best_time()
            else:
                # No match, flip back
                card1.flipped = False
                card2.flipped = False
                
            self.flipped_cards.clear()
            
    def update_game(self):
        if not self.game_won:
            self.current_time = (datetime.now() - self.start_time).seconds
            
        # Handle pygame events
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT + 1:
                self.check_match()
                pygame.time.set_timer(pygame.USEREVENT + 1, 0)  # Cancel timer
                
    def draw_game(self):
        # Background
        self.screen.fill(WHITE)
        
        # Title
        title = self.ui_font.render("🧠 Memory Cards - Cognitive Wellness Training", True, BLACK)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 30))
        self.screen.blit(title, title_rect)
        
        # Draw cards
        for card in self.cards:
            card.draw(self.screen, self.font)
            
        # Game stats
        moves_text = self.small_font.render(f"Moves: {self.moves}", True, BLACK)
        time_text = self.small_font.render(f"Time: {self.current_time}s", True, BLACK)
        matches_text = self.small_font.render(f"Matches: {self.matches}/12", True, BLACK)
        
        self.screen.blit(moves_text, (20, 60))
        self.screen.blit(time_text, (150, 60))
        self.screen.blit(matches_text, (280, 60))
        
        if self.best_time != float('inf'):
            best_text = self.small_font.render(f"Best Time: {int(self.best_time)}s", True, BLUE)
            self.screen.blit(best_text, (420, 60))
            
        # Win screen
        if self.game_won:
            # Semi-transparent overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            # Win message
            win_text = self.ui_font.render("🎉 Excellent Memory Work!", True, GOLD)
            coins_text = self.ui_font.render(f"Wellness Coins Earned: {self.coins_earned}", True, WHITE)
            stats_text = self.small_font.render(f"Completed in {self.moves} moves and {self.current_time} seconds!", True, WHITE)
            restart_text = self.small_font.render("Press R to play again, Q to quit", True, WHITE)
            
            win_rect = win_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
            coins_rect = coins_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20))
            stats_rect = stats_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60))
            
            self.screen.blit(win_text, win_rect)
            self.screen.blit(coins_text, coins_rect)
            self.screen.blit(stats_text, stats_rect)
            self.screen.blit(restart_text, restart_rect)
            
        # Wellness tip
        tip_text = self.small_font.render("💡 Memory games strengthen neural pathways and improve concentration!", True, BLUE)
        self.screen.blit(tip_text, (20, WINDOW_HEIGHT - 30))
        
        pygame.display.flip()
        
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update_game()
            self.draw_game()
            self.clock.tick(60)
            
        pygame.quit()
        
        # Return wellness data
        return {
            'game': 'Memory Cards',
            'moves': self.moves,
            'time': self.current_time,
            'best_time': self.best_time if self.best_time != float('inf') else None,
            'coins_earned': self.coins_earned,
            'completed': self.game_won,
            'cognitive_benefit': True
        }

if __name__ == "__main__":
    print("🧠 Memory Cards - Cognitive Wellness Training")
    print("Click cards to flip them and find matching pairs!")
    print("This game improves memory, concentration, and cognitive flexibility!")
    
    game = WellnessMemoryGame()
    result = game.run()
    
    print(f"\n🎯 Wellness Results:")
    print(f"Moves: {result['moves']}")
    print(f"Time: {result['time']} seconds")
    print(f"Coins Earned: {result['coins_earned']}")
    print(f"Completed: {result['completed']}")
    print(f"Great cognitive workout! Your memory and focus are getting stronger! 🧠✨")