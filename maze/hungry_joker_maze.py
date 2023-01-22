import random


MAZE_HEIGHT = 420
MAZE_WIDTH = 420
CELL_SIZE = 20
rows = MAZE_HEIGHT//CELL_SIZE
cols = MAZE_WIDTH//CELL_SIZE
y_ranges = range((MAZE_HEIGHT//2), -(MAZE_HEIGHT//2), -20)

x_ranges = range(-(MAZE_WIDTH//2), (MAZE_WIDTH//2)+1, 20)


obs_history = []


def create_base_grid()->list:
    
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    return grid


def modify_base_grid():
    grid = create_base_grid()
    length_of_row = len(grid[0])
    median_of_grid = (rows+1)//2
    start_x = 0
    end_x = 0
    start_y = median_of_grid-3
    end_y = median_of_grid+2
    start_z = 0
    end_z = len(grid)-1
    column_stretcher = 0
    column_shrinker = len(grid)-1
    mid_point = CELL_SIZE//2
    
    
    for row in range(len(grid)):
        if row%2==0 and row < median_of_grid:
            square_range = range(start_x,length_of_row+end_x)
            for col in square_range:
                grid[row][col] = 1
                
            start_x+=2
            end_x-=2
            
        elif row%2==0 and row > median_of_grid:
            square_range = range(start_y, end_y)
            for col in square_range:
                grid[row][col] = 1
                
            start_y-=2
            end_y+=2
            
        if row%2==0:
            for z in range(start_z, end_z):
                grid[z][column_stretcher] = 1
                grid[z][column_shrinker] = 1
                
            start_z+=2
            end_z-=2
            column_stretcher+=2
            column_shrinker-=2
            
    ## hard-code opening in the middle
    grid[10][10] = 0
    grid = place_extra_walls(grid)


    return randomize_pathways(grid)


def create_turtle_coordinate_grid():
    grid = []
    
    
    for i in y_ranges:
        coods = []
        for j in x_ranges:
            positions = (j,i)
            coods.append(positions)
            
        grid.append(coods)

        
    
    return grid


def randomize_pathways(grid):
    
    ran_range = 0
    start = 0
    stop = len(grid[0])-1
    
    for row in range(len(grid)):
        if row == 0 or row == len(grid)-1:
            
            ran_range = random.randint(start+1, stop-1)
            grid[row][ran_range] = 0
            
        if row == 2 or row == stop-2:
            
            ran_range = random.randint(start+3, stop-4)
            grid[row][ran_range] = 0
            
        if row == 4 or row == stop-4:
            
            ran_range = random.randint(start+5, stop-5)
            grid[row][ran_range] = 0
            
        if row == 6 or row == stop-6:
            
            ran_range = random.randint(start+7, stop-7)
            grid[row][ran_range] = 0
            
        if row == 8 or row == stop - 8:
            ran_range = random.randint(start+9, stop-9)
            grid[row][ran_range] = 0
            
            
    return grid


def place_extra_walls(grid):
    
    ran_range = 0
    start = 1
    stop = len(grid[0])-1
    range_start = 2
    range_end = len(grid[0])-3
    swap = 0
    
    for row in range(len(grid)):
        if row == 1 or row == stop-1:
            ran_range = random.randint(start+2, stop-2)
            grid[row][ran_range] = 1
            
        if row == 3 or row == stop-3:
            ran_range = random.randint(start+5, stop-5)
            grid[row][ran_range] = 1
                
            
    return grid
            
        
            
        
            


def map_blueprint_to_turtle_grid():
    
    blueprint = modify_base_grid()
    turtle_grid = create_turtle_coordinate_grid()
    print("turtle grid info")

    gets = []

    
    for i in range(rows):
        for j in range(cols):
            if blueprint[i][j] == 1:
                gets.append(turtle_grid[i][j])
    
    return gets
                

def reset_obs():
    global obs_history
    
    obs_history = []

def get_obstacles():
    
    # - get algorithm to generate 1's in base grid, map to turt grid
    global obs_history
    obs_history = map_blueprint_to_turtle_grid()

    
    return obs_history

        
def is_position_blocked(x,y):
    
    global obs_history
    for obs in obs_history:
        
        if ((x in range(obs[0], obs[0]+21)) and (y in range(obs[1]-20,obs[1]+1))): return True
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