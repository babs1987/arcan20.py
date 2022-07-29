from modules.window import Window
import pygame

def main():
    game = Window()
    game.run()

    pygame.time.delay(1000)
    game.stop()


if __name__ == '__main__':
    main()