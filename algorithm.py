from mazes import print_maze
from colorama import Fore, Style
from copy import deepcopy
import time
import os


class Algorithm:
    
    def get_solution_path(self, node):
        current_node = node
        while current_node.parent != None:
            self.colored_print(Fore.LIGHTCYAN_EX, "C A M I N O   E N   R E V E R S A")
            print_maze(current_node.state.map, current_node.state.cols_size)
            time.sleep(0.1)
            green_path = current_node.state.get_green_path()
            current_node = current_node.parent
            for green_coord in green_path:
                current_node.state.map[green_coord[0]][green_coord[1]] = "🟩"
        self.colored_print(Fore.LIGHTCYAN_EX, "C A M I N O   E N   R E V E R S A")
        print_maze(current_node.state.map, current_node.state.cols_size)


    def is_state_on_reached(self, test_state, reached):
        for state in reached:
            if state.map == test_state.map:
                return True
        return False

    def colored_print(self, color, text):
        os.system("clear")
        print(color)
        print(text)
        print(Style.RESET_ALL)

    def print_maze_map(self, mapa, cols):
        os.system("clear")
        print_maze(mapa, cols)

    def print_checked_map(self, state, reached):
        # Primero hacemos una copia del mapa para no modificar el original.
        copied_map = deepcopy(state.map)
        # Creamos lista para guardar las coordenadas del agente del mapa que entra.
        green_coords = state.get_green_path()
        # Recorremos todos los estados ya alcanzados.
        for state in reached:
            agent_coords = state.agent_coordinates
            copied_map[agent_coords[0]][agent_coords[1]] = self.reached_color
        for coord in green_coords:
            copied_map[coord[0]][coord[1]] = self.agent_color
        print_maze(copied_map, state.cols_size)