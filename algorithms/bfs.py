from foundations import Node
from collections import deque
import time
import os
from colorama import Fore, Style, Back
from copy import deepcopy
from algorithms.algorithm import Algorithm

class BFS(Algorithm):
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
            self.print_checked_map(node.state, reached, frontier)
            time.sleep(0.2)
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

    
