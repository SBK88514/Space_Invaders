import random

from Play import *


class Manager(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.screen = Settings.screen
        self.scaled_image = Settings.scaled_image
        self.alien_a = Alien  # Create an instance of the Alien class
        self.aliens = pygame.sprite.Group()  # Group for aliens
        self.grid_aliens = self.create_grid_aliens()
        self.counter_a = 0  # Counter for alien shots
        self.spaceship = Spaceship()  # Create an instance of the Spaceship class
        self.position_shot1 = self.spaceship.rect.centerx  # Initial position of shots
        self.shots_s = pygame.sprite.Group()  # Group for player shots
        self.shots_a = pygame.sprite.Group()  # Group for alien shots
        self.clock = pygame.time.Clock()

    def launch_scren(self):
        pygame.init()
        self.clock.tick(60) / 1000

    def create_grid_aliens(self):
        for i in range(Settings.Alien_lines):
            for j in range(Settings.Alien_columns):
                x = 100 + j * 50
                y = 100 + i * 50
                self.aliens.add(self.alien_a((x, y)))
        return self.aliens

    def move_spaceship(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.spaceship.move_left()
        if keys[pygame.K_RIGHT]:
            self.spaceship.move_right()

    def spaceship_shot(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                new_shot = self.spaceship.shot()
                self.shots_s.add(new_shot)

    def update(self):  # Update and draw elements on the screen
        self.shots_a.update()
        self.shots_s.update()
        self.move_aliens()
        self.screen.blit(self.scaled_image, (0, 0))
        self.screen.blit(self.spaceship.spaceship, self.spaceship.rect)
        self.aliens.draw(Settings.screen)
        self.shots_a.draw(Settings.screen)
        self.shots_s.draw(Settings.screen)

    def move_aliens(self):
        for alien in self.aliens:
            if alien.rect.right >= Settings.WIDTH or alien.rect.left <= 0:
                for alien in self.aliens:
                    alien.move_daon()
        self.aliens.update()

    def random_alien_shots(self):
        if self.aliens and self.counter_a == 40:
            random_alien = random.choice(self.aliens.sprites())
            random_alien_shot = random_alien.shot()
            self.shots_a.add(random_alien_shot)
            self.counter_a = 0
        self.counter_a += 1

    def exsident(self):  # Handle collisions and update the score/life
        pygame.sprite.groupcollide(self.shots_a, self.shots_s, True, True)
        if pygame.sprite.groupcollide(self.aliens, self.shots_s, True, True):
            Settings.score += 1
        if pygame.sprite.spritecollide(self.spaceship, self.shots_a, True):
            Settings.life -= 1
        if pygame.sprite.spritecollide(self.spaceship, self.aliens, True):
            print("Your score:", Settings.score)
            exit()

    def check_game_over(self, events):
        for event in events:
            if event.type == pygame.QUIT or Settings.life == 0:
                print("Your score:", Settings.score)
                exit()
            elif not self.aliens:
                print("Congratulations! You cleared the aliens. Your score:", Settings.score)
                exit()
