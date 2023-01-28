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





if __name__ == '__main__':
    unittest.main()