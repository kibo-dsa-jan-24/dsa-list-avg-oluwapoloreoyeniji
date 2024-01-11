import unittest
import timeit
from listavg import ListAverage

class TestListAverage(unittest.TestCase):
    def test(self):
        lavg = ListAverage([1, 2, 3])
        assert lavg.compute_avg() == 2.0

    # add more unit tests below
    def test_add(self):
        ladd = ListAverage([1, 2, 3])

        ladd.add(4)
        assert ladd.lst == [1, 2, 3, 4]

        with self.assertRaises(TypeError):
            ladd.add()
    
    def test_compute_avg_faster(self):
        lavg = ListAverage([1, 2, 3])

        assert lavg.compute_avg_faster() == 2.0

        time_taken_slower = timeit.timeit(lavg.compute_avg, number=1)
        time_taken_faster = timeit.timeit(lavg.compute_avg_faster, number=1)
        assert time_taken_slower > time_taken_faster

if __name__ == '__main__':
    unittest.main()
        