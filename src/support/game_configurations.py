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
CLOCK_FRAME = 40


class Game:
    """
        Class to control the game screen and event's configuration.
        And also is possible to pass variable of control on this class, 
        This because it will be passed by the other class.
    """

    pygame.init()

    screen_size: tuple              # To be used in the other class loop's
    screen: pygame.Surface          # The game Surface
    current_link: str               # Variable to control the link's and current state
    game_events: pygame.event       # To store all the event's that might happen
    clock: pygame.time              # The frame range to be used
    clock_frame: int                # The value to be used on the clock
    background_color: tuple         # To store the RGB value of the BG color
                                        # what allow's us to control and change 
                                        # in any place of the game  

    def __init__(self):
        self.screen_size = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(get_screen_text("game_tittle"))
        self.game_events = None
        self.current_link = "game_loop"
        self.clock = pygame.time.Clock()
        self.clock_frame = CLOCK_FRAME
        self.background_color = color.black.value

        self.screen_fill_bg()
    
    def screen_fill_bg(self) -> None:
        """
            Setting the background color.
        """
        self.screen.fill(self.background_color)
    
    def change_bg_color(self, rgb_color: tuple) -> None:
        """
            Method to change the background color
        """
        self.background_color = rgb_color

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