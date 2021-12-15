__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
    Class of all the links on the game.
    It's possible to create a new link and call it from the main file.
    To take in consideration that the link is made by a method of this class.
"""

from src.pages.pause_menu import Game_Pause_Menu
from src.pages.game_over import Game_over
from src.game_components.game import Game_loop
from src.pages.start import Game_start
from src.pages.menu import Game_menu
from src.pages.quit import Game_quit
from src.pages.credits import Game_Credits


class Game_links:

    game_page_object :object   # Store an object of the class that represent the current page
    game_backup :object        # Store a backup object from the game loop class
                                    # what allow's us to return back to the game exacty the same 
                                    # as when we pause it.

    def __init__(self) -> None:
        self.game_page_object = object
        self.game_backup = object

    def start_game(self, game_obj: object) -> str:
        """
            Method of the Start page link.
        """
        self.game_page_object = Game_start(game_obj)
        self.game_page_object.run_link()

    def game_main_menu(self, game_obj: object) -> str:
        """
            Method of the Main Menu page link.
        """
        self.game_page_object = Game_menu(game_obj)
        self.game_page_object.run_link()

    def continue_game(self, game_obj) -> str:
        """
            Method of the Continue Game page link.
            If we have a backup we use the backup, and
            if not we create a new instance of the class Game_loop
        """
        game_obj.current_link = "game_loop"
        if(isinstance(self.game_backup, Game_loop)):
            self.game_page_object = self.game_backup
        else:
            self.game_page_object = Game_loop(game_obj)

        self.game_page_object.run_link()

    def gameplay_loop(self, game_obj: object) -> str:
        """
            Method of the Game loop page link.
        """
        self.game_page_object = Game_loop(game_obj)
        self.game_page_object.run_link()
        self.game_backup = self.game_page_object

    def game_credits(self, game_obj: object) -> str:
        """
            Method of the Credits page link.
        """
        self.game_page_object = Game_Credits(game_obj)
        self.game_page_object.run_link()

    def game_quit(self, game_obj: object) -> str:
        """
            Method of the Quit page link.
        """
        self.game_page_object = Game_quit(game_obj)
        self.game_page_object.run_link()

    def game_pause_menu(self, game_obj: object) -> str:
        """
            Method of the Pause Menu page link.
        """
        self.game_page_object = Game_Pause_Menu(game_obj)
        self.game_page_object.run_link()

    def game_over(self, game_obj: object) -> str:
        """
            Method of the Game Over page link.
        """
        self.game_backup = object
        self.game_page_object = Game_over(game_obj)
        self.game_page_object.run_link()
