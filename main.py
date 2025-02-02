import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0)) # black screen
        for u in updatable:
            u.update(dt)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000

if __name__ == "__main__":
    main()