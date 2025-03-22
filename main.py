import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()


	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	drawable.add(player)
	updatable.add(player)
	updatable.add(asteroid_field)

	

	Player.containers = (updatable, drawable, asteroids)
	Asteroid.containers = (updatable, drawable, asteroids)
	Shot.containers = (updatable, drawable, shots)
	AsteroidField.containers = (updatable,)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		

		for obj in drawable:
			obj.draw(screen)
		
		updatable.update(dt)

		for obj in asteroids:
			if obj.collide(player):
				return

		pygame.display.flip()
		clock.tick(60)
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
