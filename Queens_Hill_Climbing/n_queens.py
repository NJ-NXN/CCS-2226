import pygame
import sys
import random

def get_attacking_pairs(board):
   # Counts the number of pairs of queens that are attacking each other.
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                attacks += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def hill_climb_step(board):
    # Evaluates all neighboring states (moving one queen to a different row) and returns the best one.
    n = len(board)
    current_attacks = get_attacking_pairs(board)
    
    if current_attacks == 0:
        return board, False 

    best_board = list(board)
    best_attacks = current_attacks
    is_stuck = True

    for col in range(n):
        for row in range(n):
            if board[col] != row:
                neighbor = list(board)
                neighbor[col] = row
                neighbor_attacks = get_attacking_pairs(neighbor)
                
                if neighbor_attacks < best_attacks:
                    best_attacks = neighbor_attacks
                    best_board = neighbor
                    is_stuck = False

    return best_board, is_stuck

# Constants
N = 8 
SQUARE_SIZE = 80
WIDTH = N * SQUARE_SIZE
HEIGHT = N * SQUARE_SIZE

# Colors
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
RED = (220, 20, 60)   # Unsolved queens
GREEN = (34, 139, 34) # Solved queens

def draw_board(screen, n):
    """Draws the checkerboard pattern."""
    for row in range(n):
        for col in range(n):
            color = WHITE if (row + col) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_queens(screen, board, is_solved):
    """Draws the queens as circles."""
    color = GREEN if is_solved else RED
    for col, row in enumerate(board):
        center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
        pygame.draw.circle(screen, color, center, SQUARE_SIZE // 3)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"{N}-Queens Hill Climbing")
    font = pygame.font.SysFont(None, 36)

    # Initialize a random board
    board = [random.randint(0, N-1) for _ in range(N)]
    running = True
    solved = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_board(screen, N)
        
        attacks = get_attacking_pairs(board)
        
        if attacks == 0:
            solved = True
            draw_queens(screen, board, is_solved=True)
            # Display success message
            text = font.render("Solved!", True, (0, 0, 0))
            screen.blit(text, (10, 10))
        else:
            draw_queens(screen, board, is_solved=False)
            
            # Display current attacks
            text = font.render(f"Attacks: {attacks}", True, (0, 0, 0))
            screen.blit(text, (10, 10))

            # Perform the next step of the algorithm
            board, is_stuck = hill_climb_step(board)
            
            if is_stuck and attacks > 0:
                # Random-Restart: We hit a local optimum, so we scramble the board!
                print("Hit a local optimum! Restarting...")
                board = [random.randint(0, N-1) for _ in range(N)]
            
            # Pause briefly so we can actually see the pieces moving
            pygame.time.delay(200) 

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()