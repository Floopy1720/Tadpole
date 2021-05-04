import pygame
import random

WIDTH, HIGEHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HIGEHT))

playerX = 500
playerY = 350
sharkX = 0
FPS = 60
air = pygame.Rect(0, 200, 800, 10)
sharkTime = 1
tick = 0
sharkY = 210
player_hitbox = pygame.Rect(playerX, playerY, 64, 64)
shark_hitbox = pygame.Rect(sharkX, sharkY, 300, 150)

def draw():
    global sharkY
    global sharkX
    global tick
    player = pygame.image.load('bonana.png')
    player = pygame.transform.scale(player, (64, 64))
    shark = pygame.image.load('sharkgame.xcf')
    shark = pygame.transform.scale(shark, (300, 150))
    WIN.fill((25, 255, 255))
    pygame.draw.rect(WIN, (0, 0, 0), air)
    # pygame.draw.rect(WIN, (0, 0, 0), player_hitbox)
    WIN.blit(player, (playerX, playerY))
    # pygame.draw.rect(WIN, (0, 0, 0), shark_hitbox)
    if tick == 370:
        sharkY = random.randint(210, 450)
        tick = 0
        sharkX = -300
        pass

    if player_hitbox.colliderect(shark_hitbox):
        print("Collison")
        pygame.quit()
        pass
    WIN.blit(shark, (sharkX, sharkY))
    pygame.display.update()
    pass


def main():
    clock = pygame.time.Clock()
    global playerY
    global sharkX
    global tick
    global player_hitbox
    global shark_hitbox
    run = True


    while run:
        player_hitbox = pygame.Rect(playerX, playerY, 50, 64)
        shark_hitbox = pygame.Rect(sharkX + 35, sharkY + 40, 265, 80)
        tick += 1
        sharkX += 3
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_presssed = pygame.key.get_pressed()

        if keys_presssed[pygame.K_UP] and playerY > 0:
            playerY -= 4
            pass

        if keys_presssed[pygame.K_DOWN] and playerY < 538:
            playerY += 4
            pass

        draw()
    pass


if __name__ == "__main__":
    main()
