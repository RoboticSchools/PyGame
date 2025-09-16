# catch_falling.py
import pygame, sys, random

# Initialize pygame
pygame.init()

# Screen dimensions
w, h = 640, 480
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Catch the Falling Object")
clock = pygame.time.Clock()

# Font setup
font = pygame.font.SysFont(None, 36)

# Basket (player) setup
basket = pygame.Rect(w // 2 - 40, h - 40, 80, 20)  # Positioned at bottom center
basket_speed = 7  # Movement speed of the basket


# Class for falling objects (drops)
class Drop:
    def __init__(self):
        # Random X position (inside screen bounds)
        self.x = random.randint(20, w - 20)
        # Start above the screen
        self.y = -20
        # Random falling speed
        self.vy = random.uniform(3.0, 5.5)
        self.size = 18  # Size of the drop

    def rect(self):
        # Return a pygame rectangle representing the drop
        return pygame.Rect(
            int(self.x - self.size / 2),
            int(self.y - self.size / 2),
            self.size,
            self.size
        )

    def update(self):
        # Move drop downward
        self.y += self.vy


# Game variables
drops = [Drop()]  # List of active drops
score = 0

# Main game loop
while True:
    # Handle events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player controls (basket movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket.x -= basket_speed
    if keys[pygame.K_RIGHT]:
        basket.x += basket_speed

    # Keep basket within screen bounds
    basket.clamp_ip(screen.get_rect())

    # Occasionally spawn new drops
    if random.random() < 0.02:
        drops.append(Drop())

    # Update and check collisions for each drop
    for d in drops[:]:  # Iterate over a copy of the list
        d.update()

        # If basket catches the drop
        if d.rect().colliderect(basket):
            score += 10
            drops.remove(d)

        # If drop falls past the screen bottom → simply remove it
        elif d.y - d.size / 2 > h:
            drops.remove(d)

    # --- Drawing section ---
    screen.fill((18, 24, 40))  # Background color

    # Draw basket
    pygame.draw.rect(screen, (200, 160, 60), basket)

    # Draw drops
    for d in drops:
        pygame.draw.rect(screen, (80, 200, 220), d.rect())

    # Draw score only
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)  # Limit FPS to 60
