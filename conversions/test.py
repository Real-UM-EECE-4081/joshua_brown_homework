from util import C_to_F, F_to_C 

import unittest

class TempUnitTest(unittest.TestCase):

    def test_F_to_C_absol_0(self):

        self.assertRaises(ValueError, F_to_C, -465)

  
    def test_C_tp_F_absol_0(self):

        self.assertRaises(ValueError, C_to_F, -275)

  
    def test_F_to_C_convert(self):

        test_temp = F_to_C(957.2)

        self.assertEqual(test_temp, 514, "Invalid Temperature")

  
    def test_C_to_F_convert(self):

        test_temp = C_to_F(-44)

        self.assertEqual(test_temp, -47.2, "Invalid Temperature")

unittest.main()