__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from src.pages.pause_menu import Game_Pause_Menu
from src.pages.game_over import Game_over
from src.game_components.game import Game_loop
from src.pages.start import Game_start
from src.pages.menu import Game_menu
from src.pages.quit import Game_quit
from src.pages.credits import Game_Credits
from src.pages.game_mode import Game_mode


class Game_links:
    game_page_object :object
    game_backup :object

    def __init__(self) -> None:
        self.game_page_object = object
        self.game_backup = object

    def start_game(self, game_obj: object) -> str:
        if(not isinstance(self.game_page_object, Game_start)):
            self.game_page_object = Game_start(game_obj)
        return  self.game_page_object.run_link()

    def game_main_menu(self, game_obj: object) -> str:
        if(not isinstance(self.game_page_object, Game_menu)):
            self.game_page_object = Game_menu(game_obj)
        return  self.game_page_object.run_link()

    def continue_game(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(isinstance(self.game_backup, Game_loop)):
            self.game_page_object = self.game_backup
        
        if(not isinstance(self.game_page_object, Game_loop)):
            self.game_page_object = Game_mode(screen, screen_size)

        return  self.game_page_object.run_link(game_event)

    def gameplay_loop(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_loop)):
            self.game_page_object = Game_loop(screen, screen_size)
        
        next_page = self.game_page_object.run_link(game_event)

        if (next_page != "game_loop"):
            self.game_backup = self.game_page_object

        return  next_page

    def game_credits(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_Credits)):
            self.game_page_object = Game_Credits(screen, screen_size)
        return  self.game_page_object.run_link(game_event)

    def game_quit(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_quit)):
            self.game_page_object = Game_quit(screen, screen_size)
        return  self.game_page_object.run_link(game_event)

    def game_pause_menu(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_Pause_Menu)):
            self.game_page_object = Game_Pause_Menu(screen, screen_size)
        return  self.game_page_object.run_link(game_event)

    def game_over(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_over)):
            self.game_backup = object
            self.game_page_object = Game_over(screen, screen_size)
        return  self.game_page_object.run_link(game_event)
    
    def chose_game_mode(self, screen :pygame.Surface, screen_size :tuple, game_event :pygame.event) -> str:
        if(not isinstance(self.game_page_object, Game_mode)):
            self.game_backup = object
            self.game_page_object = Game_mode(screen, screen_size)
        return  self.game_page_object.run_link(game_event)
