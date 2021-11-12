from collections import deque
from maze_foundations import Node

class DFS:
    def __init__(self, problem):
        self.problem = problem
        self.answer = self.apply_algorithm()

    def apply_algorithm(self):
        # Creamos la frontera. La frontera tiene una lógica LIFO (Last in First out).
        frontier = deque()
        # Agregamos un nodo inicial, con el estado inicial, a la frontera.
        node = Node(self.problem.state, None)
        frontier.append(node)
        result = False
        while len(frontier) > 0:
            node = frontier.pop(-1)
            if self.problem.goal_state.map == node.state.map:
                return node
            