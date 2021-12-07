__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.1.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
    Main file for the template.
    This is where the main loop starts.
"""

import pygame
from src.support.auxiliar_functions import get_screen_text
from src.support.game_links import Game_links as Link
from src.support.colors import Game_color as color


WIDTH = 700
HEIGHT = 500

class Game:

    pygame.init()

    screen_size: tuple
    screen: pygame.Surface
    current_link: str
    game_events: pygame.event
    game_links: dict
    clock: pygame.time

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
        self.screen.fill(color.black.value)

    def game_events_handler(self) -> bool:
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

# Making the dict of the game links with link name and the related function
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

    game_links[game.current_link](game)
    print("Current path: ", game.current_link)
