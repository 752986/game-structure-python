import pygame
import settings
from gameobject import GameObject


class Game:
	def __init__(self, root_object: GameObject, clear_color: pygame.Color=pygame.Color(0, 0, 0)) -> None:
		pygame.init()
		self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
		self.clock = pygame.time.Clock()
		self.root = root_object
		self.clear_color = clear_color

	def run(self):
		running = True
		while running:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					running = False

			delta = self.clock.tick(settings.FRAMERATE) / 1000

			#print(1/delta)

			self.root.update(self.screen, delta)

			pygame.display.flip()

			self.screen.fill(self.clear_color)

		pygame.quit()
