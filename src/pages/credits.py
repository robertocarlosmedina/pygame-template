__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.5"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from pygame.constants import NOEVENT
from src.support.font import Game_fonts as fonts
from src.support.colors import Game_color as color
from src.support.buttons import verticalButtonsDisplay
from src.support.auxiliar_functions import draw_header_styled_lines, get_screen_text

class Game_Credits:

    game_buttons :list
    button_clicked :str
    mouse_position :tuple
    menu_tittles :dict
    menus_start_positions :dict
    buttons_size :dict

    def __init__(self, game_obj) -> None:
        self.game_obj = game_obj
        self.button_clicked = ""
        self.game_buttons = {
            "game_menu": "Back",
        }
        self.buttons_size = {
            "x":220,
            "y":50
        }
        self.menus_start_positions = {
            "game_menu":{
                "x": int(self.game_obj.screen_size[0]/2 - self.buttons_size["x"]/2),
                "y":190
            }
        }
    
    def credits_content(self) -> None:

        font_size = pygame.font.Font.size(fonts.montserrat_size_22.value, get_screen_text("game_credits_tittle"))
        line = fonts.montserrat_size_22.value.render(get_screen_text("game_credits_tittle"), True, color.green.value)
        self.game_obj.screen.blit(
            line, 
            (self.menus_start_positions["game_menu"]["x"]-(font_size[0]/2)+(self.buttons_size["x"]/2),
                self.menus_start_positions["game_menu"]["y"]-font_size[1]*2)
        )
        draw_header_styled_lines(self.game_obj.screen, self.game_obj.screen_size)

        font_size = pygame.font.Font.size(fonts.montserrat_size_22.value, f"Game made by {__author__}")
        line = fonts.montserrat_size_22.value.render(f"Game made by {__author__}", True, color.white_1.value)
        self.game_obj.screen.blit(
            line, 
            (self.menus_start_positions["game_menu"]["x"]-(font_size[0]/2)+(self.buttons_size["x"]/2),
                self.menus_start_positions["game_menu"]["y"]+font_size[1]/2)
        )
        
        y = font_size[1] + 20
        for text in get_screen_text("author_text"):
            font_size = pygame.font.Font.size(fonts.montserrat_size_16.value, text)
            line = fonts.montserrat_size_16.value.render(text, True, color.white_1.value)
            self.game_obj.screen.blit(
                line, 
                (self.menus_start_positions["game_menu"]["x"]-(font_size[0]/2)+(self.buttons_size["x"]/2),
                    self.menus_start_positions["game_menu"]["y"]+font_size[1]/2 + y)
            )
            y += font_size[1]

    def draw_menu_buttons(self) -> None:
        self.button_clicked = verticalButtonsDisplay(
            screen = self.game_obj.screen,
            buttons = self.game_buttons.values(),
            start_position = {
                "x":self.menus_start_positions["game_menu"]["x"],
                "y":self.menus_start_positions["game_menu"]["y"]+180
            },
            box_dim = self.buttons_size,
            mouse_pos = self.mouse_pos,
            font = fonts.montserrat_size_16.value,
            button_clicked = self.button_clicked
        )

    def run_link(self) -> str:
        change_page_by_action = change_page_by_action = False

        while True: 
            self.mouse_pos = pygame.mouse.get_pos()
            self.game_obj.screen_fill_bg()

            font_size = pygame.font.Font.size(fonts.montserrat_size_30.value, get_screen_text("game_tittle"))
            line = fonts.montserrat_size_30.value.render(get_screen_text("game_tittle"), True, color.white.value)
            self.game_obj.screen.blit(line, (self.game_obj.screen_size[0]/2-(font_size[0]/2), 25))

            self.credits_content()
            self.draw_menu_buttons()

            if (self.button_clicked != "" ):
                for key,value in self.game_buttons.items():
                    if(self.button_clicked == value):
                        self.button_clicked = ""
                        self.game_obj.current_link = key
                        change_page_by_action = True
                        break

            change_page_by_event = self.game_obj.game_events_handler()

            if change_page_by_action or change_page_by_event:
                break

            pygame.display.update()
            
