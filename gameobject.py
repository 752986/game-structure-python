import pygame
import globals

class GameObject:
	priority: int = 0
	shouldDelete: bool = False

	def __init__(self, children: list["GameObject"]=[]) -> None:
		self.children = children

	def update(self, delta:float=1.0):
		for child in self.children:
			child.update(delta)

	def draw(self, delta:float=1.0):
		pass
