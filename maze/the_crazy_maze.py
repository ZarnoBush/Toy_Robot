import random

MAZE_HEIGHT = 420
MAZE_WIDTH = 420
CELL_SIZE = 20
rows = MAZE_HEIGHT//CELL_SIZE
cols = MAZE_WIDTH//CELL_SIZE
y_ranges = range((MAZE_HEIGHT//2), -(MAZE_HEIGHT//2), -20)
x_ranges = range(-(MAZE_WIDTH//2), (MAZE_WIDTH//2)+1, 20)


obs_history = []
v_edges = []
right_edge = []
left_edge = []


def get_edges(end):
    
    top, bottom = v_edges[0], v_edges[-1]
    left = left_edge[0]
    right = right_edge[0]
    
    edges = {
        "top": top,
        "bottom": bottom,
        "left": left,
        "right": right
    }
    
    if end in edges:
        return edges.get(end)
    
    return None



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

def randomize_pathways_vertically(ran_range, start, stop, grid):
    
    for row in range(len(grid)):
        if row == 0 or row == len(grid)-1:
            
            ran_range = random.randint(start+1, stop-1)
            grid[row][ran_range] = 0
            v_edges.append((row, ran_range))
            
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


def swap_vals(val1, val2):
    
    if val2 < val1:
        return val2, val1
    
    return val1, val2

def randomize_pathways_horizontally(ran_range, start, stop, grid):
            
    new_range = [i for i in range(start+1, stop, 2)]
    shuffle = []
    while new_range != []:
        i = random.randint(0, len(new_range)-1)
        shuffle.append(new_range[i])
        new_range.pop(i)

    pos_col = 0
    neg_col = stop
    
    for i in shuffle:
        
        grid[i][pos_col] = 0
        left_edge.append((i,pos_col))
        pos_col+=2
        if pos_col==10:
            break
    
    
    neg_shuffle = []
    while shuffle != []:
        i = random.randint(0, len(shuffle)-1)
        neg_shuffle.append(shuffle[i])
        shuffle.pop(i)
        
    for i in neg_shuffle:
    
        grid[i][neg_col] = 0
        right_edge.append((i,neg_col))
        neg_col-=2
        if neg_col == 12:
            break

    return grid

            

def randomize_pathways(grid):
    
    ran_range = 0
    start = 0
    stop = len(grid[0])-1
    
    grid = randomize_pathways_vertically(ran_range, start, stop, grid)
    grid_h = randomize_pathways_horizontally(ran_range, start, stop, grid)
     

    return grid_h



            

def map_blueprint_to_turtle_grid():
    
    blueprint = modify_base_grid() ## grid
    turtle_grid = create_turtle_coordinate_grid() ## turtle coods
    

    gets = []

    
    for i in range(rows):
        for j in range(cols):
            if blueprint[i][j] == 1:
                gets.append(turtle_grid[i][j])
    
    return gets,blueprint
                

def reset_obs():
    global obs_history
    
    obs_history = []
    


def get_obstacles():
    global obs_history
    grid, blueprint = map_blueprint_to_turtle_grid()
    
    
    while grid != []:
        i = random.randint(0,len(grid)-1)
        obs_history.append(grid[i])
        grid.pop(i)
    

    return obs_history, blueprint

        
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

