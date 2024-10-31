# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x, y)

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        #pygame.Surface.fill((0,0,0))

        #player.update(dt)
        #player.draw(screen)

        for update_thing in updatable:
            update_thing.update(dt)

        for draw_thing in drawable:
            draw_thing.draw(screen)

        pygame.display.flip()

        #At the end of each iteration of the game loop, call the .tick() method, and pass it 60. It will pause the game loop until 1/60th of a second has passed.
        #The .tick() method also returns the amount of time that has passed since the last time it was called: the delta time. Divide the return value by 1000 (to convert from milliseconds to seconds) and save it into the dt variable we created earlier. We're not using dt yet, but we will later.
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
