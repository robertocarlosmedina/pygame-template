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

    button_clicked :str
    button_start_position :dict
    box_dim :dict
    mouse_position :pygame.mouse

    def __init__(self, game_obj) -> None:
        self.game_obj = game_obj
        self.quit_confirmation_buttons = ["Yes", "No"]
        self.button_clicked = ""
        self.box_dim = {
            "x":100,
            "y":40
        }
        self.button_start_position = {
            "x":int((self.game_obj.screen_size[0] / 2) - (self.box_dim["x"] * 2 + 20) / 2),
            "y":int((self.game_obj.screen_size[1] / 2) - (self.box_dim["y"] * 2) / 2) + 20
        }
        
    def draw_quit_menu_buttons(self) -> None:
        self.button_clicked = horizontalButtonDisplay(
            screen = self.game_obj.screen,
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

    def run_link(self) -> str:
        change_page_by_action = change_page_by_action = False

        while True:
            self.mouse_position = pygame.mouse.get_pos()
            self.mouse_pos = pygame.mouse.get_pos()
            self.game_obj.screen_fill_bg()

            font_size = pygame.font.Font.size(fonts.montserrat_size_18.value, get_screen_text("game_quit_text"))
            line = fonts.montserrat_size_18.value.render(get_screen_text("game_quit_text"), True, color.white.value)
            self.game_obj.screen.blit(line, (self.game_obj.screen_size[0]/2-(font_size[0]/2), (self.game_obj.screen_size[1]/2-(font_size[1]/2) - 60)))

            self.draw_quit_menu_buttons()

            if (self.button_clicked != ""):
                if(self.button_clicked == "Yes"):
                    exit(1)
                else:
                    self.button_clicked = ""
                    self.game_obj.current_link = "game_menu"
                    change_page_by_action = True

            change_page_by_event = self.game_obj.game_events_handler()

            if change_page_by_action or change_page_by_event:
                break

            pygame.display.update()