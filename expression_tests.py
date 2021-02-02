import unittest
from Expression import *

i_1, i_2, i_n2, i_3, i_4, i_5, i_6, i_7 = Int(1), Int(2), Int(-2), Int(3), Int(4), Int(5), Int(6), Int(7)
a, b, c, x, y, z, cool = Var("a"), Var("b"), Var("c"), Var("x"), Var("y"), Var("z"), Var("cool")
i_P_1_2 = Plus(i_1, i_2)
i_P_n2_3 = Plus(i_n2, i_3)
i_P_nested = Plus(i_P_1_2, i_P_n2_3)
b_2_E_3 = Equals(i_2, i_3)
b_P_a_3_E_P_n2_3 = Equals(Plus(a, i_3), i_P_n2_3)

class TestRepresentation(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(i_1.__repr__(), "1")
        self.assertEqual(i_n2.__repr__(), "-2")
        self.assertEqual(a.__repr__(), "a")
        self.assertEqual(cool.__repr__(), "cool")
    
    def test_plus(self):
        self.assertEqual(i_P_1_2.__repr__(), "1 + 2")
        self.assertEqual(i_P_nested.__repr__(), "(1 + 2) + (-2 + 3)")
    
    def test_equals(self):
        self.assertEqual(b_2_E_3.__repr__(), "2 = 3")
        self.assertEqual(b_P_a_3_E_P_n2_3.__repr__(), "a + 3 = -2 + 3")
    
