import pygame

# Initialize Pygame
pygame.init()

# Set up screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Rectangle Back and Forth")

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)

# Rectangle properties
rect_x = 100      # starting x position of rectangle
rect_y = 250      # fixed y position (rectangle will only move horizontally)
rect_width = 120  # rectangle width
rect_height = 80  # rectangle height
rect_speed = 5    # speed at which rectangle moves

# Clock object to control FPS (frames per second)
clock = pygame.time.Clock()

# Game loop flag
running = True

# ---------------- Main Game Loop ---------------- #
while running:
    # Event handling (check for quit button click)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the rectangle horizontally
    rect_x += rect_speed

    # If rectangle touches left or right edge, reverse its direction
    if rect_x <= 0 or rect_x + rect_width >= screen_width:
        rect_speed = -rect_speed

    # Fill screen with white color (clear previous frame)
    screen.fill(white)

    # Draw the red rectangle at its new position
    pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))

    # Update the screen with new drawing
    pygame.display.update()

    # Run at 60 frames per second (smooth movement)
    clock.tick(60)

# Quit Pygame safely
pygame.quit()
