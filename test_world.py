import world.text.world as world
import unittest
import sys
from test_base import captured_io
from io import StringIO

class TestWorld(unittest.TestCase):

    def test_text_world_exists(self):
        self.assertTrue('world' in sys.modules)


    def test_turtle_world_exists(self):
        '''This tests passes but opens turtle screen everytime it is run.
        I commented out so it doesn't affect the test runtime when I grade.
        '''

        # import world.turtle.world
        # self.assertTrue('world' in sys.modules)


    def test_show_position(self):
        with captured_io(StringIO()) as (out, err):
            world.show_position('R2D2', 0, 0)

        output = out.getvalue().strip()
        self.assertEqual('''> R2D2 now at position (0,0).''',
        output)

        with captured_io(StringIO()) as (out, err):
            world.show_position('R2D2', -10, 5)

        output = out.getvalue().strip()
        self.assertEqual('''> R2D2 now at position (-10,5).''',
        output)


    def test_position_allowed(self):

        result = world.is_position_allowed(-100, -200)
        self.assertEqual(result, True)

        result = world.is_position_allowed(100, 200)
        self.assertTrue(result)

        result = world.is_position_allowed(101, 201)
        self.assertEqual(result, False)

        result = world.is_position_allowed(-101, 201)
        self.assertFalse(result)


    def test_update_position(self):

        result = world.update_position(10, 0, 0, 0)
        self.assertEqual(result, (True, 0, 10))

        result = world.update_position(10, 0, 10, 1)
        self.assertEqual(result, (True, 10, 10))

        result = world.update_position(5, 10, 10, 2)
        self.assertEqual(result, (True, 10, 5))

        result = world.update_position(5, 10, 5, 3)
        self.assertEqual(result, (True, 5, 5))

        result = world.update_position(201, 0, 0, 0)
        self.assertEqual(result, (False, 0, 0))


    def test_do_forward(self):

        result = world.do_forward('R2D2', 10, 0, 0, 0, [])
        self.assertEqual(result, (True, ' > R2D2 moved forward by 10 steps.', 0, 10))

        result = world.do_forward('R2D2', 201, 0, 0, 0, [])
        self.assertEqual(result, (True, 'R2D2: Sorry, I cannot go outside my safe zone.', 0, 0))


    def test_do_back(self):

        result = world.do_back('R2D2', 10, 0, 0, 0, [])
        self.assertEqual(result, (True, ' > R2D2 moved back by 10 steps.', 0, -10))

        result = world.do_back('R2D2', 201, 0, 0, 0, [])
        self.assertEqual(result, (True, 'R2D2: Sorry, I cannot go outside my safe zone.', 0, 0))


    def test_do_right_turn(self):

        result = world.do_right_turn('R2D2', 0)
        self.assertEqual(result, (True, ' > R2D2 turned right.', 1))

        result = world.do_right_turn('R2D2', 3)
        self.assertEqual(result, (True, ' > R2D2 turned right.', 0))


    def test_do_left_turn(self):

        result = world.do_left_turn('R2D2', 0)
        self.assertEqual(result, (True, ' > R2D2 turned left.', 3))

        result = world.do_left_turn('R2D2', 1)
        self.assertEqual(result, (True, ' > R2D2 turned left.', 0))


    def test_do_sprint(self):

        with captured_io(StringIO()) as (out, err):
            result = world.do_sprint('R2D2', 5, 0, 0, 0, [])
            self.assertEqual(result, (True, ' > R2D2 moved forward by 1 steps.', 0, 15 ))


    def test_show_obstacles(self):

        with captured_io(StringIO()) as (out, err):
            world.show_obstacles([(1,1), (-50, 100), (90, -39)])

        output = out.getvalue().strip()
        self.assertEqual('''There are some obstacles:
- At position 1,1 (to 5,5)
- At position -50,100 (to -46,104)
- At position 90,-39 (to 94,-35)''',output)





if __name__ == '__main__':
    unittest.main()
