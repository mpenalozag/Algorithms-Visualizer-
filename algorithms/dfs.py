from collections import deque
from foundations import Node
from colorama import Fore, Back, Style
from mazes import print_maze
from algorithms.algorithm import Algorithm


import time
import os
from copy import deepcopy


class DFS(Algorithm):
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
            self.print_checked_map(node.state, reached, frontier)
            time.sleep(0.3)
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