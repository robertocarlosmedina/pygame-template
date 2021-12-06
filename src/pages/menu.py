__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
    This is the main menu class. This class controls all the navegation that
    can be done on the game.

"""

import pygame
from pygame.constants import NOEVENT
from src.support.font import Game_fonts as fonts
from src.support.colors import Game_color as color
from src.support.buttons import verticalButtonsDisplay
from src.support.auxiliar_functions import draw_header_styled_lines, get_screen_text

class Game_menu:

    game_buttons :list
    button_clicked :str
    mouse_position :tuple
    menus_start_positions :dict
    buttons_size :dict

    def __init__(self, game_obj: object) -> None:
        self.game_obj = game_obj
        self.button_clicked = ""
        self.delay = 0
        self.start_buttons_info()

    def start_buttons_info(self):
        self.game_buttons = {
            "game_chose_mode": "New Game", 
            "game_continue":"Continue", 
            "game_credits":"Credits", 
            "game_quit":"Quit"
        }
        self.buttons_size = {
            "x":220,
            "y":50
        }
        self.menus_start_positions = {
            "game_menu":{
                "x":int(self.game_obj.screen_size[0]/2 - self.buttons_size["x"]/2),
                "y":190
            },
        }
    
    def game_play_buttons(self) -> None:

        font_size = pygame.font.Font.size(fonts.montserrat_size_22.value, get_screen_text("game_main_menu_text"))
        line = fonts.montserrat_size_22.value.render(get_screen_text("game_main_menu_text"), True, color.white_1.value)
        self.game_obj.screen.blit(
            line, 
            (self.menus_start_positions["game_menu"]["x"]-(font_size[0]/2)+(self.buttons_size["x"]/2),
                self.menus_start_positions["game_menu"]["y"]-font_size[1]*2)
        )

        self.button_clicked = verticalButtonsDisplay(
            screen = self.game_obj.screen,
            buttons = self.game_buttons.values(),
            start_position = {
                "x":self.menus_start_positions["game_menu"]["x"],
                "y":self.menus_start_positions["game_menu"]["y"]
            },
            box_dim = self.buttons_size,
            mouse_pos = self.mouse_pos,
            font = fonts.montserrat_size_16.value,
            button_clicked = self.button_clicked
        )

    def on_press_delay_control(self) -> bool:
        if self.delay > 10:
            return False

        self.delay += 1
        return True

    def run_link(self) -> str:
        change_page_by_event = change_page_by_action = False

        while True:
            self.game_obj.screen_fill_bg()
            

            self.mouse_pos = pygame.mouse.get_pos()
            font_size = pygame.font.Font.size(fonts.montserrat_size_30.value, get_screen_text("game_tittle"))
            line = fonts.montserrat_size_30.value.render(get_screen_text("game_tittle"), True, color.red_2.value)
            self.game_obj.screen.blit(line, (self.game_obj.screen_size[0]/2-(font_size[0]/2), 25))
            draw_header_styled_lines(self.game_obj.screen, self.game_obj.screen_size)
            self.game_play_buttons()

            

            if (self.button_clicked != "" ):
                for key,value in self.game_buttons.items():
                    if(self.button_clicked == value):
                        self.game_obj.current_link = key
                        change_page_by_action = True
                        break

            if self.on_press_delay_control():
                self.button_clicked = ""
                change_page_by_action = False

            change_page_by_event = self.game_obj.game_events_handler()

            if change_page_by_action or change_page_by_event:
                break

            pygame.display.update()
            