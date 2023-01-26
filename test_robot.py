import robot
import unittest
from test_base import captured_io
from io import StringIO
import maze.obstacles as obstacles


class TestToyRobot(unittest.TestCase):

    def test_get_robot_name(self):
        with captured_io(StringIO('R2D2\n')) as (out, err):
            name = robot.get_robot_name()

        self.assertEqual(name, 'R2D2')
        output = out.getvalue().strip()
        self.assertEqual('''What do you want to name your robot?''', output)


    def test_get_command(self):
        with captured_io(StringIO('foward 10\nForward 10\n')) as (out, err):
            command = robot.get_command('R2D2')

        output = out.getvalue().strip()
        self.assertEqual('''R2D2: What must I do next? R2D2: Sorry, I did not understand 'foward 10'.
R2D2: What must I do next?''', output)
        self.assertEqual(command, 'forward 10')


    def test_split_command_input(self):
        args = robot.split_command_input('forward 10')
        self.assertEqual(args[0], 'forward')
        self.assertEqual(args[1], '10')

        args = robot.split_command_input('right')
        self.assertEqual(args[0], 'right')
        self.assertEqual(args[1], '')


    def test_is_int(self):
        isit = robot.is_int('10')
        self.assertTrue(isit)

        isit = robot.is_int('a')
        self.assertFalse(isit)


    def test_valid_command(self):
        isit = robot.valid_command('Forward 10')
        self.assertTrue(isit)

        isit = robot.valid_command('Foward 10')
        self.assertFalse(isit)

        isit = robot.valid_command('HeLp')
        self.assertTrue(isit)

        isit = robot.valid_command('replay 5-2')
        self.assertTrue(isit)


    def test_do_help(self):
        help = robot.do_help()
        help_boolean = help[0]
        help_string = help[1]
        self.assertTrue(help_boolean)
        self.assertEqual("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
""", help_string)


    def test_output(self):
        with captured_io(StringIO()) as (out, err):
            robot.output('R2D2', 'Shutting down..')

        output = out.getvalue().strip()
        self.assertEqual('R2D2: Shutting down..', output)


    def test_add_to_history(self):
        history = robot.add_to_history('forward 10', [])
        self.assertEqual(history, ['forward 10'])

        history = robot.add_to_history('right', ['forward 10'])
        self.assertEqual(history, ['forward 10', 'right'])

        history = robot.add_to_history('replay 5', ['forward 10', 'right'])
        self.assertEqual(history, ['forward 10', 'right', 'replay 5'])


    def test_replay(self):

        with captured_io(StringIO('R2D2\nforward 10\nback 5\nreplay\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual('''What do you want to name your robot? R2D2: Hello kiddo!
R2D2: Loaded obstacles.
R2D2: What must I do next?  > R2D2 moved forward by 10 steps.
 > R2D2 now at position (0,10).
R2D2: What must I do next?  > R2D2 moved back by 5 steps.
 > R2D2 now at position (0,5).
R2D2: What must I do next?  > R2D2 moved forward by 10 steps.
 > R2D2 now at position (0,15).
 > R2D2 moved back by 5 steps.
 > R2D2 now at position (0,10).
 > R2D2 replayed 2 commands.
 > R2D2 now at position (0,10).
R2D2: What must I do next? R2D2: Shutting down..''', output)


    def test_replay_reversed(self):

        with captured_io(StringIO('R2D2\nforward 10\nback 5\nreplay reversed\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual('''What do you want to name your robot? R2D2: Hello kiddo!
R2D2: Loaded obstacles.
R2D2: What must I do next?  > R2D2 moved forward by 10 steps.
 > R2D2 now at position (0,10).
R2D2: What must I do next?  > R2D2 moved back by 5 steps.
 > R2D2 now at position (0,5).
R2D2: What must I do next?  > R2D2 moved back by 5 steps.
 > R2D2 now at position (0,0).
 > R2D2 moved forward by 10 steps.
 > R2D2 now at position (0,10).
 > R2D2 replayed 2 commands in reverse.
 > R2D2 now at position (0,10).
R2D2: What must I do next? R2D2: Shutting down..''', output)


    def test_replay_silent(self):

        with captured_io(StringIO('R2D2\nforward 10\nback 5\nreplay silent\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual('''What do you want to name your robot? R2D2: Hello kiddo!
R2D2: Loaded obstacles.
R2D2: What must I do next?  > R2D2 moved forward by 10 steps.
 > R2D2 now at position (0,10).
R2D2: What must I do next?  > R2D2 moved back by 5 steps.
 > R2D2 now at position (0,5).
R2D2: What must I do next?  > R2D2 replayed 2 commands silently.
 > R2D2 now at position (0,10).
R2D2: What must I do next? R2D2: Shutting down..''', output)

    def test_replay_reversed_silent(self):

        with captured_io(StringIO('R2D2\nforward 10\nback 5\nreplay reversed silent\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual('''What do you want to name your robot? R2D2: Hello kiddo!
R2D2: Loaded obstacles.
R2D2: What must I do next?  > R2D2 moved forward by 10 steps.
 > R2D2 now at position (0,10).
R2D2: What must I do next?  > R2D2 moved back by 5 steps.
 > R2D2 now at position (0,5).
R2D2: What must I do next?  > R2D2 replayed 2 commands in reverse silently.
 > R2D2 now at position (0,10).
R2D2: What must I do next? R2D2: Shutting down..''', output)


if __name__ == '__main__':
    unittest.main()