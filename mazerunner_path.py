import heapq
import maze.the_worlds_most_crazy_maze as b


def get_shortest_path(obstacle,end,side):
    
    start = (0,0)
    heap = [(0, start)]
    cost = {start: 0}
    parent = {start: None}
    visited = []
    dirs = [(0, 5), (0, -5), (5, 0), (-5, 0)]
    
    while heap:
        # Get the node with the lowest cost
        curr_cost, curr_pos = heapq.heappop(heap)
        # If the current position is the end, return the path
        if  (curr_pos[1] == 200 or curr_pos[1] == -200 ) and (side == 'top' or side == "bottom"):
            end = curr_pos
            return path(parent, end)[-1::-1]

        if  (side == 'left'and curr_pos[0] == -100):
            end = curr_pos
            return path(parent, end)[-1::-1]

        if side == "right" and curr_pos[0] == 100:
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
            #if the position is the obsticle skip it
            if b.is_path_blocked(x,y,new_x,new_y,obstacle) and b.is_position_blocked(new_x,new_y,obstacle):
                continue
            # Calculate the new cost
            new_cost = cost[curr_pos] + 5
            # If the new cost is lower than the existing cost, update it
            if new_cost < cost.get((new_x, new_y), float("inf")):
                cost[(new_x, new_y)] = new_cost
                priority = new_cost + manhattan_distance(end, (new_x, new_y))
                heapq.heappush(heap, (priority, (new_x, new_y)))
                parent[(new_x, new_y)] = curr_pos
    return []


def manhattan_distance(pos1, pos2):
    ''''calculate the Manhattan distance'''

    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)

def path(parent, end):
    '''construct the path from the parent dictionary'''
    curr = end
    path = []
    while curr:
        path.append(curr)
        curr = parent[curr]
    return path


def get_end_point(obstacle,side):
    '''get the end point of the selected side.'''

    x =...
    y = ...
    if side == "left":
        x= -100
        for y in range(-200,201,5):
            if not (x,y) in obstacle:
                end = (x,y)
                break
        return end

    elif side == "right":
        x= 100
        for y in range(-200,201,5):
            if not (x,y) in obstacle:
                end = (x,y)
                break
        return end

    elif side == "top" or side == None:
        y= 200
        for x in range(-100,101,5):
            if not (x,y) in obstacle:
                end = (x,y)
                break
        return end

    elif side == "bottom":
        y= -200
        for x in range(-100,101,5):
            if not (x,y) in obstacle:
                end = (x,y)
                break
        return end
    else:
        y= 200
        for x in range(-100,101,5):
            if not (x,y) in obstacle:
                end = (x,y)
                break
        return end


def draw_path(obstacle,side):
    '''getting the path from the start to the end point.'''

    if side =='' : side = "top"
    end = get_end_point(obstacle, side)
    path = get_shortest_path(obstacle,end, side)
    return path

