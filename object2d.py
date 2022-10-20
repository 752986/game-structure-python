from math import degrees
from pygame.transform import (smoothscale, rotozoom)
from pygame.math import Vector2
from pygame.surface import Surface
from gameobject import GameObject


class Transform2D:
	origin: Vector2
	scale: Vector2 = Vector2(1, 1)
	rotation: float = 0.0

	def __init__(self, origin: Vector2 = Vector2(0, 0), scale: Vector2 = Vector2(1, 1), rotation: float = 0.0) -> None:
		self.origin = origin
		self.scale = scale
		self.rotation = rotation

	def xform_point(self, v: Vector2):
		return Vector2(v.x * self.scale.x, v.y * self.scale.y).rotate_rad(-self.rotation) + self.origin

	def xform_transform(self, other: "Transform2D"):
		return Transform2D(self.xform_point(other.origin), Vector2(self.scale.x * other.scale.x, self.scale.y * other.scale.y), self.rotation + other.rotation) # TODO: scale algorithm may be incorrect, it may need to be adjsuted based on the rotation of `other`

	

	# def xform_surface(self, s: Surface): # TODO: replace with "draw with transform"
	# 	return rotate(smoothscale(s, (s.get_width() * self.scale.x, s.get_height() * self.scale.y)), degrees(self.rotation))


class Object2D(GameObject):
	local_transform: Transform2D
	global_transform: Transform2D
	global_only: bool

	def __init__(self, transform: Transform2D = Transform2D(), global_only: bool = False, children: list[GameObject] = []):
		super().__init__(children)
		self.local_transform = transform
		self.global_transform = self.local_transform
		self.global_only = global_only

	def update(self, surface: Surface, delta: float = 1):
		for child in self.children:
			if isinstance(child, Object2D) and not child.global_only:
				child.global_transform = self.global_transform.xform_transform(child.local_transform)

		super().update(surface, delta)


class Sprite2D(Object2D):
	image: Surface

	def __init__(self, image: Surface, transform: Transform2D = Transform2D(), global_only: bool = False, children: list[GameObject] = []):
		super().__init__(transform, global_only, children)
		self.image = image

	def update(self, surface: Surface, delta: float = 1):
		super().update(surface, delta)

	def draw(self, surface: Surface, delta: float = 1):
		transformed_image = rotozoom(
				smoothscale(
					self.image, 
					(
						self.image.get_width() * self.global_transform.scale.x, 
						self.image.get_height() * self.global_transform.scale.y
					)
				), 
				degrees(
					self.global_transform.rotation
				),
				1.0
			)

		surface.blit(transformed_image, self.global_transform.origin - Vector2(transformed_image.get_rect().center))

