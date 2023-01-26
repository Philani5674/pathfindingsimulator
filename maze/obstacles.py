import random 

def get_obstacles():
    '''
    Generates and returns a list of obstacles.
    Each obstacle is represented by it's bottom left cooordinate, (x,y).
    '''
    obstacles = []
    len_obstacles = random.randint(1, 10)

    while len(obstacles) < len_obstacles:
        obs_x, obs_y = random.randint(-100,100), random.randint(-200,200)
        if (obs_x + 4) <= 100 and (obs_y + 4) <= 200:
            obs = (obs_x,obs_y)
            obstacles.append(obs) 
        else:
            continue

    return obstacles


def is_position_blocked(x, y, obs_list):
    '''
    Returns true if potential new position of robot is in an obstacle.
    '''
    for obs in obs_list:
        obs_x, obs_y = obs[0], obs[1]
        if obs_x <= x <= obs_x + 5 and obs_y <= y <= obs_y + 5:return True
        else:continue


def is_path_blocked(x1, y1, x2, y2, obs_list):
    '''
    Returns true if an obstacle lies between the robot's start point 
    and potential end point.
    '''
    if x1 == x2:
        x = x1
        for obs in obs_list:
            obs_x, obs_y= obs[0], obs[1]
            if y1 < y2 and obs_x <= x <= obs_x + 5 and  y1 <= obs_y + 5 <= y2:return True
            elif y2 < y1 and obs_x <= x <= obs_x + 5 and y2 <= obs_y + 5 <= y1:return True
            else:continue
                

    elif y1 == y2:
        y = y1
        for obs in obs_list:
            obs_x, obs_y= obs[0], obs[1]
            if x1 < x2 and obs_y <= y <= obs_y + 5 and x1 <= obs_x + 5 <= x2:return True
            elif x2 < x1 and obs_y <= y <= obs_y + 5 and x2 <= obs_x + 5 <= x1:return True
            else:continue
