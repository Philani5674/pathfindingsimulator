import unittest
import maze.obstacles as obs


class TestObstacles(unittest.TestCase):

    def test_get_obstacles(self):
        obs.random.randint = lambda a, b: 0
        obstacles = obs.get_obstacles()

        self.assertEqual(len(obstacles), 0)
        self.assertEqual(obstacles, [])

        obs.random.randint = lambda a, b: 1
        obstacles = obs.get_obstacles()

        self.assertEqual(len(obstacles), 1)
        self.assertEqual(obstacles, [(1,1)])


    def test_position_blocked(self):
        isit = obs.is_position_blocked(5, 5, [(1,1), (6,9), (-20,120)])
        self.assertTrue(isit)

        isit = obs.is_position_blocked(6, -20, [(1,1), (6,9), (-20,120)])
        self.assertFalse(isit)


    def test_path_blocked(self):
        isit = obs.is_path_blocked(0, 0, 0, 5, [(0,1), (6,9), (-20,120)])
        self.assertTrue(isit)

        isit = obs.is_path_blocked(6, -20, 6, 39, [(1,1), (3,9), (-20,120)])
        self.assertTrue(isit)

        isit = obs.is_path_blocked(-3, 0, 90, 0, [(0,1), (6,9), (-20,120)])
        self.assertNotEqual(isit, True)


if __name__ == '__main__':
    unittest.main()