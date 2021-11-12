from collections import deque
from maze_foundations import Node
from colorama import Fore, Back, Style
from mazes import print_maze
import time
import os


class DFS:
    def __init__(self, problem):
        self.problem = problem
        self.answer = self.apply_algorithm()

    def apply_algorithm(self):
        # Creamos la frontera. La frontera tiene una lógica LIFO (Last in First out).
        frontier = deque()
        # Agregamos un nodo inicial, con el estado inicial, a la frontera.
        node = Node(self.problem.initial_state, None)
        frontier.append(node)
        reached = [node.state]
        
        # Mientras hayan nodos en la frontera.
        while len(frontier) > 0:
            # Sacamos el último nodo agregado.
            node = frontier.popleft()
            self.colored_print(Fore.LIGHTYELLOW_EX, "D E P T H   F I R S T   S E A R C H   W O R K I N G")
            print_maze(node.state.map, node.state.cols_size)
            time.sleep(0.4)
            # Si es que el nodo actual es la solución, retornamos el nodo.
            if self.problem.goal_state.map == node.state.map:
                self.get_solution_path(node)
                return node
            # Recorremos cada hijo del nodo que estamos observando.
            for child in node.expand():
                # Agregamos cada hijo al principio de la cola.
                if not self.is_state_on_reached(child.state, reached):
                    reached.append(child.state)
                    frontier.appendleft(child)
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
        #os.system("clear")
        print(color)
        print(text)
        print(Style.RESET_ALL)