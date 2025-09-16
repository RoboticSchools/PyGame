# brick_breaker_clean.py
import pygame
import sys
import random

# Initialize pygame
pygame.init()

# --- Screen setup ---
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()

# --- Fonts ---
font = pygame.font.SysFont(None, 36)

# --- Game state ---
score = 10        # Start score at 10 (as requested)
lives = 10        # Start with 10 lives
game_over = False # Flag for game over
game_win = False  # Flag for game win

# --- Paddle setup ---
paddle_width, paddle_height = 120, 14
paddle = pygame.Rect(
    screen_width // 2 - paddle_width // 2,  # Center horizontally
    screen_height - 40,                     # Position near bottom
    paddle_width,
    paddle_height
)
paddle_speed = 8  # Paddle movement speed

# --- Ball setup ---
ball_size = 20
ball = pygame.Rect(screen_width // 2 - ball_size // 2, screen_height - 60, ball_size, ball_size)

def reset_ball():
    """Reset ball to starting position and return new velocity."""
    ball.center = (screen_width // 2, screen_height - 80)
    return random.choice([-5, 5]), -5  # Random horizontal direction, upward vertical

# Initial ball velocity
ball_velocity_x, ball_velocity_y = reset_ball()

# --- Bricks setup ---
top_reserved_space = 80  # Reserved space at the top for score/lives
brick_rows, brick_columns = 6, 10
brick_width = screen_width // brick_columns

def create_bricks():
    """Create a grid of bricks and return as a list of Rects."""
    return [
        pygame.Rect(col * brick_width + 5, row * 30 + top_reserved_space, brick_width - 10, 24)
        for row in range(brick_rows) for col in range(brick_columns)
    ]

# Initial brick layout
bricks = create_bricks()

# --- Main game loop ---
while True:
    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close the game window
            pygame.quit()
            sys.exit()

        # Restart game when pressing R after game over or win
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and (game_over or game_win):
            paddle.topleft = (screen_width // 2 - paddle_width // 2, screen_height - 40)  # Reset paddle
            bricks = create_bricks()  # Reset bricks
            lives = 10
            score = 10
            ball_velocity_x, ball_velocity_y = reset_ball()
            game_over = False
            game_win = False

    # --- Game logic (only runs if not over/win) ---
    if not game_over and not game_win:
        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.x -= paddle_speed
        if keys[pygame.K_RIGHT]:
            paddle.x += paddle_speed
        paddle.clamp_ip(screen.get_rect())  # Keep paddle within screen bounds

        # Ball movement
        ball.x += ball_velocity_x
        ball.y += ball_velocity_y

        # Bounce off walls
        if ball.left <= 0 or ball.right >= screen_width:
            ball_velocity_x *= -1
        if ball.top <= 0:
            ball_velocity_y *= -1

        # Paddle collision
        if ball.colliderect(paddle) and ball_velocity_y > 0:
            ball_velocity_y *= -1  # Bounce upwards
            # Add horizontal velocity based on where the ball hit the paddle
            offset = (ball.centerx - paddle.centerx) / (paddle.width / 2)
            ball_velocity_x += int(offset * 2)

        # Brick collisions
        hit_index = ball.collidelist(bricks)  # Check collision with any brick
        if hit_index != -1:
            hit_brick = bricks.pop(hit_index)  # Remove brick
            score += 10
            # Decide whether to reflect X or Y based on collision side
            if abs(ball.centerx - hit_brick.centerx) > hit_brick.width / 2:
                ball_velocity_x *= -1
            else:
                ball_velocity_y *= -1

        # Ball falls below screen
        if ball.bottom >= screen_height:
            lives -= 1
            ball_velocity_x, ball_velocity_y = reset_ball()
            if lives <= 0:
                game_over = True  # No lives left

        # Win condition
        if not bricks:
            game_win = True  # All bricks cleared

    # --- Drawing ---
    screen.fill((12, 12, 20))  # Background color

    if not game_over and not game_win:
        # Draw paddle
        pygame.draw.rect(screen, (200, 200, 200), paddle)

        # Draw ball
        pygame.draw.ellipse(screen, (255, 150, 60), ball)

        # Draw bricks
        for brick in bricks:
            pygame.draw.rect(screen, (150, 50, 200), brick)

    # Always draw score and lives at top center
    top_text = font.render(f"Score: {score}    Lives: {lives}", True, (255, 255, 255))
    screen.blit(top_text, (screen_width // 2 - top_text.get_width() // 2, 10))

    # Display win/lose messages
    if game_win:
        win_text = font.render("YOU WIN! Press R to play again", True, (180, 255, 180))
        screen.blit(win_text, (screen_width // 2 - win_text.get_width() // 2, screen_height // 2 - 20))
    elif game_over:
        game_over_text = font.render("GAME OVER - Press R to restart", True, (255, 120, 120))
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - 20))

    # Update display
    pygame.display.flip()
    clock.tick(60)  # Cap frame rate at 60 FPS
