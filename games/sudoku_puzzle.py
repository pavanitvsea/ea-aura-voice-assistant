import pygame
import random
import sys
import json
from datetime import datetime
import copy

# Initialize Pygame
pygame.init()

# Game settings
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
GRID_SIZE = 540
CELL_SIZE = GRID_SIZE // 9
GRID_OFFSET_X = (WINDOW_WIDTH - GRID_SIZE) // 2
GRID_OFFSET_Y = 80

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)
GOLD = (255, 215, 0)

class SudokuCell:
    def __init__(self, row, col, value=0):
        self.row = row
        self.col = col
        self.value = value
        self.original = False  # True if part of initial puzzle
        self.selected = False
        self.possible_values = set()
        
    def get_rect(self):
        x = GRID_OFFSET_X + self.col * CELL_SIZE
        y = GRID_OFFSET_Y + self.row * CELL_SIZE
        return pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

class WellnessSudoku:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Sudoku - Logical Wellness Training")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.ui_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Game state
        self.grid = [[SudokuCell(r, c) for c in range(9)] for r in range(9)]
        self.selected_cell = None
        self.difficulty = "Medium"
        self.mistakes = 0
        self.start_time = datetime.now()
        self.game_completed = False
        self.hints_used = 0
        self.coins_earned = 0
        
        self.generate_puzzle()
        self.best_times = self.load_best_times()
        
    def load_best_times(self):
        try:
            with open('sudoku_best_times.json', 'r') as f:
                return json.load(f)
        except:
            return {"Easy": None, "Medium": None, "Hard": None}
            
    def save_best_times(self):
        with open('sudoku_best_times.json', 'w') as f:
            json.dump(self.best_times, f)
            
    def generate_puzzle(self):
        # Generate a complete valid Sudoku grid
        self.solve_grid([[0 for _ in range(9)] for _ in range(9)])
        
        # Copy the complete solution
        complete_grid = [[self.grid[r][c].value for c in range(9)] for r in range(9)]
        
        # Remove numbers based on difficulty
        cells_to_remove = {"Easy": 40, "Medium": 50, "Hard": 60}[self.difficulty]
        
        positions = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(positions)
        
        for r, c in positions[:cells_to_remove]:
            self.grid[r][c].value = 0
            self.grid[r][c].original = False
            
        # Mark remaining cells as original
        for r in range(9):
            for c in range(9):
                if self.grid[r][c].value != 0:
                    self.grid[r][c].original = True
                    
    def solve_grid(self, grid):
        # Simple backtracking solver for puzzle generation
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for num in numbers:
                        if self.is_valid_move(grid, i, j, num):
                            grid[i][j] = num
                            if self.solve_grid(grid):
                                return True
                            grid[i][j] = 0
                    return False
        
        # Copy solved grid to game grid
        for r in range(9):
            for c in range(9):
                self.grid[r][c].value = grid[r][c]
        return True
        
    def is_valid_move(self, grid, row, col, num):
        # Check row
        for c in range(9):
            if grid[row][c] == num:
                return False
                
        # Check column
        for r in range(9):
            if grid[r][col] == num:
                return False
                
        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if grid[r][c] == num:
                    return False
                    
        return True
        
    def is_valid_current_move(self, row, col, num):
        current_grid = [[self.grid[r][c].value for c in range(9)] for r in range(9)]
        return self.is_valid_move(current_grid, row, col, num)
        
    def calculate_coins(self):
        elapsed_time = (datetime.now() - self.start_time).seconds
        base_coins = {"Easy": 20, "Medium": 35, "Hard": 50}[self.difficulty]
        mistake_penalty = self.mistakes * 3
        hint_penalty = self.hints_used * 5
        time_bonus = max(0, (600 - elapsed_time) // 30)  # Bonus for completing quickly
        
        return max(10, base_coins - mistake_penalty - hint_penalty + time_bonus)
        
    def get_hint(self):
        # Find an empty cell and provide the correct number
        empty_cells = [(r, c) for r in range(9) for c in range(9) 
                      if self.grid[r][c].value == 0]
        
        if empty_cells:
            # Generate complete solution to get hint
            temp_grid = [[self.grid[r][c].value for c in range(9)] for r in range(9)]
            if self.solve_sudoku_complete(temp_grid):
                r, c = random.choice(empty_cells)
                self.grid[r][c].value = temp_grid[r][c]
                self.hints_used += 1
                return True
        return False
        
    def solve_sudoku_complete(self, grid):
        # Complete solver for hints
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(grid, i, j, num):
                            grid[i][j] = num
                            if self.solve_sudoku_complete(grid):
                                return True
                            grid[i][j] = 0
                    return False
        return True
        
    def check_completion(self):
        # Check if all cells are filled correctly
        for r in range(9):
            for c in range(9):
                if self.grid[r][c].value == 0:
                    return False
                    
        # Check if solution is valid
        for r in range(9):
            for c in range(9):
                value = self.grid[r][c].value
                self.grid[r][c].value = 0  # Temporarily remove
                if not self.is_valid_current_move(r, c, value):
                    self.grid[r][c].value = value  # Restore
                    return False
                self.grid[r][c].value = value  # Restore
                
        return True
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_completed:
                    self.__init__()  # Reset game
                elif event.key == pygame.K_q:
                    return False
                elif event.key == pygame.K_h and not self.game_completed:
                    self.get_hint()
                elif event.key >= pygame.K_1 and event.key <= pygame.K_9:
                    if self.selected_cell and not self.game_completed:
                        num = event.key - pygame.K_0
                        self.place_number(num)
                elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    if self.selected_cell and not self.game_completed:
                        self.clear_cell()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.game_completed:  # Left click
                    self.handle_cell_click(event.pos)
        return True
        
    def handle_cell_click(self, pos):
        # Check if click is within grid
        if (GRID_OFFSET_X <= pos[0] <= GRID_OFFSET_X + GRID_SIZE and
            GRID_OFFSET_Y <= pos[1] <= GRID_OFFSET_Y + GRID_SIZE):
            
            col = (pos[0] - GRID_OFFSET_X) // CELL_SIZE
            row = (pos[1] - GRID_OFFSET_Y) // CELL_SIZE
            
            # Clear previous selection
            if self.selected_cell:
                self.selected_cell.selected = False
                
            # Select new cell
            self.selected_cell = self.grid[row][col]
            self.selected_cell.selected = True
            
    def place_number(self, num):
        if self.selected_cell and not self.selected_cell.original:
            old_value = self.selected_cell.value
            
            if self.is_valid_current_move(self.selected_cell.row, self.selected_cell.col, num):
                self.selected_cell.value = num
                
                # Check if game is completed
                if self.check_completion():
                    self.game_completed = True
                    elapsed_time = (datetime.now() - self.start_time).seconds
                    self.coins_earned = self.calculate_coins()
                    
                    # Update best time
                    if (self.best_times[self.difficulty] is None or 
                        elapsed_time < self.best_times[self.difficulty]):
                        self.best_times[self.difficulty] = elapsed_time
                        self.save_best_times()
            else:
                self.selected_cell.value = num  # Place it anyway but mark as mistake
                self.mistakes += 1
                
    def clear_cell(self):
        if self.selected_cell and not self.selected_cell.original:
            self.selected_cell.value = 0
            
    def draw_grid(self):
        # Draw cells
        for r in range(9):
            for c in range(9):
                cell = self.grid[r][c]
                rect = cell.get_rect()
                
                # Cell background
                if cell.selected:
                    color = LIGHT_BLUE
                elif cell.original:
                    color = LIGHT_GRAY
                else:
                    color = WHITE
                    
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)
                
                # Cell value
                if cell.value != 0:
                    text_color = BLACK if cell.original else BLUE
                    text = self.font.render(str(cell.value), True, text_color)
                    text_rect = text.get_rect(center=rect.center)
                    self.screen.blit(text, text_rect)
                    
        # Draw thick lines for 3x3 boxes
        for i in range(1, 3):
            # Vertical lines
            x = GRID_OFFSET_X + i * 3 * CELL_SIZE
            pygame.draw.line(self.screen, BLACK, 
                           (x, GRID_OFFSET_Y), 
                           (x, GRID_OFFSET_Y + GRID_SIZE), 3)
            # Horizontal lines
            y = GRID_OFFSET_Y + i * 3 * CELL_SIZE
            pygame.draw.line(self.screen, BLACK, 
                           (GRID_OFFSET_X, y), 
                           (GRID_OFFSET_X + GRID_SIZE, y), 3)
                           
        # Grid border
        pygame.draw.rect(self.screen, BLACK, 
                        (GRID_OFFSET_X, GRID_OFFSET_Y, GRID_SIZE, GRID_SIZE), 3)
        
    def draw_ui(self):
        # Title
        title = self.ui_font.render("🧩 Sudoku - Logical Wellness Training", True, BLACK)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 30))
        self.screen.blit(title, title_rect)
        
        # Stats
        elapsed_time = (datetime.now() - self.start_time).seconds
        time_text = self.small_font.render(f"Time: {elapsed_time // 60}:{elapsed_time % 60:02d}", True, BLACK)
        mistakes_text = self.small_font.render(f"Mistakes: {self.mistakes}", True, BLACK)
        hints_text = self.small_font.render(f"Hints: {self.hints_used}", True, BLACK)
        difficulty_text = self.small_font.render(f"Level: {self.difficulty}", True, BLACK)
        
        self.screen.blit(time_text, (20, 55))
        self.screen.blit(mistakes_text, (150, 55))
        self.screen.blit(hints_text, (280, 55))
        self.screen.blit(difficulty_text, (380, 55))
        
        # Best time
        if self.best_times[self.difficulty]:
            best_time = self.best_times[self.difficulty]
            best_text = self.small_font.render(f"Best: {best_time // 60}:{best_time % 60:02d}", True, BLUE)
            self.screen.blit(best_text, (480, 55))
            
        # Instructions
        if not self.game_completed:
            inst_text = self.small_font.render("Click cell, press 1-9 to enter number, H for hint", True, GRAY)
            self.screen.blit(inst_text, (20, WINDOW_HEIGHT - 50))
        
        # Win screen
        if self.game_completed:
            # Semi-transparent overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            # Win message
            win_text = self.ui_font.render("🎉 Puzzle Solved!", True, GOLD)
            coins_text = self.ui_font.render(f"Wellness Coins Earned: {self.coins_earned}", True, WHITE)
            elapsed_time = (datetime.now() - self.start_time).seconds
            stats_text = self.small_font.render(f"Time: {elapsed_time // 60}:{elapsed_time % 60:02d} | Mistakes: {self.mistakes} | Hints: {self.hints_used}", True, WHITE)
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
        tip_text = self.small_font.render("💡 Sudoku enhances logical thinking, pattern recognition, and mental focus!", True, BLUE)
        self.screen.blit(tip_text, (20, WINDOW_HEIGHT - 25))
        
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            
            # Clear screen
            self.screen.fill(WHITE)
            
            # Draw game
            self.draw_grid()
            self.draw_ui()
            
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()
        
        # Return wellness data
        elapsed_time = (datetime.now() - self.start_time).seconds
        return {
            'game': 'Sudoku',
            'difficulty': self.difficulty,
            'time': elapsed_time,
            'mistakes': self.mistakes,
            'hints_used': self.hints_used,
            'coins_earned': self.coins_earned,
            'completed': self.game_completed,
            'logical_benefit': True
        }

if __name__ == "__main__":
    print("🧩 Sudoku - Logical Wellness Training")
    print("Fill the 9x9 grid so each row, column, and 3x3 box contains digits 1-9!")
    print("This game improves logical thinking, problem-solving, and concentration!")
    
    game = WellnessSudoku()
    result = game.run()
    
    print(f"\n🎯 Wellness Results:")
    print(f"Difficulty: {result['difficulty']}")
    print(f"Time: {result['time'] // 60}:{result['time'] % 60:02d}")
    print(f"Mistakes: {result['mistakes']}")
    print(f"Hints Used: {result['hints_used']}")
    print(f"Coins Earned: {result['coins_earned']}")
    print(f"Completed: {result['completed']}")
    print(f"Excellent logical workout! Your problem-solving skills are sharp! 🧩✨")