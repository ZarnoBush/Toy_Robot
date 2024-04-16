import random

obs_history = []


def reset_obs():
    global obs_history
    
    obs_history = []

def get_obstacles():
    global obs_history
    blueprint = []
    random_range = random.randint(1,10)
    for i in range(random_range):
        x = random.randint(-10,10)
        y = random.randint(-20,20)
        obs_history.append((x,y))
        
    
    
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