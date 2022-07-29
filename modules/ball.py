from dataclasses import dataclass
from modules.parts import Color,Direction
@dataclass

class SetBall:
    x: int
    y: int
    radius: int

    def to_pygame(self):
        return [self.x, self.y, self.radius]
class Ball:
    def __init__(self):
        self.color = Color(255, 0, 0)
        self.pos = SetBall(x=60, y=450, radius=10)
        self.direction_x = Direction.RIGHT
        self.direction_y = Direction.UP
        self.speed = 1
        self.color_dict = {1: Color(0, 255, 0), 2: Color(0, 0, 255), 3: Color(255, 0, 0)}
    def update(self):
        if self.direction_x == Direction.LEFT:
            self.pos.x -= self.speed
        if self.direction_y == Direction.UP:
            self.pos.y -= self.speed
        if self.direction_x == Direction.RIGHT:
            self.pos.x += self.speed
        if self.direction_y == Direction.DOWN:
            self.pos.y += self.speed

    def ball_direction_changer(self, platform: 'Platform', game: 'Window'):
        self.block_collapse(game, platform)
        if self.pos.x <= 10:
            self.direction_x = Direction.RIGHT
        if self.pos.x > game.width - 10:
            self.direction_x = Direction.LEFT
        if self.pos.y <= 10:
            self.direction_y = Direction.DOWN

        if self.pos.y + 10 > game.height - 20 and platform.pos.x < self.pos.x + 6 and self.pos.x < platform.pos.x + platform.pos.width:
            if self.direction_x != platform.direction and platform.is_running:
                self.direction_x = platform.direction
                self.direction_y = Direction.UP
            else:
                self.direction_y = Direction.UP
        elif self.pos.y >= game.height:
            self.speed = 0
            game.game_over()
            game.is_running = False

    def render(self, game: 'Window', platform: 'Platform', pygame, display):
        self.update()

        self.ball_direction_changer(platform, game)

        if platform.direction == Direction.LEFT and platform.is_running:
            if platform.platform_limiter(game) != "no_left":
                platform.pos.x -= platform.speed

        elif platform.direction == Direction.RIGHT and platform.is_running:
            if platform.platform_limiter(game) != "no_right":
                platform.pos.x += platform.speed
        pygame.draw.circle(display, self.color.to_pygame(), (self.pos.x, self.pos.y),
                           self.pos.radius)

    def block_collapse(self, game: 'Window', platform: 'Platform'):

        if not game.blocks:
            game.is_running = False
        for block in game.blocks:
            if block.pos.y + 20 >= self.pos.y - 5 and block.pos.x <= self.pos.x + 6 <= block.pos.x + block.pos.width:
                block.level -= 1
                if block.level == 0:
                    game.blocks.remove(block)
                    game.make_harder(self, platform)
                else:
                    block.color = self.color_dict[block.level]
                self.direction_y = Direction.DOWN