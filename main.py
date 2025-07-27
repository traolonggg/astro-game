import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0
asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updatable,drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)

asteroid_field = AsteroidField()
player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)


def main() :


    while True : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000
        screen.fill("black")
        updatable.update(dt)
        for obj in drawable :
            obj.draw(screen)
        for asteroid in asteroids :
            if player.check_collide(asteroid):
                print("GAME OVER!")
                sys.exit()
        pygame.display.flip()
if __name__ == "__main__":
    main()

