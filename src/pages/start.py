__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.1.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"
__file__ = "start.py"
__path__ = "https://github.com/robertocarlosmedina/pygame-template"

"""
    This class represent a smood animation on the beginning of the game.
"""

import pygame
from src.support.colors import Game_color as color
from src.support.auxiliar_functions import get_screen_text
from src.support.font import Game_fonts as font


class Game_start:

    def __init__(self, game_obj: object):
        self.delay = self.highCircle  = self.count = 0
        self.game_object = None
        self.game_object = game_obj
    
    def draw_screen_text(self) -> None:
        # drawing tittle
        size = pygame.font.Font.size(font.montserrat_size_50.value, get_screen_text("game_tittle"))
        line = font.montserrat_size_50.value.render(get_screen_text("game_tittle"), True, color.red_2.value)
        self.game_object.screen.blit(line, (self.game_object.screen_size[0]/2 - size[0]/2, (self.game_object.screen_size[1]/2 - size[1]/2) - 40))
        # drawing sub tittle
        size = pygame.font.Font.size(font.montserrat_size_12.value, get_screen_text("game_subtittle"))
        line = font.montserrat_size_12.value.render(get_screen_text("game_subtittle"), True, color.white.value)
        self.game_object.screen.blit(line, (self.game_object.screen_size[0]/2 - size[0]/2, (self.game_object.screen_size[1]/2 - size[1]/2) - 10))

        # drawing tittle bottom info
        size = pygame.font.Font.size(font.montserrat_size_8.value, f'Made by {__author__}')
        line = font.montserrat_size_8.value.render(f'Made by {__author__}', True, color.white.value)
        self.game_object.screen.blit(line, (self.game_object.screen_size[0]/2 - size[0]/2, 440))
        # drawing tittle bottom info
        size = pygame.font.Font.size(font.montserrat_size_8.value, f'{__email__}')
        line = font.montserrat_size_8.value.render(f'{__email__}', True, color.white.value)
        self.game_object.screen.blit(line, (self.game_object.screen_size[0]/2 - size[0]/2, 450))
         # drawing tittle bottom info
        size = pygame.font.Font.size(font.montserrat_size_8.value, f'{__path__}')
        line = font.montserrat_size_8.value.render(f'{__path__}', True, color.white.value)
        self.game_object.screen.blit(line, (self.game_object.screen_size[0]/2 - size[0]/2, 460))

    # Method that control this class
    def run_link(self):
        while True:
            self.game_object.screen_fill_bg()
            self.draw_screen_text()
            self.animation()

            # Controling if the process of drawing runned 6 times to pass this start page
            if self.count >= 3:    
                self.game_object.current_link = "game_menu"
                break

            if self.game_object.game_events_handler():
                break
            
            pygame.display.update()

    # Method that control the circle animation display and the time 
    def animation(self):
        """
            Method to draw the circle and handle their state (min, average, max).
            And depending on their state draw them on the screen.
        """
        
        pos_x, pos_y = int(self.game_object.screen_size[0]/2), int(self.game_object.screen_size[1]/2)+20
        for i in range(0, 7):
            if i == self.highCircle:
                pygame.draw.circle(self.game_object.screen, color.red.value, (pos_x - 60, pos_y), 6)
            elif i == self.highCircle + 1:
                pygame.draw.circle(self.game_object.screen, color.red_1.value, (pos_x - 60, pos_y), 3)
            elif i == self.highCircle - 1:
                pygame.draw.circle(self.game_object.screen, color.red_1.value, (pos_x - 60, pos_y), 3)
            else:
                pygame.draw.circle(self.game_object.screen, color.red_1.value, (pos_x - 60, pos_y), 2)
            pos_x +=20

        # Controling the delay to change the higher circle
        if self.delay >= 5:
            self.highCircle += 1
            self.delay = 0
        self.delay += 1

        # COntroling the if the higher  circle is in the end to return it to the start
        if self.highCircle > 7:
            self.highCircle = 0
            self.count += 1
