import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0
asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable,drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)

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
        for asteroid in asteroids :
            for bullet in shots :
                if bullet.check_collide(asteroid):
                    bullet.kill()
                    asteroid.split()
        pygame.display.flip()
if __name__ == "__main__":
    main()

