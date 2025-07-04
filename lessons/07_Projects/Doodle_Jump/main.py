import pygame

#VARIABLES
SCREEN_WIDHT = 300
SCREEN_HEIGHT = 400
PLAYER_SIZE = 20
PLATFORM_WIDTH = 50
PLATFORM_THICKNESS = 20
SPEED = 20
GRAVITY = 1
GAME_SPEED = 15
white: tuple = (255, 255, 255)
black: tuple = (0, 0, 0)
player_x_vel = 0
player_y_vel = -15

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))

# Define player
player = pygame.Rect((SCREEN_WIDHT - PLAYER_SIZE) / 2, SCREEN_HEIGHT - PLAYER_SIZE - PLATFORM_THICKNESS - 20, PLAYER_SIZE, PLAYER_SIZE)
platforms = list()
platforms.append(pygame.Rect((SCREEN_WIDHT - PLATFORM_WIDTH) / 2, SCREEN_HEIGHT - PLATFORM_THICKNESS - 20, PLATFORM_WIDTH, PLATFORM_THICKNESS))

running = True
clock = pygame.time.Clock()

while running:
    player_y_vel += GRAVITY
    player.x += player_x_vel
    player.y += player_y_vel

    # Draw everything
    screen.fill(white)
    pygame.draw.rect(screen, black, player)
    for x in platforms:
        pygame.draw.rect(screen, black, x)

    pygame.display.flip()
    clock.tick(30)

pygame.quit