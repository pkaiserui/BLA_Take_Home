import unittest
import numpy as np
from land_BFS import BarrenLandBFS


class TestMakeLand(unittest.TestCase):

    def setUp(self):
        self.BFS = BarrenLandBFS([], 5, 10)

    def test_land_dimensions(self):
        self.assertEqual(
            (len(self.BFS.land), len(self.BFS.land[0])),
            (10,5)
        )

    def test_land_entries(self):
        self.assertEqual(self.BFS.land[0][0], 0)

class TestBFS(unittest.TestCase):

    def test_empty_small_plot(self):
        empty_small_BFS = BarrenLandBFS([], 15, 15)
        self.assertEqual(empty_small_BFS.bfs(0,0), 225)

    def test_empty_large_plot(self):
        empty_large_BFS = BarrenLandBFS([], 400, 600)
        self.assertEqual(empty_large_BFS.bfs(0,0), 240000)

    def test_starting_barren_land(self):
        barren_BFS = BarrenLandBFS([[0, 3, 4, 4]], 6,6)
        self.assertEqual(barren_BFS.bfs(0,3), 0)

    def test_running_into_barren(self):
        barren_BFS = BarrenLandBFS([[0, 3, 3, 4]], 5, 10)
        self.assertEqual(barren_BFS.bfs(0,0), 42)

class TestBuildCoordList(unittest.TestCase):

    def test_single_coord_list(self):
        BFS = BarrenLandBFS([[0, 3, 3, 7]])
        self.assertEqual(
            BFS.coord_list, [{
                'x0': 0,
                'y0': 3,
                'x1': 3,
                'y1': 7
            }]
        )

    def test_multi_coord_list(self):
        BFS = BarrenLandBFS([[4, 2, 2, 8],[3, 6, 6, 20]])
        self.assertEqual(
            BFS.coord_list,[{
                'x0': 4,
                'y0': 2,
                'x1': 2,
                'y1': 8
            },
            {
                'x0': 3,
                'y0': 6,
                'x1': 6,
                'y1': 20
            }]
        )

class TestPopulateBarrenLand(unittest.TestCase):

    def test_barren_land(self):
        BLS = BarrenLandBFS([[0, 1, 3, 2]], 4, 5)
        self.assertEqual(((BLS.land) == ([[0]*4, [-1]*4, [-1]*4, [0]*4, [0]*4])).all(),True)



class TestFindFertileArea(unittest.TestCase):

    def test_empty_case(self):
        BFS = BarrenLandBFS([])
        self.assertEqual(BFS.find_fertile_areas(), [240000])

    def test_example_case_1(self):
        BFS = BarrenLandBFS([[0, 292, 399, 307]])
        self.assertEqual(BFS.find_fertile_areas(), [116800, 116800])

    def test_example_case_2(self):
        BFS = BarrenLandBFS([[48, 192, 351, 207],
                                [48, 392, 351, 407],
                                [120, 52, 135, 547],
                                [260, 52, 275, 547]])
        self.assertEqual(BFS.find_fertile_areas(), [22816, 192608])

if __name__ == '__main__':
    unittest.main()
