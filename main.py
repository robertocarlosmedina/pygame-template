__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.1.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
    Main file for the template.
    This is where the main loop starts.
    And from here according to the page that the player are it will be to the main
    loop of that page.
"""

from src.support.game_links import Game_links as Link
from src.support.game_configurations import Game

game_links: dict            # To store all the links an possible page to go on the game

links = Link()

# To add a new link here, it's necessary to declare that link in the Game_links class
# and the creating a new element to this dict, in whitch the Id of the element, will
# be the name of the link, and the value will be the method to call relative to link.
# And then to call the page it just call the function like this:
# game_links["name_of_the_link"](game)
game_links = {
    "game_start": links.start_game,
    "game_menu": links.game_main_menu,
    "game_loop": links.gameplay_loop,
    "game_quit": links.game_quit,
    "game_credits": links.game_credits,
    "game_continue": links.continue_game,
    "game_pause_menu": links.game_pause_menu,
    "game_over": links.game_over
}

game = Game()
# game.current_link = "game_menu"

while True:
    """
        Main Loop of the game.
    """
    game_links[game.current_link](game)
    print("Current path: ", game.current_link)
