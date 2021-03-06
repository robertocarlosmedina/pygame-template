__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
    This file contain some method's that can be use to draw an list of buttons on the screen.
    It can be done both in Horizontal and Vertical.
    And it is possible to declare more styled buttons to.
"""

import pygame
from src.support.colors import Game_color as color


def verticalButtonsDisplay(screen :pygame.Surface, buttons :list, start_position :dict, 
        box_dim :dict, mouse_pos :list, font :pygame.font, button_clicked :str, border = 10, 
        select_color = color.green.value, hover_color = color.grey.value, 
        button_color = color.blue.value, fill_box = 2, text_color = color.blue.value,
        hover_text_color = color.white.value, select_text_color = color.black.value) -> str:
    """
        Method to draw Vertical buttons on the screen.
        Given a list, and some proper style in the params, this draw the buttons
        and also make hover efect on them. And if one button is clicked on that list it return it's
        value.
    """

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
            pygame.draw.rect(screen, hover_color, button_box, border_radius = border)
            line = font.render(button, True, hover_text_color)

        else:
            pygame.draw.rect(screen, button_color, button_box, fill_box, border)
            line = font.render(button, True, text_color)
        
        if button_clicked == button:
            pygame.draw.rect(screen, select_color, button_box, border_radius = border)
            line = font.render(button, True, select_text_color)

        screen.blit(
            line, 
            (start_position["x"]-(font_size[0]/2)+(box_dim["x"]/2),
                start_position["y"]-(font_size[1]/2)+(box_dim["y"]/2))
        )
        start_position["y"] += (box_dim["y"] + 10)

    return button_clicked


def horizontalButtonDisplay(screen :pygame.Surface, buttons :list, start_position :dict, 
        box_dim :dict, mouse_pos :list, font :pygame.font, button_clicked :str, border = 10, 
        select_color = color.green.value, hover_color = color.grey.value, 
        button_color = color.blue.value, fill_box = 2, text_color = color.blue.value,
        hover_text_color = color.white.value, select_text_color = color.black.value) -> str:
    """
        Method to draw Horizontal buttons on the screen.
        Given a list, and some proper style in the params, this draw the buttons
        and also make hover efect on them. And if one button is clicked on that list it return it's
        value.
    """

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
            pygame.draw.rect(screen, hover_color, button_box, border_radius = border)
            line = font.render(button, True, hover_text_color)

        else:
            pygame.draw.rect(screen, button_color, button_box, fill_box, border)
            line = font.render(button, True, text_color)
        
        if button_clicked == button:
            pygame.draw.rect(screen, select_color, button_box, border_radius = border)
            line = font.render(button, True, select_text_color)

        screen.blit(
            line, 
            (start_position["x"]-(font_size[0]/2)+(box_dim["x"]/2),
                start_position["y"]-(font_size[1]/2)+(box_dim["y"]/2))
        )
        start_position["x"] += (box_dim["x"] + 10)

    return button_clicked
    