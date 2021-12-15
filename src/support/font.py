__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.1.5"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

from enum import Enum
import pygame

"""
    Class that contain all the fonts used in the game.
"""

class Game_fonts(Enum):
    pygame.init()
    
    montserrat_size_50 = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 40)
    montserrat_size_40 = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 40)
    montserrat_size_30 = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 30)
    montserrat_size_20 = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 20)
    montserrat_size_22 = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 22)
    montserrat_size_18 = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 18)
    montserrat_size_16 = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 16)
    montserrat_size_14 = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 14)
    montserrat_size_12 = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 12)
    montserrat_size_8 = pygame.font.Font("assets/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 8)
    