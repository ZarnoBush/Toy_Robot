import random

obs_history = []
HEIGHT = 400
WIDTH = 200


def get_edges(end):
    
    
    
    
    
    edges = {
        "top" : (0,99),
        "bottom" : (399, 1),
        "left" : (40,0),
        "right" : (40, 199)
    }
    
    if end in edges:
        return edges.get(end)
    
    return edges.get("top")

def basic_blueprint():
    
    r = HEIGHT
    c = WIDTH
    
    grid = [[0 for _ in range(c)] for _ in range(r)]
    
    return grid


def basic_turtle_grid():
    
    turt = []
    
    for i in range((HEIGHT//2), -(HEIGHT//2),-1):
        turt_coods = []
        for j in range(-(WIDTH//2), (WIDTH//2)+1):
            positions = (j,i)
            turt_coods.append(positions)
            

            
        turt.append(turt_coods)
        
    return turt


        

def get_random_coods():
    to_obs = []
    random_range = random.randint(1,10)
    for _ in range(random_range):
        x = random.randint(-100,101)
        y = random.randint(-200,201)
        
        to_obs.append((x,y))
        
    return to_obs


def graph_obstacles_to_grid(obs):
    
    grid = basic_blueprint()
    print(f"Len og grid{len(grid)}")
    turt = basic_turtle_grid()
    print(f"Len og turt{len(turt)}")
    print(f"obs: {obs}")
        
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if turt[i][j] in obs:
                grid[i][j] = 1
                

            
    return grid
    

def reset_obs():
    global obs_history
    
    obs_history = []

def get_obstacles():
    global obs_history
    
    obs_history = get_random_coods()
    for i in obs_history:
        print(f"Obs:{i}")
    blueprint = graph_obstacles_to_grid(obs_history)
    # for blue in blueprint:
    #     print(blue)

        
    return obs_history, blueprint

        
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