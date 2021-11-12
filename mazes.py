# En este archivo tendremos todos los mapas de laberintos

def print_maze(maze, cols):
    """
    Esta función se encarga de printear los laberintos con un formato entendible.
    """
    for i in range(cols+1):
        print("--", end="")
    print()
    for row in maze:
        row_add = "|"
        for i in range(cols):
            row_add += row[i]
        row_add += "|"
        print(row_add)
    for i in range(cols+1):
        print("--", end="")
    print()



easy_maze = dict()
easy_maze["rows"] = 4
easy_maze["cols"] = 3
easy_maze["initial"] = [
    ["🟩", "||", "GG"],
    ["  ", "||", "  "],
    ["  ", "||", "  "],
    ["  ", "  ", "  "],
]
easy_maze["agent_coords"] = (0,0)
easy_maze["goal"] = [
    ["  ", "||", "🟩"],
    ["  ", "||", "  "],
    ["  ", "||", "  "],
    ["  ", "  ", "  "],
]


medium_maze = dict()
medium_maze["initial"] = [
    ["  ","||","  ","||","  ","  ","  ",],
    ["  ","||","  ","||","  ","||","||",],
    ["🟩","  ","  ","  ","  ","||","GG",],
    ["  ","||","  ","||","  ","||","  ",],
    ["  ","||","  ","||","  ","  ","  ",]
]
medium_maze["rows"] = 5
medium_maze["cols"] = 7
medium_maze["agent_coords"] = (2,0)
medium_maze["goal"] = [
    ["  ","||","  ","||","  ","  ","  ",],
    ["  ","||","  ","||","  ","||","||",],
    ["  ","  ","  ","  ","  ","||","🟩",],
    ["  ","||","  ","||","  ","||","  ",],
    ["  ","||","  ","||","  ","  ","  ",]
]


hard_maze = dict()
hard_maze["rows"] = 15
hard_maze["cols"] = 10
hard_maze["agent_coords"] = (0, 0)
hard_maze["initial"] = [
    ["🟩", "||", "  ", "||", "  ", "  ", "  ", "||", "  ", "GG" ],
    ["  ", "||", "  ", "||", "  ", "||", "||", "||", "  ", "||" ],
    ["  ", "  ", "  ", "||", "  ", "||", "  ", "||", "  ", "  " ],
    ["  ", "||", "||", "||", "  ", "||", "  ", "||", "||", "  " ],
    ["  ", "  ", "  ", "||", "  ", "||", "  ", "||", "  ", "  " ],
    ["  ", "  ", "  ", "  ", "  ", "||", "  ", "||", "  ", "||" ],
    ["  ", "  ", "  ", "||", "  ", "||", "  ", "||", "  ", "||" ],
    ["  ", "||", "||", "||", "  ", "  ", "  ", "||", "  ", "||" ],
    ["  ", "  ", "  ", "||", "  ", "||", "||", "||", "  ", "||" ], 
    ["  ", "||", "  ", "||", "  ", "||", "  ", "  ", "  ", "  " ],
    ["  ", "||", "  ", "||", "  ", "||", "  ", "||", "||", "||" ],
    ["  ", "||", "  ", "||", "  ", "||", "  ", "  ", "  ", "  " ],
    ["  ", "||", "  ", "||", "  ", "||", "  ", "||", "||", "  " ],
    ["  ", "||", "||", "||", "  ", "||", "  ", "||", "  ", "  " ],
    ["  ", "  ", "  ", "||", "  ", "  ", "  ", "||", "||", "  " ],
]

hard_maze["goal"] = [
    ["  ", "||", "  ", "||", "  ", "  ", "  ", "||", "  ", "🟩", ],
    ["  ", "||", "  ", "||", "  ", "||", "||", "||", "  ", "||", ],
    ["  ", "  ", "  ", "||", "  ", "||", "  ", "||", "  ", "  ", ],
    ["  ", "||", "||", "||", "  ", "||", "  ", "||", "||", "  ", ],
    ["  ", "  ", "  ", "||", "  ", "||", "  ", "||", "  ", "  ", ],
    ["  ", "  ", "  ", "  ", "  ", "||", "  ", "||", "  ", "||", ],
    ["  ", "  ", "  ", "||", "  ", "||", "  ", "||", "  ", "||", ],
    ["  ", "||", "||", "||", "  ", "  ", "  ", "||", "  ", "||", ],
    ["  ", "  ", "  ", "||", "  ", "||", "||", "||", "  ", "||", ], 
    ["  ", "||", "  ", "||", "  ", "||", "  ", "  ", "  ", "  ", ],
    ["  ", "||", "  ", "||", "  ", "||", "  ", "||", "||", "||", ],
    ["  ", "||", "  ", "||", "  ", "||", "  ", "  ", "  ", "  ", ],
    ["  ", "||", "  ", "||", "  ", "||", "  ", "||", "||", "  ", ],
    ["  ", "||", "||", "||", "  ", "||", "  ", "||", "  ", "  ", ],
    ["  ", "  ", "  ", "||", "  ", "  ", "  ", "||", "||", "  ", ],
]