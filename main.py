from game import Game
import settings
import pygame
from object2d import Object2D, Sprite2D, Transform2D
from gameobject import GameObject
import math
import cProfile


game = Game()

# this file is garbage, but it demonstrates how this structure works

# this class extends the Sprite2D class, giving it custom behavior while reusing the behaivoir of Sprite2D 
class Niko(Sprite2D):
	def __init__(self, transform: Transform2D = Transform2D(), global_only: bool = False, children: list[GameObject] = []):
		super().__init__(pygame.image.load("res/OneShot_Niko_Vector.webp"), transform, global_only, children)

	def update(self, surface: pygame.surface.Surface, delta: float = 1):
		# this class displays an image that spins over time
		self.local_transform.rotation += delta * 0.5
		super().update(surface, delta)

# this class doesn't directly draw anything, so it doesn't need to inherit from Sprite2D. It does have a transform, though, so it inherits from Object2D
class MultiNiko(Object2D):
	# the initializer for the class creates a Niko instance, and gives it some children in the form of alternate nikos
	# as the MultiNiko moves, its child Niko is moved automatically                  <┬ THIS IS THE COOL PART
	# likewise, as the Niko moves and spins, its child niko Sprite2Ds are also moved <┘
	def __init__(self, N_BULBS: int = 9, transform: Transform2D = Transform2D(), global_only: bool = False, children: list[GameObject] = []):
		super().__init__(transform, global_only, children)
		for _ in range(10): # change the `1` to a `2` and watch the framerate get cut in half <- THIS IS THE NOT COOL PART
			niko = Niko()
			niko.children = [Sprite2D(transform=Transform2D(pygame.Vector2(math.cos(math.tau / N_BULBS * i) * 400, math.sin(math.tau / N_BULBS * i) * 400), pygame.Vector2(0.1, 0.1)), image=pygame.image.load("res/Niko_(OS).webp")) for i in range(0, N_BULBS)]
			self.children.append(niko)

	def update(self, surface: pygame.surface.Surface, delta: float = 1):
		self.global_transform.origin.y = math.sin(pygame.time.get_ticks() / 2000) * 200 + settings.HEIGHT / 2
		super().update(surface, delta)

def run():
	root = MultiNiko(N_BULBS=5, transform=Transform2D(pygame.Vector2(settings.WIDTH / 2, settings.HEIGHT / 2)))
	game.set_state(root, pygame.Color(15, 10, 20))
	game.run()

if __name__ == "__main__":
	cProfile.run("run()", sort=1)
	#run()