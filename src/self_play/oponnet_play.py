__author__ = "Roberto Medina"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

"""
"""

class Hamiltonian_Algorithm:

    counter :int
    algorithm_type :str
    table_info :dict
    possible_move :list
    previus_move :str
    snake_step :int

    def __init__(self, algorithm_type :str, table_info :dict, snake_step :int) -> None:
        self.counter = 0
        self.algorithm_type = algorithm_type
        self.table_info = table_info
        self.snake_step = snake_step
        self.previus_move = ""
        self.aux = 0
        self.setup_possible_moves()
    
    def setup_possible_moves(self):
        if(self.algorithm_type == "hamiltonian_horizontal"):
            self.possible_move = {
                "up": {
                    "right": [
                        self.table_info["x_position"], 
                        self.table_info["x_position"] + self.snake_step*2,
                        self.table_info["y_position"] ,
                        self.table_info["y_position"] + self.table_info["height"],
                    ],
                    "left": [
                        self.table_info["x_position"] + self.table_info["widht"] - self.snake_step*5,
                        self.table_info["x_position"] + self.table_info["widht"] - self.snake_step,
                        self.table_info["y_position"] ,
                        self.table_info["y_position"] + self.table_info["height"],
                    ]
                }, 
                "left": {
                    "up": [
                        self.table_info["x_position"],
                        self.table_info["x_position"] + self.snake_step*2,
                        self.table_info["y_position"] ,
                        self.table_info["y_position"] + self.table_info["height"],
                    ]

                }, 
                "down": {
                    "left": [
                        self.table_info["x_position"] + self.table_info["widht"] - self.snake_step*2,
                        self.table_info["x_position"] + self.table_info["widht"] ,
                        self.table_info["y_position"] + self.table_info["height"] - self.snake_step*2,
                        self.table_info["y_position"] + self.table_info["height"],
                    ]
                },
                "right": {
                    "down": [
                        self.table_info["x_position"] + self.table_info["widht"] - self.snake_step*2,
                        self.table_info["x_position"] + self.table_info["widht"],
                        self.table_info["y_position"],
                        self.table_info["y_position"] + self.snake_step,
                    ],
                    "up": [
                        self.table_info["x_position"] + self.table_info["widht"] - self.snake_step*3,
                        self.table_info["x_position"] + self.table_info["widht"] - self.snake_step*2,
                        self.table_info["y_position"] + self.snake_step*2,
                        self.table_info["y_position"] + self.table_info["height"],
                    ]
                },
            }

    def execute_algorithm(self, snake_head_position :dict, current_direction :str):
        for key,values in self.possible_move[current_direction].items():
            if(snake_head_position["x"] in range(values[0], values[1]) and snake_head_position["y"] in range(values[2], values[3])):
                return key

        return ""
