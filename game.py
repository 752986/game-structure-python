import pygame
import settings
from gameobject import GameObject

class Game:
	def __init__(self, root_object: GameObject) -> None:
		pygame.init()
		self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
		self.clock = pygame.time.Clock()
		self.root = root_object

	def run(self):
		running = True
		while running:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					running = False

			delta = self.clock.tick(settings.FRAMERATE) / 1000

			self.root.update(delta)

			pygame.display.flip()

		pygame.quit()
