import mazes
from maze_foundations import Problem, State, Node
import bfs
import dfs
from threading import Thread, Lock


# Creamos problema easy.
easy_maze = mazes.easy_maze
easy_initial_state = State(easy_maze["initial"], easy_maze["agent_coords"], easy_maze["rows"], easy_maze["cols"])
easy_goal_state = State(easy_maze["goal"], easy_maze["agent_coords"], easy_maze["rows"], easy_maze["cols"])
easy_problem = Problem(easy_initial_state, easy_goal_state)

# Creamos problema medium.
medium_maze = mazes.medium_maze
medium_initial_state = State(medium_maze["initial"], medium_maze["agent_coords"], medium_maze["rows"], medium_maze["cols"])
medium_goal_state = State(medium_maze["goal"], medium_maze["agent_coords"], medium_maze["rows"], medium_maze["cols"])
medium_problem = Problem(medium_initial_state, medium_goal_state)

# Creamos problema hard.
hard_maze = mazes.hard_maze
hard_initial_state = State(hard_maze["initial"], hard_maze["agent_coords"], hard_maze["rows"], hard_maze["cols"])
hard_goal_state = State(hard_maze["goal"], hard_maze["agent_coords"], hard_maze["rows"], hard_maze["cols"])
hard_problem = Problem(hard_initial_state, hard_goal_state)


def start_algorithms(algorithms):
    """
    Recibe una lista de algoritmos.
    """  

# Creamos los solvers para poder resolver el problema.
bfs_solver = bfs.BFS(hard_problem)
dfs_solver = dfs.DFS(hard_problem)

algorithms = [
    bfs_solver,
    dfs_solver
]



#node = Node(initial_state, None)
#node.expand()