import pygame

#SETTING
SCREEN_WIDHT = 300
SCREEN_HEIGHT = 400
PLAYER_SIZE = 35
PLATFORM_WIDTH = 50
PLATFORM_THICKNESS = 20
SPEED = 20
GRAVITY = -1
GAME_SPEED = 15
MAX_Y_DIFF = 200
WHITE: tuple = (255, 255, 255)
BLACK: tuple = (0, 0, 0)

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Initialize screen
        self.screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
        self.cam_y_pos = 0

    def start_game(self):
        # Define player
        self.player = Player()
        self.platforms = list()
        self.platforms.append(Platform((SCREEN_WIDHT - PLATFORM_WIDTH) / 2, PLATFORM_THICKNESS + 20))

        self.running = True
        self.clock = pygame.time.Clock()

        while self.running:
            self.player.update(self)

            # Draw everything
            self.screen.fill(WHITE)
            self.player.draw(self.screen)
            for x in self.platforms:
                x.update(self)
                x.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit
    
    def y_to_screen(self, y):
        return SCREEN_HEIGHT - (y - self.cam_y_pos)

class Player:
    def __init__(self):
        self.x_vel = 0
        self.y_vel = 16
        self.x = (SCREEN_WIDHT - PLAYER_SIZE) / 2
        self.y = PLAYER_SIZE + PLATFORM_THICKNESS + 20
        self.hitbox = pygame.Rect(self.x, self.y, PLAYER_SIZE, PLAYER_SIZE)

    def update(self, game):
        self.y_vel += GRAVITY
        self.x += self.x_vel
        self.y += self.y_vel
        if self.y > game.cam_y_pos + MAX_Y_DIFF:
            game.cam_y_pos = self.y - MAX_Y_DIFF
        self.hitbox.x = self.x
        self.hitbox.y = game.y_to_screen(self.y)
        
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.hitbox)

class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, PLATFORM_WIDTH, PLATFORM_THICKNESS)

    def update(self, game):
        self.hitbox.x = self.x
        self.hitbox.y = game.y_to_screen(self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.hitbox)

game = Game()
game.__init__()
game.start_game()