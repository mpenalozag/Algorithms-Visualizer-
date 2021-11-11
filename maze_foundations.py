# En este archivo tendremos las cosas básicas que necesitamos
# para poder aplicar nuestros algoritmos de manera efectiva.

# En primer lugar necesitamos tener nodos. Un nodo representa un estado en el universo.
from mazes import print_maze
from copy import deepcopy


class Node:
    """
    State:
        En un laberinto el estado de cada nodo sería el laberinto entero.
        La diferencia entre cada estado estaría en la posición del agente.
    """

    agent_color = "🟩"
    reached_color = "🟦"
    expanded_color = "🟨"
    used_path = "🟥"

    def __init__(self, state, parent):
        self.state = state
        self.reached = False
        self.expanded = False
        self.parent = parent
        self.reached_nodes = []

    def expand(self):
        """
        Retorna una lista con todos los nodos que pueden ser alcanzados al 
        expandir el nodo actual.
        """
        nodes = []
        possible_states = self.get_possible_states()
        for state in possible_states:
            node = Node(state, self)
            nodes.append(node)

        return nodes

    def get_possible_states(self):
        """
        Función que consigue todos los posibles estados que puedo alcanzar 
        desde el nodo actual.
        """
        possible_moves = self.get_possible_moves()
        
        states = []
        new_map = deepcopy(self.state.map)    
        new_map[self.state.agent_coordinates[0]][self.state.agent_coordinates[1]] = "  "
        for move in possible_moves:
            other_map = deepcopy(new_map)
            other_map[move[0]][move[1]] = self.agent_color
            new_state = State(other_map, move, self.state.rows_size, self.state.cols_size)
            states.append(new_state)

        return states

    def get_possible_moves(self):
        possible_moves = []
        x = self.state.agent_coordinates[0]
        y = self.state.agent_coordinates[1]

        # Revisamos movimientos hacia arriba
        if x - 1 >= 0 and self.move_is_valid((x-1, y), "up"):
            possible_moves.append((x-1, y))
        # Revisamos movimientos hacia abajo
        if x + 1 < self.state.rows_size and self.move_is_valid((x+1, y), "down"):
            possible_moves.append((x+1, y))
        # Revisamos movimientos hacia la izquierda
        if y - 1 >= 0 and self.move_is_valid((x, y-1), "left"):
            possible_moves.append((x, y-1))
        # Revisamos movimientos hacia la derecha 
        if y + 1 < self.state.cols_size and self.move_is_valid((x, y+1), "right"):
            possible_moves.append((x, y+1))

        return possible_moves

    def move_is_valid(self, move, direction):
        if self.state.map[move[0]][move[1]] != "||" and self.state.map:
            return True
        return False
        

# Generamos ahora una clase estado que contendrá toda la información necesaria de un estado.
class State:
    def __init__(self, mapa, agent_coords, rows_size, cols_size):
        self.map = mapa
        self.agent_coordinates = agent_coords
        self.rows_size = rows_size
        self.cols_size = cols_size

    def get_green_path(self):
        coords = []
        for x in range(self.rows_size):
            for y in range(self.cols_size):
                if self.map[x][y] == "🟩":
                    coords.append((x,y))
        return coords

class Problem:
    def __init__(self, initial_state, goal_state):
        self.goal_state = goal_state
        self.initial_state = initial_state
        