import pygame
import random

#SETTING
SCREEN_WIDHT = 300
SCREEN_HEIGHT = 400
PLAYER_SIZE = 35
PLATFORM_WIDTH = 60
PLATFORM_THICKNESS = 20
PLAYER_SPEED = 10
JUMP_SPEED = 16
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
        self.player = Player(self)
        self.platforms = pygame.sprite.Group()
        self.next_y = PLATFORM_THICKNESS + 20

        self.running = True
        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update game objects
            self.player.update(self)

            self.spawn_new_platforms()

            for platform in self.platforms:
                platform.update(self)
            
            # Check for collisions
            collider = pygame.sprite.spritecollide(self.player, self.platforms, dokill=False)
            if collider and self.player.y_vel <= 0:
                for c in collider:
                    if self.player.y > c.y:
                        self.player.jump(JUMP_SPEED)
                        break

            # Draw everything
            self.screen.fill(WHITE)
            for sprite in self.platforms:
                sprite.draw(self.screen)
            self.player.draw(self.screen)
            pygame.display.flip()
            pygame.event.pump()
            clock.tick(30)
        pygame.quit
    
    def y_to_screen(self, y):
        return SCREEN_HEIGHT - (y - self.cam_y_pos)
    
    def spawn_platform(self, y):
        self.platforms.add(Platform(self, random.random() * SCREEN_WIDHT, y))
        self.next_y = y + 50

    def spawn_new_platforms(self):
        if self.cam_y_pos + SCREEN_HEIGHT > self.next_y:
            self.spawn_platform(self.next_y)



class GameObject(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = game.y_to_screen(y)

    def update(self, game):
        self.rect.centerx = self.x
        self.rect.centery = game.y_to_screen(self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self)



class Player(GameObject):
    def __init__(self, game):
        self.y_vel = JUMP_SPEED
        super().__init__(game, SCREEN_WIDHT / 2, 0, PLAYER_SIZE, PLAYER_SIZE)
        #self.hitbox = pygame.Rect(self.x, self.y, PLAYER_SIZE, PLAYER_SIZE)

    def update(self, game):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.x += PLAYER_SPEED

        self.x = self.x % SCREEN_WIDHT
        
        self.y_vel += GRAVITY
        self.y += self.y_vel
        if self.y > game.cam_y_pos + MAX_Y_DIFF:
            game.cam_y_pos = self.y - MAX_Y_DIFF
        super().update(game)
        
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self)

    def jump(self, speed):
        self.y_vel = speed



class Platform(GameObject):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, PLATFORM_WIDTH, PLATFORM_THICKNESS)

    def update(self, game):
        super().update(game)
        if self.y < game.cam_y_pos:
            game.platforms.remove(self)

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self)



game1 = Game()
game1.__init__()
game1.start_game()