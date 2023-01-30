import random 


def get_obstacles():
    '''
    Generates and returns a list of obstacles.
    Each obstacle is represented by it's bottom left cooordinate, (x,y).
    '''
    obstacles = []
    for x in range(-100,101,5):
        for y in range(-200,201,5):
            if (x + 5) >200 or (y+5) >200:continue
            if make_top_path(x,y): continue
            if make_bottom_path(x,y): continue
            if make_right_path(x,y):continue
            if make_left_path(x,y):continue
            obstacles.append((x,y))
    return obstacles

        
def make_top_path(x,y):
    if x >= -20 and x<20 and y > -40 and y<40:return True
    elif x >= 20 and x<=80 and (y>=20 and y<=30):return True
    elif x >= 60 and x<=70 and (y>=30 and y<=60):return True
    elif x >= 40 and x<=70 and (y>=60 and y<=70):return True
    elif x >= 40 and x<=70 and (y>=60 and y<=70):return True     
    elif x >= -40 and x<=70 and (y>=60 and y<=70):return True   
    elif x >= -10 and x<=0 and (y>=70 and y<=180):return True    
    elif x >= -30 and x<=90 and (y>=180 and y<=190):return True
    elif x >= 40 and x<=50 and (y>=80 and y<=200):return True
    else: return False


def make_bottom_path(x,y):
    if x >= -70 and x<=-20 and (y>=-30 and y<=-20):return True
    elif x >= -70 and x<=-60 and (y>=-60 and y<=-30):return True
    elif x >= -70 and x<=40 and (y>=-70 and y<=-60):return True
    elif x >= 0 and x<=10 and (y>=-180 and y<=-70):return True     
    elif x >= 20 and x<=90 and (y>=-80 and y<=-70):return True   
    elif x >= -90 and x<=20 and (y>=-190 and y<=-180):return True    
    elif x >= -40 and x<=-30 and (y>=-200 and y<=-140):return True
    else: return False


def make_left_path(x,y):
    if x >= -90 and x<=-20 and (y>=-10 and y<=0):return True
    elif x >= -90 and x<=-80 and (y>=-150 and y<=-10):return True
    elif x >= -90 and x<=70 and (y>=-140 and y<=-130):return True
    elif x >= 60 and x<=70 and (y>=-190 and y<=-70):return True     
    elif x >= 60 and x<=100 and (y>=-190 and y<=-180):return True   
    elif x >= -90 and x<=20 and (y>=-190 and y<=-180):return True    
    elif x >= -90 and x<=100 and (y>=-195 and y<=-185):return True
    else: return False


def make_right_path(x,y):
    if x >= 20 and x<=94 and (y>=-10 and y<=0):return True
    elif x >= 80 and x<=94 and (y>=-160 and y<=80):return True
    elif x >= -85 and x<95 and (y>=80 and y<=90):return True
    elif x >= -80 and x<=-70 and (y>=80 and y<=120):return True     
    elif x >= -100 and x<=-15 and (y>=120 and y<=130):return True   
    else: return False


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
