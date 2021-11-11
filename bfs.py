from maze_foundations import Node
from collections import deque
import time
import os
from colorama import Fore, Style, Back

from mazes import print_maze

class BFS:
    def __init__(self, problem):
        self.problem = problem
        self.answer = self.apply_algorithm()

    def apply_algorithm(self):
        """
        Retorna el nodo objetivo o retorna que no hay solución.
        """
        # Creamos el nodo inicial, que contiene el estado inicial del problema.
        node = Node(self.problem.initial_state, None)
        # Si el nodo inicial es la solución, retornamos el nodo.
        if self.problem.goal_state.map == node.state.map:
            return node
        # Creamos la frontera, que será una cola FIFO de nodos.
        frontier = deque()
        # Agregamos el nodo inicial a la frontera
        frontier.append(node)
        # Creamos lista reached, con todos los estados que ya alcanzamos.
        reached = []
        reached.append(node.state.map)
        
        # Mientras existan elementos en la frontera.
        while len(frontier) > 0:
            # Tomamos el nodo de mas antiguedad en la frontera (lógica FIFO)
            node = frontier.popleft()
            os.system("clear")
            print(Fore.LIGHTYELLOW_EX)
            print("B R E A D T H   F I R S T   S E A R C H   W O R K I N G")
            print(Style.RESET_ALL)
            print_maze(node.state.map, node.state.cols_size)
            time.sleep(0.2)
            # Recorremos los hijos del nodo.
            for child in node.expand():
                if child.state.map == self.problem.goal_state.map:
                    os.system("clear")
                    print_maze(child.state.map, node.state.cols_size)
                    self.get_solution_path(child)
                    return child
                if child.state.map not in reached:
                    reached.append(child.state.map)
                    frontier.append(child)
        # Retornamos fallo en la búsqueda de una solución.
        print("This maze has no solution!")
        return False

    def get_solution_path(self, node):
        current_node = node
        while current_node.parent != None:
            os.system("clear")
            print(Fore.LIGHTCYAN_EX)
            print("C A M I N O   E N   R E V E R S A")
            print(Style.RESET_ALL)
            print_maze(current_node.state.map, current_node.state.cols_size)
            time.sleep(0.1)
            green_path = current_node.state.get_green_path()
            current_node = current_node.parent
            for green_coord in green_path:
                current_node.state.map[green_coord[0]][green_coord[1]] = "🟩"
        os.system("clear")
        print(Fore.LIGHTCYAN_EX)
        print("C A M I N O   E N   R E V E R S A")
        print(Style.RESET_ALL)
        print_maze(current_node.state.map, current_node.state.cols_size)

    def color_closed_path(self, child):
        current_node = child
        while current_node.parent != None:
            agent_coords = child.state.agent_coordinates
            child.state.map[agent_coords[0]][agent_coords[1]] = child.used_path
            print_maze(child.state.map, child.state.cols_size)
            time.sleep(1)
            current_node = current_node.parent