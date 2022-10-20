from pygame.surface import Surface

class GameObject:
	priority: int = 0
	shouldDelete: bool = False
	children: list["GameObject"]

	def __init__(self, children: list["GameObject"] = []):
		self.children = children

	def update(self, surface: Surface, delta:float=1.0):
		for child in self.children:
			child.update(surface, delta)
		
		self.draw(surface, delta)

	def draw(self, surface: Surface, delta:float=1.0):
		pass