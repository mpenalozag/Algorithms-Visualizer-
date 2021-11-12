from maze_foundations import Node
from collections import deque
import time
import os
from colorama import Fore, Style, Back
from copy import deepcopy

from mazes import print_maze

class BFS:

    agent_color = "🟩"
    reached_color = "🟦"
    expanded_color = "🟨"
    used_path = "🟥"

    def __init__(self, problem):
        self.problem = problem
        self.answer = self.apply_algorithm()

    def apply_algorithm(self):
        """
        Retorna el nodo objetivo o retorna que no hay solución.
        """
        # Creamos el nodo inicial, que contiene el estado inicial del problema.
        node = Node(deepcopy(self.problem.initial_state), None)
        # Si el nodo inicial es la solución, retornamos el nodo.
        if self.problem.goal_state.map == node.state.map:
            return node
        # Creamos la frontera, que será una cola FIFO de nodos.
        frontier = deque()
        # Agregamos el nodo inicial a la frontera
        frontier.append(node)
        # Creamos lista reached, con todos los estados que ya alcanzamos.
        reached = []
        reached.append(node.state)
        
        # Mientras existan elementos en la frontera.
        while len(frontier) > 0:
            # Tomamos el nodo de mas antiguedad en la frontera (lógica FIFO)
            node = frontier.popleft()
            self.colored_print(Fore.LIGHTYELLOW_EX, "B R E A D T H   F I R S T   S E A R C H   W O R K I N G")
            self.print_checked_map(node.state, reached)
            #print_maze(node.state.map, node.state.cols_size)
            time.sleep(0.3)
            # Recorremos los hijos del nodo.
            childs = node.expand()
            for child in childs:
                if child.state.map == self.problem.goal_state.map:
                    self.print_maze_map(child.state.map, node.state.cols_size)
                    self.get_solution_path(child)
                    return child
                if not self.is_state_on_reached(child.state, reached):
                    reached.append(child.state)
                    frontier.append(child)
        # Retornamos fallo en la búsqueda de una solución.
        print("This maze has no solution!")
        return False

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
