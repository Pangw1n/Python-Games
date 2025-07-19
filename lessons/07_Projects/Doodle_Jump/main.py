import pygame

#SETTINGS
class GameSettings:
    SCREEN_WIDHT = 300
    SCREEN_HEIGHT = 400
    PLAYER_SIZE = 35
    PLATFORM_WIDTH = 50
PLATFORM_THICKNESS = 20
SPEED = 20
GRAVITY = 1
GAME_SPEED = 15
camera_y_pos = 0
white: tuple = (255, 255, 255)
black: tuple = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))

class Player:
    def __init__(self):
        self.x_vel = 0
        self.y_vel = -16
        self.x = (SCREEN_WIDHT - PLAYER_SIZE) / 2
        self.y = SCREEN_HEIGHT - PLAYER_SIZE - PLATFORM_THICKNESS - 20
        self.hitbox = pygame.Rect(self.x, self.y, PLAYER_SIZE, PLAYER_SIZE)

    def update(self):
        self.y_vel += GRAVITY
        self.x += self.x_vel
        self.y += self.y_vel
        self.hitbox.x = self.x
        self.hitbox.y = self.y
        
    def draw(self):
        pygame.draw.rect(screen, black, self.hitbox)

class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, PLATFORM_WIDTH, PLATFORM_THICKNESS)

    def update(self):
        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def draw(self):
        pygame.draw.rect(screen, black, self.hitbox)

# Define player
player = Player()
platforms = list()
platforms.append(Platform((SCREEN_WIDHT - PLATFORM_WIDTH) / 2, SCREEN_HEIGHT - PLATFORM_THICKNESS - 20))

running = True
clock = pygame.time.Clock()


while running:
    player.update()

    # Draw everything
    screen.fill(white)
    player.draw()
    for x in platforms:
        x.draw()

    pygame.display.flip()
    clock.tick(30)

pygame.quit