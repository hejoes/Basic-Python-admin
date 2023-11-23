import unittest
from koordinaadid_hejoes.konverter import *

import warnings
warnings.filterwarnings("ignore") 

class Testing(unittest.TestCase):
    def test_1(self):
        self.assertEqual(wgs84_to_est(59.395312, 24.664182), (6584338.656, 537735.467))
        
    def test_2(self):
        self.assertEqual(est_to_wgs84(6584338, 537735), (59.395, 24.664))
        
    
if __name__ == "__main__":
    unittest.main()