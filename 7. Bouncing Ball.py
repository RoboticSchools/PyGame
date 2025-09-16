import pygame

# Initialize Pygame
pygame.init()

# Set screen size
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)

# Ball properties
ball_x, ball_y = 100, 100              # starting position (x, y)
ball_radius = 25                       # radius of the ball
ball_velocity_x, ball_velocity_y = 5, 4  # speed in x and y directions

# Clock to control FPS
clock = pygame.time.Clock()

# Game loop flag
running = True

# ---------------- Main Game Loop ---------------- #
while running:
    # Handle quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Bounce off left and right walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_velocity_x = -ball_velocity_x  # reverse x direction

    # Bounce off top and bottom walls
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
        ball_velocity_y = -ball_velocity_y  # reverse y direction

    # Clear screen with white background
    screen.fill(white)

    # Draw the red ball at current position
    pygame.draw.circle(screen, red, (int(ball_x), int(ball_y)), ball_radius)

    # Refresh the screen
    pygame.display.update()

    # Run at 60 frames per second
    clock.tick(60)

# Quit Pygame safely
pygame.quit()
