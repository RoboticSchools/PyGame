import pygame
import random

# Initialize Pygame
pygame.init()

# Create a game window with size 800x600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Random Color Changing Window")

# Start with black color
color = (0, 0, 0)

# Keep track of the last time color was changed
last_change = pygame.time.get_ticks()

# Game loop flag
running = True

# Main game loop
while running:
    # Handle all events (keyboard, mouse, close button etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicks the close (X) button
            running = False

    # Check if 1 second (1000 ms) has passed since the last color change
    if pygame.time.get_ticks() - last_change >= 1000:
        # Pick a new random RGB color (each value between 0 and 255)
        color = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))
        
        # Update the time of the last color change
        last_change = pygame.time.get_ticks()

    # Fill the entire window with the current color
    screen.fill(color)

    # Refresh the screen with updated color
    pygame.display.update()

# Quit Pygame properly
pygame.quit()
