

import pygame
from src.support.colors import Game_color as color

def draw_input_boxes(screen, input_boxes, input_limit, events, mouse_pos, y_start, x_start, boxes_dim, 
    space_between_box, place_holder = "Click and write") -> dict:

    
    for key, box_info in input_boxes.items():
        # getting the mouse click
        click = pygame.mouse.get_pressed(3)

        # Writing the boxx name on the screen
        if box_info[0] != '':
            box_text_surface = pygame.font.SysFont("arial", 12).render(key, True, color.green.value)

            # bliting the text in the center of the box
            info_text_surface = pygame.font.SysFont("arial", 20).render(input_boxes[key][0], True, (255, 255, 255))
            size_info = pygame.font.Font.size(pygame.font.SysFont("arial", 20), input_boxes[key][0])
            screen.blit(info_text_surface, (x_start+boxes_dim[0]/2 - size_info[0]/2, y_start + 12))

            # Display the cursor in the box
            if box_info[1]:
                pygame.draw.line(screen, color.grey_1.value, (x_start+boxes_dim[0]/2 + size_info[0]/2 , y_start + 10),\
                                    (x_start+boxes_dim[0]/2 + size_info[0]/2, y_start + 30), 2)
        else:
            box_text_surface = pygame.font.SysFont("arial", 12).render(key, True, color.red_2.value)

        size = pygame.font.Font.size(pygame.font.SysFont("arial", 12), key)
        screen.blit(box_text_surface, (x_start+boxes_dim[0]/2-size[0]/2,y_start-15))

        # control if mouse pressed on the box, to active it 
        if mouse_pos[0] in range(x_start, x_start+boxes_dim[0]) and mouse_pos[1] in range(y_start, y_start+boxes_dim[1])\
            and click[0] == 1:
            input_boxes[key][1] = True

        elif (mouse_pos[0] not in range(x_start, x_start+boxes_dim[0]) or mouse_pos[1] not in range(y_start, y_start+boxes_dim[1]))\
            and click[0] == 1:
            input_boxes[key][1] = False

            # putting the other box's in state False
            for key1 in input_boxes.keys():
                if key1 != key:
                    input_boxes[key1][1] = False

        # drawing the box accordin to his state (True or False)
        pygame.draw.rect(screen, color.white.value, pygame.Rect(x_start, y_start, boxes_dim[0], boxes_dim[1]), 2) if box_info[1]\
            else pygame.draw.rect(screen, color.grey.value, pygame.Rect(x_start, y_start, boxes_dim[0], boxes_dim[1]), 2)
        
        # Writing the place holder in the box
        if box_info[0] == '' and not box_info[1]:
            text_surface = pygame.font.SysFont("arial", 12).render(place_holder+key, True, color.grey_1.value)
            size = pygame.font.Font.size(pygame.font.SysFont("arial", 12), place_holder+key)
            screen.blit(text_surface, (x_start+boxes_dim[0]/2 - size[0]/2,y_start + 15))

        # adding some space between the box's
        y_start += space_between_box

        # checking the events and adding the text to the variable
        for event in events:
            if event.type == pygame.KEYDOWN and box_info[1]:
                if event.key==pygame.K_BACKSPACE:
                    input_boxes[key][0] = input_boxes[key][0][:-1]
                elif event.key==pygame.K_SPACE:
                    pass
                elif((len(input_boxes[key][0])<=input_limit)):
                    input_boxes[key][0] += event.unicode
    
    return input_boxes

# Method that verify all the inputs
def verifyInput(input_boxes):
    for value in input_boxes.values():
        if value[0] == "" or value[0] == " " or len(value[0])<2:
            return False
    return True