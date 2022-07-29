from modules.parts import Color,Rect
from modules.block import Block,Platform
from modules.ball import Ball
import pygame
FRAME_PER_SECOND = 300



class Window:
    def __init__(self,game='Game'):
        pygame.init()
        self.display = pygame.display.set_mode((1024, 768))
        self.level = 0
        pygame.display.update()
        pygame.display.set_caption("Арканоид")
        self.width, self.height = pygame.display.get_surface().get_size()
        self.platform = Platform(self)
        self.ball = Ball()

        self.blocks = [Block(Color(255, 0, 0), Rect(x=i, y=j, width=self.width // 7, height=24)) for i in
                       range(0, 900, self.width // 7 + 1) for j in range(0, 101, 25)]
        self.is_running = True

    def render(self):
        self.ball.render(self, self.platform, pygame, self.display)
        self.platform.render(pygame, self.display)
        for block in self.blocks:
            block.render(pygame, self.display)
        self.level_text_render()

        pygame.display.update()
        self.display.fill((30, 0, 0))

    # @staticmethod
    def game_over(self):
        font = pygame.font.Font(None, 40)
        if self.blocks:
            game_over_text = font.render(f"GAME OVER!", True, (0, 255, 0))
        else:
            game_over_text = font.render(f"YOU WIN", True, (0, 255, 0))
        self.display.blit(game_over_text, (200, 200))

    def make_harder(self, ball: 'Ball', platform: 'Platform'):
        # +
        ball.speed += 1
        platform.pos.width -= 25
        self.level += 1

    def level_text_render(self):

        font = pygame.font.Font(None, 40)
        level_num = font.render(f"Level:{self.level}", True, (0, 255, 205))
        self.display.blit(level_num, (0, 400))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                self.game_over()
            self.platform.handle_events(event)

    def run(self):
        while self.is_running:
            pygame.time.delay(1000 // FRAME_PER_SECOND)
            self.handle_events()
            self.render()

    def stop(self):
        pygame.quit()





# def main():
#     game = Window()
#     game.run()
#
#     pygame.time.delay(1000)
#     game.stop()
#
#
# if __name__ == '__main__':
#     main()
