import pygame
from block import *
from sprite import *
from maps import *

WIDTH = 1600
HEIGHT = 832
FPS = 60
bg = pygame.image.load("img\\bg.jpg")
klick = 0
hp = 5
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MorningRay')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Hero()
all_sprites.add(player)
map = maps[0]


isJump = False
run = True
while run:

    clock.tick(FPS)
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Проверяем нажатые кнопки
        if event.type == pygame.KEYDOWN and event.key != pygame.K_SPACE:
            player.move_player(event.key)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and klick < 2:
            isJump = True
            player.jump = -17
            player.is_moving = False
            klick += 1


        if event.type == pygame.KEYUP and  event.key != pygame.K_SPACE:
            player.stop_player(event.key)

    for y in range(13):
        for x in range(25):
            if map[y][x] == 1:
                screen.blit(pygame.image.load("img\\floor.JPG"), (x * 64, y * 64))
            elif map[y][x] == 2:
                screen.blit(pygame.image.load("img\\object.JPG"), (x * 64, y * 64))

    player.move()

    if player.is_moving:
        player.move()

    elif isJump:
        print(player.rect.y)
        if player.rect.y <= 600:
            player.rect.y = player.rect.y + player.jump
            player.jump = player.jump + 1.5
            if player.jump == 0:
                player.jump += 1
            print(player.jump, player.rect.y )
        else:
            isJump = False
            player.jump = 0
            player.rect.y = 600
            klick = 0


    all_sprites.update()

    all_sprites.draw(screen)
    pygame.display.flip()

    pygame.display.update()









