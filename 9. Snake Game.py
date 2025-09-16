# snake_clean.py
import pygame
import sys
import random

# Initialize pygame
pygame.init()

# --- Screen setup ---
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# --- Fonts ---
font = pygame.font.SysFont(None, 36)

# --- Grid setup ---
cell_size = 20  # Each snake segment size
columns, rows = screen_width // cell_size, screen_height // cell_size  # Number of grid cells


def spawn_food(snake_body):
    """Spawn food at a random grid position that is not occupied by the snake"""
    while True:
        x = random.randrange(columns) * cell_size
        y = random.randrange(rows) * cell_size
        if (x, y) not in snake_body:  # Ensure food doesn't spawn on the snake
            return (x, y)


# --- Snake setup ---
snake_body = [(columns // 2 * cell_size, rows // 2 * cell_size)]  # Start at center
snake_direction = (1, 0)  # Initially moving right
food_position = spawn_food(snake_body)
score = 0
game_over = False

# --- Main loop ---
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            # Arrow keys to control direction (cannot go directly backward)
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            if event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            if event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            if event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

            # Restart game when pressing "R" after game over
            if event.key == pygame.K_r and game_over:
                snake_body = [(columns // 2 * cell_size, rows // 2 * cell_size)]
                snake_direction = (1, 0)
                food_position = spawn_food(snake_body)
                score = 0
                game_over = False

    if not game_over:
        # --- Snake movement ---
        head_x = snake_body[0][0] + snake_direction[0] * cell_size
        head_y = snake_body[0][1] + snake_direction[1] * cell_size

        # Wrap around screen (snake reappears on opposite side)
        head_x = head_x % screen_width
        head_y = head_y % screen_height
        new_head = (head_x, head_y)

        # --- Check collisions ---
        if new_head in snake_body:  # Self-collision → Game over
            game_over = True
        else:
            snake_body.insert(0, new_head)  # Move snake head
            if new_head == food_position:  # Snake eats food
                score += 10
                food_position = spawn_food(snake_body)  # Spawn new food
            else:
                snake_body.pop()  # Remove tail (snake moves forward)

    # --- Drawing section ---
    screen.fill((15, 15, 25))  # Background color

    # Draw snake
    for segment in snake_body:
        pygame.draw.rect(
            screen,
            (100, 200, 120),
            (segment[0], segment[1], cell_size - 2, cell_size - 2)
        )

    # Draw food
    pygame.draw.rect(
        screen,
        (255, 220, 60),
        (food_position[0], food_position[1], cell_size - 2, cell_size - 2)
    )

    # Draw score
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

    # Draw game over message
    if game_over:
        game_over_text = font.render("GAME OVER - Press R to restart", True, (255, 100, 100))
        screen.blit(
            game_over_text,
            (screen_width // 2 - game_over_text.get_width() // 2,
             screen_height // 2 - 20)
        )

    # Update display
    pygame.display.flip()
    clock.tick(10)  # Control snake speed (10 FPS)
