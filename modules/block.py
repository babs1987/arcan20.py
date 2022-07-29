import pygame
from modules.parts import Rect,Color,Direction
class Block:
    def __init__(self, color: 'Color' = None, position: 'Rect' = None, level=3):
        self.color = color
        self.pos = position
        self.level = level

    def __str__(self):
        return f"{self.pos.x}:{self.pos.y}:{self.color}"

    def render(self, pygame, display):
        #for i in game.blocks:
        pygame.draw.rect(display, self.color.to_pygame(), self.pos.to_pygame())


class Platform(Block):
    def __init__(self, game: 'Window'):
        self.color = Color(0, 200, 100)
        self.pos = Rect(x=0, y=game.height - 20, width=400, height=20)
        self.is_running = False
        self.direction = Direction.RIGHT
        self.speed = 3

    def platform_limiter(self, game: 'Window'):
        if self.pos.x <= 0:
            return "no_left"
        elif self.pos.x + self.pos.width >= game.width:
            return "no_right"

    def handle_events(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # and self.platform_limiter() != "no_left":
                self.is_running = True
                self.direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT:  # and self.platform_limiter() != "no_right":
                self.is_running = True
                self.direction = Direction.RIGHT

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.is_running = False
                self.direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT:
                self.is_running = False
                self.direction = Direction.RIGHT

    def render(self, pygame, display):
        pygame.draw.rect(display, self.color.to_pygame(), self.pos.to_pygame())
