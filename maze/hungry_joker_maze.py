import random

MAZE_HEIGHT = 400
MAZE_WIDTH = 200
CELL_SIZE = 5

obs_history = []


def create_base_grid()->list:
    rows = MAZE_HEIGHT//CELL_SIZE
    cols = MAZE_WIDTH//CELL_SIZE
    
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    return grid


def create_turtle_coordinate_grid():
    x_ranges = range(-(MAZE_WIDTH//2), MAZE_WIDTH//2, 5)
    y_ranges = range(MAZE_HEIGHT//2, -(MAZE_HEIGHT//2), -5)
    grid = []
    
    for i in y_ranges:
        coods = []
        for j in x_ranges:
            positions = (j,i)
            coods.append(positions)
        grid.append(coods)
        
    
    return grid
            

def reset_obs():
    global obs_history
    
    obs_history = []

def get_obstacles():
    
    # - get algorithm to generate 1's in base grid, map to turt grid
    
    
    return obs_history

        
def is_position_blocked(x,y):
    global obs_history
    for obs in obs_history:
        if ((x in range(obs[0], obs[0]+5)) and (y in range(obs[1],obs[1]+5))): return True
    return False


def is_path_blocked(x1,y1, x2, y2):
    global obs_history
    
    path_blocked = False
    
    if x1 == x2:
        if y1 < y2:
            for i in range(y1,y2):
                if is_position_blocked(x2,i):
                    path_blocked = True
        elif y1 > y2:
            for i in range(y2, y1):
                if is_position_blocked(x2,i):
                    path_blocked = True
        
    elif y1 == y2:
        if x1 < x2:
            for i in range(x1,x2):
                if is_position_blocked(i, y2):
                    path_blocked = True
                
        elif x1 > x2:
            for i in range(x2, x1):
                if is_position_blocked(i, y2):
                    path_blocked = True
             
                    
    return path_blocked