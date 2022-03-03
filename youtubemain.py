import pygame
import sys

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Jumping in PyGame")

X_POSITION, Y_POSITION = 400, 660

jumping = False

Y_GRAVITY = 0.6
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("assets/mario_standing.png"), (48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("assets/mario_jumping.png"), (48, 64))
BACKGROUND = pygame.image.load("assets/background.png")

mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
        jumping = True

    SCREEN.blit(BACKGROUND, (0, 0))
    
    if jumping:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
        mario_rect = JUMPING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(JUMPING_SURFACE, mario_rect)
    else:
        mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(STANDING_SURFACE, mario_rect)
        

    pygame.display.update()
    CLOCK.tick(60)