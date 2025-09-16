# pong_clean.py
import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
screen_width, screen_height = 800, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.SysFont(None, 48)

# Paddle setup
paddle_width, paddle_height = 12, 90
# Left paddle positioned at x=30
left_paddle = pygame.Rect(30, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)
# Right paddle positioned near right edge
right_paddle = pygame.Rect(screen_width - 30 - paddle_width, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Ball setup
ball_size = 20
ball = pygame.Rect(
    screen_width // 2 - ball_size // 2,
    screen_height // 2 - ball_size // 2,
    ball_size,
    ball_size
)
ball_velocity_x, ball_velocity_y = 5, 4  # Initial ball velocity

# Score
score_left, score_right = 0, 0

# --- Main game loop ---
while True:
    # Handle events (quit game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement (keyboard controls)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Left paddle up
        left_paddle.y -= 6
    if keys[pygame.K_s]:  # Left paddle down
        left_paddle.y += 6
    if keys[pygame.K_UP]:  # Right paddle up
        right_paddle.y -= 6
    if keys[pygame.K_DOWN]:  # Right paddle down
        right_paddle.y += 6

    # Keep paddles inside the screen
    left_paddle.clamp_ip(screen.get_rect())
    right_paddle.clamp_ip(screen.get_rect())

    # Move the ball
    ball.x += ball_velocity_x
    ball.y += ball_velocity_y

    # Bounce off top and bottom walls
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_velocity_y *= -1  # Reverse vertical direction

    # Collision with left paddle
    if ball.colliderect(left_paddle) and ball_velocity_x < 0:
        ball_velocity_x *= -1  # Reverse horizontal direction
        # Add spin depending on where the ball hits the paddle
        offset = (ball.centery - left_paddle.centery) / (paddle_height / 2)
        ball_velocity_y = int(ball_velocity_y + offset * 3)

    # Collision with right paddle
    if ball.colliderect(right_paddle) and ball_velocity_x > 0:
        ball_velocity_x *= -1
        offset = (ball.centery - right_paddle.centery) / (paddle_height / 2)
        ball_velocity_y = int(ball_velocity_y + offset * 3)

    # Scoring conditions
    if ball.left <= 0:  # Right player scores
        score_right += 1
        # Reset ball to center
        ball.center = (screen_width // 2, screen_height // 2)
        ball_velocity_x = 5  # Send ball to the right

    if ball.right >= screen_width:  # Left player scores
        score_left += 1
        ball.center = (screen_width // 2, screen_height // 2)
        ball_velocity_x = -5  # Send ball to the left

    # --- Drawing section ---
    screen.fill((10, 10, 30))  # Background color

    # Draw paddles
    pygame.draw.rect(screen, (200, 200, 200), left_paddle)
    pygame.draw.rect(screen, (200, 200, 200), right_paddle)

    # Draw ball
    pygame.draw.ellipse(screen, (255, 200, 0), ball)

    # Draw center divider line
    center_line = pygame.Rect(screen_width // 2 - 2, 0, 4, screen_height)
    pygame.draw.rect(screen, (80, 80, 80), center_line)

    # Draw scores
    left_score_surface = font.render(str(score_left), True, (255, 255, 255))
    right_score_surface = font.render(str(score_right), True, (255, 255, 255))
    screen.blit(left_score_surface, (screen_width // 4 - left_score_surface.get_width() // 2, 20))
    screen.blit(right_score_surface, (3 * screen_width // 4 - right_score_surface.get_width() // 2, 20))

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit FPS to 60
