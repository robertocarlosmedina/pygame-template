__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
import os
from src.support.font import Game_fonts as fonts
from src.support.colors import Game_color as color
from src.support.buttons import verticalButtonsDisplay
from src.support.auxiliar_functions import draw_header_styled_lines, \
    read_from_file, get_screen_text

class Game_over:

    game_buttons :list
    button_clicked :str
    mouse_position :tuple
    menu_tittles :dict
    menus_start_positions :dict
    buttons_size :dict
    game_data :list
    delay: int

    def __init__(self, game_obj) -> None:
        self.game_object = game_obj
        self.button_clicked = ""
        self.y_pos = 390
        self.game_data = read_from_file("data/end_game_values.txt", "r")[0].split(" ")
        self.delay = 0
        self.game_buttons = {
            "game_loop": "New Game",
            "game_menu": "Main Menu",
            "game_quit":"Quit"
        }

        self.buttons_size = {
            "x":220,
            "y":50
        }
        self.menus_start_positions = {
            "game_menu":{
                "x": int(self.game_object.screen_size[0]/2 - self.buttons_size["x"]/2),
                "y":190
            }
        }
    
    def menu_buttons(self) -> None:
        font_size = pygame.font.Font.size(fonts.montserrat_size_22.value, get_screen_text("game_result_text"))
        line = fonts.montserrat_size_22.value.render(get_screen_text("game_result_text"), True, color.white_1.value)
        self.game_object.screen.blit(
            line, 
            (self.menus_start_positions["game_menu"]["x"]-(font_size[0]/2)+(self.buttons_size["x"]/2),
                self.menus_start_positions["game_menu"]["y"]-font_size[1]*2)
        )

        self.button_clicked = verticalButtonsDisplay(
            screen = self.game_object.screen,
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
    
    def draw_game_results(self) -> None:

        # Winner display
        font_size = pygame.font.Font.size(fonts.montserrat_size_18.value, get_screen_text("game_win_text"))
        line = fonts.montserrat_size_18.value.render(get_screen_text("game_win_text"), True, color.green.value)
        self.game_object.screen.blit(line, (self.game_object.screen_size[0]/2 - font_size[0]/2, self.y_pos))

        # Loser Display
        # line = fonts.montserrat_size_18.value.render(get_screen_text("game_lost_text"), True, color.red.value)
        # self.game_object.screen.blit(line, (519, self.y_pos + 55))

    def on_press_delay_control(self) -> bool:
        if self.delay > 10:
            return False

        self.delay += 1
        return True

    def run_link(self) -> str:
        change_page_by_event = change_page_by_action = False

        while True:
            self.game_object.screen_fill_bg()
            self.mouse_pos = pygame.mouse.get_pos()

            font_size = pygame.font.Font.size(fonts.montserrat_size_30.value, get_screen_text("game_tittle"))
            line = fonts.montserrat_size_30.value.render(get_screen_text("game_tittle"), True, color.red_2.value)
            self.game_object.screen.blit(line, (self.game_object.screen_size[0]/2-(font_size[0]/2), 25))

            draw_header_styled_lines(self.game_object.screen, self.game_object.screen_size)

            self.menu_buttons()
            self.draw_game_results()

            if (self.button_clicked != "" ):
                for key,value in self.game_buttons.items():
                    if(self.button_clicked == value):
                        self.game_object.current_link = key
                        change_page_by_action = True
                        break

            if self.on_press_delay_control():
                self.button_clicked = ""
                change_page_by_action = False

            change_page_by_event = self.game_object.game_events_handler()

            if change_page_by_action or change_page_by_event:
                break

            pygame.display.update()
