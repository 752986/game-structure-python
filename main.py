import pygame
import globals
from gameobject import GameObject

_FRAMERATE = 60

class Game:
	def __init__(self, main_object: GameObject) -> None:
		pygame.init()
		self.screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
		self.clock = pygame.time.Clock()

	def run(self):
		running = True
		while running:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					running = False

			delta = self.clock.tick(_FRAMERATE)

			pygame.display.flip()

		pygame.quit()

if __name__ == "__main__":
	main = GameObject()
	Game(main).run()