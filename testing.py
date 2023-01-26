import heapq
import robot as r
import maze.the_worlds_most_crazy_maze as b
obstacle = b.get_obstacles()

def get_shortest_path():
    
    start = (0,0)
    #get the end point
    end = get_end_point()
    # Create a priority queue to store the next nodes to visit
    heap = [(0, start)]
    # Create a dictionary to store the cost of visiting each node
    cost = {start: 0}
    # Create a dictionary to store the parent of each node
    parent = {start: None}
    # Create a set to store the visited nodes
    visited = []
    # Create a list of directions (up, down, left, right)
    dirs = [(0, 5), (0, -5), (5, 0), (-5, 0)]
    
    while heap:
        # Get the node with the lowest cost
        curr_cost, curr_pos = heapq.heappop(heap)
        # If the current position is the end, return the path
        if  curr_pos[1] == 200 or curr_pos[1] == -200\
            or curr_pos[0] == -100 or curr_pos[0] == 100:
            end = curr_pos
            return path(parent, end)[-1::-1]
        # If the current position has been visited, skip it
        if curr_pos in visited:
            continue
        visited.append(curr_pos)
        # Check the neighboring nodes
        for dx, dy in dirs:
            x, y = curr_pos
            new_x, new_y = x + dx, y + dy
            # If the new position is out of bounds or blocked, skip it
            if not (-100 <= new_x < 101 and -200 <= new_y < 201):
                continue
            if b.is_path_blocked(x,y,new_x,new_y,obstacle) and b.is_position_blocked(new_x,new_y,obstacle):
                continue
            # Calculate the new cost
            new_cost = cost[curr_pos] + 1
            # If the new cost is lower than the existing cost, update it
            if new_cost < cost.get((new_x, new_y), float("inf")):
                cost[(new_x, new_y)] = new_cost
                priority = new_cost + manhattan_distance(end, (new_x, new_y))
                heapq.heappush(heap, (priority, (new_x, new_y)))
                parent[(new_x, new_y)] = curr_pos
    
    # If the heap is empty, return None (no path was found)
    return 


# Helper function to calculate the Manhattan distance (heuristic)
def manhattan_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)


# Helper function to construct the path from the parent dictionary
def path(parent, end):
    curr = end
    path = []
    while curr:
        path.append(curr)
        curr = parent[curr]
    return path


def get_y_path(obstacle):
    from  random import choice
    path_side =  choice(["t",'d'])
    y = ...
    #finding the axis end point
    if path_side == "t":y= 200
    else: y = -200
    end = None
    for x in range(-100,101,5):
        if not (x+5,y) in obstacle:
            end = (x+5,y)
            break
    return end


def get_x_path(obstacle):
    from  random import choice
    path_side =  choice(["r",'l'])
    x = ...
    #finding the axis end point
    if path_side == "r":x= 200
    else: x = -200
    end = None
    for y in range(-200,201,5):
        if not (x,y+5) in obstacle:
            end = (x,y+5)
            break
    return end


def solve_maze(path,end):
    for pair in path:
        continue
    curr_pos = (0,0)
    for i in path:
    
        import turtle as b 
        b.shape("square")
        b.stamp()
        b.speed(1)
        if i[0] ==end[0] and end[1] == i[1]:
            break 
        
    
        b.goto(i)
        b.stamp()
        curr_pos = i
        
        
def get_end_point():
    global obstacle
    from random import choice
    return choice([get_x_path(obstacle),get_y_path(obstacle)])
    

def draw_path():
    path = get_shortest_path()
    end = get_end_point()
    solve_maze(path,end)
        
