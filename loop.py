import pygame

from Manager import Manager

manager = Manager()

running = True

# Main game loop
while running:
    manager.launch_scren()
    events = pygame.event.get()
    manager.update()
    manager.random_alien_shots()
    manager.move_spaceship()
    manager.spaceship_shot(events)
    manager.exsident()
    manager.check_game_over(events)
    pygame.display.flip()
