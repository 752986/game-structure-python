from pygame.math import Vector2
from pygame.surface import Surface

class GameObject:
	priority: int = 0
	shouldDelete: bool = False
	children: list["GameObject"]

	def __init__(self, children:list["GameObject"]=[]):
		self.children = children

	def update(self, delta:float=1.0):
		for child in self.children:
			child.update(delta)

	def draw(self, surface: Surface, delta:float=1.0):
		pass


class Object2D(GameObject):
	pos: Vector2
	scale: Vector2 = Vector2(1, 1)
	rotation: float = 0.0

	def __init__(self, pos: Vector2, children: list["GameObject"]=[]) -> None:
		super().__init__(children)
		self.pos = pos


class Sprite2D(Object2D):
	image: Surface

	def __init__(self, pos: Vector2, image:Surface, children: list["GameObject"]=[]):
		super().__init__(pos, children)
		self.image = image

	def draw(self, surface: Surface, delta:float=1.0):
		surface.blit(self.image, self.pos)