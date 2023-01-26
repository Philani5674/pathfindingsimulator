# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------
import maze.obstacles as ob


def show_obstacles(obs_list):

    if len(obs_list) != 0:
        print('There are some obstacles:')
        for obs in obs_list:
            obs_x, obs_y = obs[0], obs[1]
            print(f'- At position {obs_x},{obs_y} (to {obs_x + 4},{obs_y + 4})')
    else:
        return

def show_position(robot_name, x, y):
    print(' > '+robot_name+' now at position ('+str(x)+','+str(y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    min_y, max_y = -200, 200
    min_x, max_x = -100, 100

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps, x, y, dir_index):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    directions = ['north', 'east', 'south', 'west']

    new_x = x
    new_y = y

    if directions[dir_index] == 'north':
        new_y = new_y + steps
    elif directions[dir_index] == 'east':
        new_x = new_x + steps
    elif directions[dir_index] == 'south':
        new_y = new_y - steps
    elif directions[dir_index] == 'west':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y): 
        return True, new_x, new_y
    return False, x, y



def do_forward(robot_name, steps, x, y, dir_index, obs_list):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    update, new_x, new_y = update_position(steps, x, y, dir_index)
    if ob.is_position_blocked(new_x, new_y, obs_list) or ob.is_path_blocked(x, y, new_x, new_y, obs_list):
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.', x, y
    elif update:
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.', new_x, new_y
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.', x, y


def do_back(robot_name, steps, x, y, dir_index, obs_list):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    update, new_x, new_y = update_position(-steps, x, y, dir_index)
    if ob.is_position_blocked(new_x, new_y, obs_list) or ob.is_path_blocked(x, y, new_x, new_y, obs_list):
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.', x, y
    elif update:
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.', new_x, new_y  
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.', x, y


def do_right_turn(robot_name, dir_index):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """

    dir_index += 1
    if dir_index > 3:
        dir_index = 0

    return True, ' > '+robot_name+' turned right.', dir_index


def do_left_turn(robot_name, dir_index):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """

    dir_index -= 1
    if dir_index < 0:
        dir_index = 3

    return True, ' > '+robot_name+' turned left.', dir_index


def do_sprint(robot_name, steps, x, y, dir_index, obs_list):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1, x, y, dir_index, obs_list)
    else:
        (do_next, command_output, x, y) = do_forward(robot_name, steps, x, y, dir_index, obs_list)
        print(command_output)
        return do_sprint(robot_name, steps - 1, x, y, dir_index, obs_list)


def setup_world():
    pass

