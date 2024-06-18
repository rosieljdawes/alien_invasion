import sys
import pygame

class AlienInvasion:
    """overall class to manage game assets and behaviour"""

    def __init__(self):
        """initialise the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # set background colour
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        """start the main loop for the game"""
        while True:
            # what for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            # make the most recently drawn screen available
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()