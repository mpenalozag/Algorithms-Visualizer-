import copy
from mazes import all_mazes, print_maze
from foundations import Problem, State, Node
from algorithms import bfs
from algorithms import dfs
from threading import Thread, Lock
from copy import deepcopy

import os

while True:
    print(" S E L E C C I O N A   E L   L A B E R I N T O   A   R E S O L V E R")
    contador = 1
    for name, maze in all_mazes.items():
        print(f"{contador})")
        print_maze(maze["initial"], maze["cols"])
        print("----------------------------------------")
        contador += 1 
    print("E N T E R   0   TO   Q U I T")
    print("\n\n")
    selected_maze = input()
    os.system('cls' if os.name == 'nt' else 'clear')
    if selected_maze == "0":
        break
    if selected_maze == "1":
        print("S E L E C C O N A S T E   E S T E   L A B E R I N T O")
        print_maze(all_mazes["easy"]["initial"], all_mazes["easy"]["cols"])
        chosen_maze = all_mazes["easy"]
    if selected_maze == "2":
        print("S E L E C C O N A S T E   E S T E   L A B E R I N T O")
        print_maze(all_mazes["medium"]["initial"], all_mazes["medium"]["cols"])
        chosen_maze = all_mazes["medium"]
    if selected_maze == "3":
        print("S E L E C C O N A S T E   E S T E   L A B E R I N T O")
        print_maze(all_mazes["hard"]["initial"], all_mazes["hard"]["cols"])
        chosen_maze = all_mazes["hard"]
    problem_initial_state = State(deepcopy(chosen_maze["initial"]), chosen_maze["agent_coords"], chosen_maze["rows"], chosen_maze["cols"])
    problem_goal_state = State(deepcopy(chosen_maze["goal"]), chosen_maze["agent_coords"], chosen_maze["rows"], chosen_maze["cols"])
    problem = Problem(problem_initial_state, problem_goal_state)
    
    print("\n\n")

    print("S E L E C C I O N A   E L   A L G O R I T M O   A   U T I L I Z A R")
    print("\t1) B R E A D T H   F I R S T   S E A R C H   W O R K I N G")
    print("\t2) D E P T H   F I R S T   S E A R C H   W O R K I N G")
    print("\n E N T E R   0   TO   Q U I T\n\n")

    selected_algorithm = input()

    if selected_algorithm == "1":
        bfs_solver = bfs.BFS(problem)
    if selected_algorithm == "2":
        dfs_solver = dfs.DFS(problem)