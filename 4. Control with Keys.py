import pygame

# Initialize Pygame
pygame.init()

# Create window (800x600 pixels)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Move Square - Arrow keys & WASD")

# Define colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Square properties
x, y = 350, 250   # starting position (near center of screen)
size = 100        # width & height of square
speed = 5         # movement speed

# Clock to control frame rate
clock = pygame.time.Clock()

# Game loop flag
running = True

# ---------------- Main Game Loop ---------------- #
while running:
    # Handle events (quit button etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get all pressed keys
    keys = pygame.key.get_pressed()

    # Movement with Arrow keys OR WASD
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:   # Left
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Right
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:     # Up
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:   # Down
        y += speed

    # Keep square inside the screen boundaries
    x = max(0, min(800 - size, x))  # clamp between left & right edges
    y = max(0, min(600 - size, y))  # clamp between top & bottom edges

    # Clear screen (fill with white)
    screen.fill(white)

    # Draw the square at new position
    pygame.draw.rect(screen, blue, (x, y, size, size))

    # Update screen
    pygame.display.update()

    # Limit to 60 frames per second (smooth movement)
    clock.tick(60)

# Quit Pygame safely
pygame.quit()
