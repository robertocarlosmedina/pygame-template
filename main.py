__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.1.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
    Main file for the template.
    This is where the main loop starts.
    And from here according to the page that the player are it will be to the main
    loop of that page.
"""

import pygame
from src.support.auxiliar_functions import get_screen_text
from src.support.game_links import Game_links as Link
from src.support.colors import Game_color as color

WIDTH = 700
HEIGHT = 500

game_links: dict            # To store all the links an possible page to go on the game

class Game:

    pygame.init()

    screen_size: tuple              # To be used in the other class loop's
    screen: pygame.Surface          # The game Surface
    current_link: str               # Variable to control the link's and current state
    game_events: pygame.event       # To store all the event's that might happen
    clock: pygame.time              # The frame range to be used
    clock_frame: int                # The value to be used on the clock

    def __init__(self):
        self.screen_size = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(get_screen_text("game_tittle"))
        self.game_events = None
        self.current_link = "game_loop"
        self.clock = pygame.time.Clock()
        self.clock_frame = 40

        self.screen_fill_bg()
    
    def screen_fill_bg(self) -> None:
        """
            Setting the background color.
        """
        self.screen.fill(color.black.value)

    def game_events_handler(self) -> bool:
        """
            Control / Handle the game event's.
            And then return if there is a change in the current link.
        """
        self.game_events = pygame.event.get()
        for event in self.game_events:
            if event.type == pygame.QUIT:
                self.current_link = "game_quit"
                return True

            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_KP_ENTER]:
                    exit()
                elif pygame.key.get_pressed()[pygame.K_ESCAPE] and self.current_link == "game_loop":
                    self.current_link = "game_pause_menu"
                    return True
        
        self.clock.tick(self.clock_frame)
        return False

links = Link()

game_links = {
    "game_start": links.start_game,
    "game_menu": links.game_main_menu,
    "game_loop": links.gameplay_loop,
    "game_quit": links.game_quit,
    "game_credits": links.game_credits,
    "game_continue": links.continue_game,
    "game_pause_menu": links.game_pause_menu,
    "game_over": links.game_over
}

game = Game()

while True:
    """
        Main Loop of the game.
    """
    game_links[game.current_link](game)
    print("Current path: ", game.current_link)
