import pygame
import sys

pygame.init()

# Window
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Pac-Man")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Pac-Man settings
pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2
pacman_speed = 5
pacman_size = 15

# Dot list
dots = []
for i in range(30):
    dots.append([pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]])
import random
dots = [[random.randint(20, 580), random.randint(20, 580)] for _ in range(40)]

clock = pygame.time.Clock()

# Game loop
while True:
    screen.fill(BLACK)

    # Close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Draw Pac-Man
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_size)

    # Draw dots
    for d in dots[:]:
        pygame.draw.circle(screen, WHITE, d, 5)
        # Collision detection
        if abs(pacman_x - d[0]) < 20 and abs(pacman_y - d[1]) < 20:
            dots.remove(d)

    pygame.display.update()
    clock.tick(60)
    
