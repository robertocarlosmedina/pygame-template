__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from src.support.font import Game_fonts as fonts
from src.support.colors import Game_color as color
from src.support.buttons import horizontalButtonDisplay
from src.support.auxiliar_functions import get_screen_text

class Game_quit:

    screen :pygame.Surface
    screen_size :tuple
    button_clicked :str
    button_start_position :dict
    box_dim :dict
    mouse_position :pygame.mouse

    def __init__(self, screen, screen_size) -> None:
        self.screen = screen
        self.screen_size = screen_size
        self.quit_confirmation_buttons = ["Yes", "No"]
        self.button_clicked = ""
        self.box_dim = {
            "x":100,
            "y":40
        }
        self.button_start_position = {
            "x":int((self.screen_size[0] / 2) - (self.box_dim["x"] * 2 + 20) / 2),
            "y":int((self.screen_size[1] / 2) - (self.box_dim["y"] * 2) / 2) + 20
        }
        


    def run_link(self, game_event:pygame.event) -> str:
        del game_event
        self.mouse_position = pygame.mouse.get_pos()

        font_size = pygame.font.Font.size(fonts.montserrat_size_18.value, get_screen_text("game_quit_text"))
        line = fonts.montserrat_size_18.value.render(get_screen_text("game_quit_text"), True, color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-(font_size[0]/2), (self.screen_size[1]/2-(font_size[1]/2) - 60)))

        self.button_clicked = horizontalButtonDisplay(
            screen = self.screen,
            buttons = self.quit_confirmation_buttons,
            start_position = {
                "x": self.button_start_position["x"],
                "y": self.button_start_position["y"]
            },
            box_dim = self.box_dim,
            mouse_pos = self.mouse_position,
            font = fonts.montserrat_size_16.value,
            button_clicked = self.button_clicked
        )
        
        if (self.button_clicked != ""):
            if(self.button_clicked == "Yes"):
                exit(1)
            else:
                self.button_clicked = ""
                return "game_menu"

        return "game_quit"