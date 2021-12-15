

import pygame
from src.support.colors import Game_color as color
from src.support.font import Game_fonts as font

CURSOR_DELAY = 10
delay_controler = 0

def draw_input_boxes(screen: pygame.Surface, input_boxes: dict, input_limit: int, events: pygame.event, mouse_pos: tuple,
    y_start: int, x_start: int, boxes_dim: tuple, space_between_box, place_holder = "Click to write a ", 
    box_value_font = font.montserrat_size_18.value, box_header_text_font = font.montserrat_size_14.value, 
    cursor_color = color.white_1.value, not_filled_error_color = color.green.value, filled_success_color = color.red_2.value,
    active_box_color = color.white.value, unactive_box_color = color.grey.value, place_hodel_color = color.grey.value,
    border = 10) -> dict:
    """
        Method to control and draw all the information about the input boxes.
        Their state and their content.
    """
    for key, box_info in input_boxes.items():
        click = pygame.mouse.get_pressed(3)

        # Writing the box name on the screen
        if box_info[0] != '':
            box_text_surface = box_header_text_font.render(key.capitalize(), True, not_filled_error_color)

            # Bliting the text in the center of the box
            info_text_surface = box_value_font.render(input_boxes[key][0], True, (255, 255, 255))
            size_info = pygame.font.Font.size(box_value_font, input_boxes[key][0])
            screen.blit(info_text_surface, (x_start + boxes_dim[0]/2 - size_info[0]/2, y_start + boxes_dim[1]/2 - size_info[1]/2,))

            # Display the cursor in the box
            if box_info[1] : # and delay_controler >= CURSOR_DELAY:
                pygame.draw.line(screen, cursor_color, (x_start+boxes_dim[0]/2 + size_info[0]/2 , y_start + 10),\
                                    (x_start+boxes_dim[0]/2 + size_info[0]/2, y_start + 30), 3)
            #     delay_controler = 0
            # else:
            #     delay_controler += 1

        else:
            box_text_surface = box_header_text_font.render(key.capitalize(), True, filled_success_color)

        size = pygame.font.Font.size(box_header_text_font, key.capitalize())
        screen.blit(box_text_surface, (x_start + boxes_dim[0]/2 - size[0]/2,y_start - 25))

        # Control if mouse pressed on the box, to active it 
        if mouse_pos[0] in range(x_start, x_start + boxes_dim[0]) and mouse_pos[1] in range(y_start, y_start + boxes_dim[1])\
            and click[0] == 1:
            input_boxes[key][1] = True

        elif (mouse_pos[0] not in range(x_start, x_start+boxes_dim[0]) or mouse_pos[1] not in range(y_start, y_start + boxes_dim[1]))\
            and click[0] == 1:
            input_boxes[key][1] = False

            # Putting the other box's in state False
            for key1 in input_boxes.keys():
                if key1 != key:
                    input_boxes[key1][1] = False

        # Draw the box according to his state (True or False)
        pygame.draw.rect(screen, active_box_color, pygame.Rect(x_start, y_start, boxes_dim[0], boxes_dim[1]), 2, border_radius = border) \
            if box_info[1] else pygame.draw.rect(screen, unactive_box_color, pygame.Rect(x_start, y_start, boxes_dim[0], boxes_dim[1]), 2, \
                border_radius = border)
        
        # Writing the place holder in the box
        if box_info[0] == '' and not box_info[1]:
            text_surface = box_header_text_font.render(place_holder + key, True, place_hodel_color)
            size = pygame.font.Font.size(box_header_text_font, place_holder+key)
            screen.blit(text_surface, (x_start + boxes_dim[0]/2 - size[0]/2, y_start + boxes_dim[1]/2 - size[1]/2))

        # Adding some space between the box's
        y_start += space_between_box

        # Checking the events and adding the text to the variable
        for event in events:
            if event.type == pygame.KEYDOWN and box_info[1]:
                if event.key==pygame.K_BACKSPACE:
                    input_boxes[key][0] = input_boxes[key][0][:-1]
                elif event.key==pygame.K_SPACE:
                    pass
                elif((len(input_boxes[key][0])<=input_limit)):
                    input_boxes[key][0] += event.unicode
    
    return input_boxes


def verify_input(input_boxes: dict) -> bool:
    """
        Method that verify if all the inputs are filled.
    """
    for value in input_boxes.values():
        if value[0] == "" or value[0] == " " or len(value[0])<2:
            return False
    return True
