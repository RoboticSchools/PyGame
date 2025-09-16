# score_system.py
import pygame, sys, random

# Initialize Pygame
pygame.init()

# Screen setup
w, h = 640, 480
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Score System Game")
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.SysFont(None, 36)

# ---------------- Player Setup ---------------- #
# Create a rectangle for the player
player = pygame.Rect(w // 2 - 15, h - 60, 30, 30)  # x, y, width, height
speed = 5  # movement speed

# ---------------- Coin Setup ---------------- #
# Place coin at a random position on screen
coin = pygame.Rect(
    random.randint(20, w - 40),
    random.randint(20, h - 100),
    20, 20
)

# ---------------- Score ---------------- #
score = 0

# ---------------- Main Game Loop ---------------- #
while True:
    # Handle quit event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Keep player inside the screen boundaries
    player.clamp_ip(screen.get_rect())

    # Collision check: if player touches coin
    if player.colliderect(coin):
        score += 10  # increase score
        # respawn coin at new random position
        coin.x = random.randint(20, w - 40)
        coin.y = random.randint(20, h - 100)

    # ---------------- Drawing Section ---------------- #
    screen.fill((30, 30, 40))  # background color

    # Draw player (green rectangle)
    pygame.draw.rect(screen, (90, 200, 120), player)

    # Draw coin (gold rectangle)
    pygame.draw.rect(screen, (255, 215, 0), coin)

    # Display score in top-left corner
    score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surf, (10, 10))

    # Refresh the display
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)
