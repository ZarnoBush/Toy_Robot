import queue


def keep_visited_history(visited, node):
    
    visited.add(node)
    

def is_valid_directions(direction, grid):
    
    x,y = direction ## x is row, y is col
    valid = False
    
    if x in range(0, len(grid)) and y in range(0, len(grid)):
        valid = True
        
        if grid[x][y] == 1:
            valid = False
        
        
    return valid


def is_visited(node, visited):

    if node in visited: return True
    
    return False


def get_neighbours(node, grid, visited):
    
    neighbours = []
    x,y = node
    
    dirs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    
    
    for direction in dirs:
        if is_valid_directions(direction, grid) \
            and not is_visited(direction, visited):
            neighbours.append(direction)
            
    return neighbours


def generate_graph(grid, start, end):
    
    if is_valid_directions(start, grid) and is_valid_directions(end, grid):
    
        stack = queue.Queue()
        stack.put(start)
        graph = {}
        visited = set()
        visited.add(start)
        
        while not stack.empty():
            node = stack.get()
            neighbours = []
            
            if node == end:
                print("Reached end")
                graph[node] = neighbour
                return graph
                
            
            for neighbour in get_neighbours(node, grid, visited):
                stack.put(neighbour)
                neighbours.append(neighbour)
                visited.add(neighbour)
        
            
            if neighbours != []:
                graph[node] = neighbours
        
        
    return {}
        

def solver(prev, end, start):
    
    path_list = [] ## list of values from end point to start point
    path_list.append(end)

    while end != start:
        for key, value in prev.items():
            if end in value:
                end = key
                path_list.append(end)
    

    return list(reversed(path_list))


def get_path(grid, start, end):
    
    graph = generate_graph(grid, start, end)
    if graph != {}:
        coordinate_path = solver(graph, end, start)

        
        
        
        node = coordinate_path[0]
        x,y = node
        instructions = []
        
        indexer = 1
        
        
        while len(instructions) <= len(coordinate_path)-2:
            directions = {
                (x-1, y) : "Up",
                (x+1,y) : "Down",
                (x, y-1) : "Left",
                (x, y+1) : "Right" 
            }
            
            node = coordinate_path[indexer]
            x,y = node
            if node in directions:
                instructions.append(directions.get(node))
            
            indexer+=1
            
        return instructions
    
    return []

        
def get_instructions(grid,start, end):


    instructions = get_path(grid, start, end)
    
    return instructions