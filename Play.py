import pygame
import Settings


class Shots(pygame.sprite.Sprite):
    def __init__(self, type1, position):
        super().__init__()
        self.type = type1
        self.img_shot = pygame.image.load("shot.png")
        self.image = pygame.transform.scale(self.img_shot, (5, 12))
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self):
        if self.type == "spaceship":
            self.rect.y -= 6
        else:
            self.rect.y += 6
        if self.rect.y > Settings.screen.get_height() or self.rect.y < 0:
            self.kill()


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.spaceship = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.spaceship.get_rect(midbottom=(Settings.screen.get_width() // 2, Settings.screen.get_height()))

    def move_left(self):
        if 0 <= self.rect.x:
            self.rect.x -= 6

    def move_right(self):
        if self.rect.x <= (Settings.WIDTH - self.spaceship.get_width()):
            self.rect.x += 6

    def shot(self):
        return Shots("spaceship", self.rect.center)


class Alien(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.alien = pygame.image.load('alien.bmp')
        self.image = pygame.transform.scale(self.alien, (30, 40))
        self.rect = self.image.get_rect(midbottom=position)
        self.direction = 1

    def update(self):
        self.rect.x += 4 * self.direction

    def move_daon(self):
        self.rect.y += 10
        self.direction *= -1
        if self.rect.y == Settings.HEIGHT:
            print("Sorry game over your score is:", Settings.score)
            exit()

    def shot(self):
        return Shots("alien", self.rect.center)
