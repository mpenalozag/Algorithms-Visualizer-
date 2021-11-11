import mazes
from maze_foundations import Problem, State, Node
import bfs


# Creamos los estado initial y goal para inicializar el problema.
maze = mazes.easy_maze
initial_state = State(maze["initial"], maze["agent_coords"], maze["rows"], maze["cols"])
goal_state = State(maze["goal"], maze["agent_coords"], maze["rows"], maze["cols"])

# Creamos el problema para que pueda ser tratado por nuestros solvers.
easy_problem = Problem(initial_state, goal_state)

maze = mazes.medium_maze
initial_state = State(maze["initial"], maze["agent_coords"], maze["rows"], maze["cols"])
goal_state = State(maze["goal"], maze["agent_coords"], maze["rows"], maze["cols"])

medium_problem = Problem(initial_state, goal_state)

maze = mazes.hard_maze
initial_state = State(maze["initial"], maze["agent_coords"], maze["rows"], maze["cols"])
goal_state = State(maze["goal"], maze["agent_coords"], maze["rows"], maze["cols"])

hard_problem = Problem(initial_state, goal_state)



# Creamos el solver para poder resolver el problema.
bfs_solver = bfs.BFS(hard_problem)

#node = Node(initial_state, None)
#node.expand()