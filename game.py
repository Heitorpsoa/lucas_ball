import pygame
from pygame.constants import K_UP
from ball import Ball

pygame.init()

WHITE = (255,255,255)

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color(WHITE))

is_running = True


b = Ball([20, 50])

FPS = 30
clock = pygame.time.Clock()

while is_running:

    window_surface.blit(background, (0, 0))
    b.draw(screen=window_surface)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            b.acc = [0, 0.0001]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        b.jump()
    
    if keys[pygame.K_RIGHT]:
        b.move([0.000001, 0])
    elif keys[pygame.K_LEFT]:
        b.move([-0.000001, 0])
    else:
        b.reset()

    pygame.display.update()
clock.tick(FPS)