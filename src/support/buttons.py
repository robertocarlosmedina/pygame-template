__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

import pygame
from src.support.colors import Game_color as color


def verticalButtonsDisplay(screen :pygame.Surface, buttons :list, start_position :dict, 
                            box_dim :dict, mouse_pos :list, font :pygame.font, button_clicked :str) -> str:

    for button in buttons:
        font_size = pygame.font.Font.size(font, button)
        button_box = pygame.Rect(start_position["x"], start_position["y"], box_dim["x"], box_dim["y"])

        mouse_click = pygame.mouse.get_pressed(3)
        
        if mouse_pos[0]in range(start_position["x"], start_position["x"]+box_dim["x"]) and \
           mouse_pos[1] in range(start_position["y"], start_position["y"]+box_dim["y"])\
           and mouse_click[0] == 1:
            button_clicked = button

        # hover button effect
        if mouse_pos[0] in range(start_position["x"], start_position["x"]+box_dim["x"]) and \
           mouse_pos[1] in range(start_position["y"], start_position["y"]+box_dim["y"]):
            pygame.draw.rect(screen, color.grey.value, button_box, border_radius = 10)
            line = font.render(button, True, color.white.value)

        else:
            pygame.draw.rect(screen, color.blue.value, button_box, 2, 10)
            line = font.render(button, True, color.blue.value)
        
        if button_clicked == button:
            pygame.draw.rect(screen, color.green.value, button_box, border_radius = 10)
            line = font.render(button, True, color.black.value)

        screen.blit(
            line, 
            (start_position["x"]-(font_size[0]/2)+(box_dim["x"]/2),
                start_position["y"]-(font_size[1]/2)+(box_dim["y"]/2))
        )
        start_position["y"] += (box_dim["y"] + 10)

    return button_clicked


def horizontalButtonDisplay(screen :pygame.Surface, buttons :list, start_position :dict, 
                            box_dim :dict, mouse_pos :list, font :pygame.font, button_clicked :str) -> str:

    for button in buttons:
        font_size = pygame.font.Font.size(font, button)
        button_box = pygame.Rect(start_position["x"], start_position["y"], box_dim["x"], box_dim["y"])

        mouse_click = pygame.mouse.get_pressed(3)
        if mouse_pos[0]in range(start_position["x"], start_position["x"]+box_dim["x"]) and \
           mouse_pos[1] in range(start_position["y"], start_position["y"]+box_dim["y"])\
           and mouse_click[0] == 1:
            button_clicked = button

        # hover button effect
        if mouse_pos[0] in range(start_position["x"], start_position["x"]+box_dim["x"]) and \
           mouse_pos[1] in range(start_position["y"], start_position["y"]+box_dim["y"]):
            pygame.draw.rect(screen, color.grey.value, button_box, border_radius = 10)
            line = font.render(button, True, color.white.value)

        else:
            pygame.draw.rect(screen, color.blue.value, button_box, 2, 10)
            line = font.render(button, True, color.blue.value)
        
        if button_clicked == button:
            pygame.draw.rect(screen, color.green.value, button_box, border_radius = 10)
            line = font.render(button, True, color.black.value)

        screen.blit(
            line, 
            (start_position["x"]-(font_size[0]/2)+(box_dim["x"]/2),
                start_position["y"]-(font_size[1]/2)+(box_dim["y"]/2))
        )
        start_position["x"] += (box_dim["x"] + 10)

    return button_clicked
    