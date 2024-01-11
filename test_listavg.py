import unittest
import time
from listavg import ListAverage

class TestListAverage(unittest.TestCase):
    def test(self):
        lavg = ListAverage([1, 2, 3])
        assert lavg.compute_avg() == 2.0

    # add more unit tests below
    def test_add(self):
        ladd = ListAverage([1, 2, 3])
        assert ladd.add(4) == [1, 2, 3, 4]
        assert ladd.add() == [1, 2, 3]
        assert ladd.add('d') == [1, 2, 3, 'd'] 
    
    def test_compute_avg_faster(self):
        lavg = ListAverage([1, 2, 3])
        start_faster = time.time()
        assert lavg.compute_avg_faster == 2.0
        end_faster = time.time()
        time_faster = end_faster - start_faster

        start_normal = time.time()
        lavg.compute_avg() == 2.0
        end_normal = time.time()
        time_normal = end_normal - start_normal

        assert time_faster > time_normal
        
