import pygame

# Initialize Pygame
pygame.init()

# Create a window of size 800x600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shapes with Names")

# Define colors (R, G, B)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 100, 255)
purple = (200, 0, 200)

# Choose a font (default font, size 36)
font = pygame.font.Font(None, 36)

# Main loop flag
running = True

# Main game loop
while running:
    # Handle events (close window etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background with white
    screen.fill(white)

    # ---------------- Draw Shapes with Labels ---------------- #

    # Top Left - Rectangle
    pygame.draw.rect(screen, red, (150, 100, 150, 100))  # (x, y, width, height)
    text_rect = font.render("Rectangle", True, black)    # Render text
    screen.blit(text_rect, (170, 210))                   # Draw text below shape

    # Top Right - Circle
    pygame.draw.circle(screen, blue, (550, 150), 70)     # (x, y, radius)
    text_circle = font.render("Circle", True, black)
    screen.blit(text_circle, (520, 240))

    # Bottom Left - Line
    pygame.draw.line(screen, green, (150, 425), (300, 425), 6)  # (start, end, thickness)
    text_line = font.render("Line", True, black)
    screen.blit(text_line, (190, 440))

    # Bottom Right - Triangle (Polygon with 3 points)
    pygame.draw.polygon(screen, purple, [(550, 330), (650, 480), (450, 480)])
    text_poly = font.render("Triangle", True, black)
    screen.blit(text_poly, (510, 490))

    # --------------------------------------------------------- #

    # Update display
    pygame.display.update()

# Quit Pygame properly
pygame.quit()
