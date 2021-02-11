import unittest
from Expression import Var, Int, Plus, Minus, Equals, Times

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
    
    def test_substitute(self):
        self.assertEqual(a.substitute(b, i_1), a)
        self.assertEqual(a.substitute(a, i_1), i_1)
        self.assertEqual(Plus(a, b).substitute(a, i_1), Plus(i_1, b))
        self.assertEqual(Plus(a, b).substitute(b, i_1), Plus(a, i_1))
        self.assertEqual(Equals(a, b).substitute(a, i_1), Equals(i_1, b))
        self.assertEqual(Equals(a, b).substitute(b, i_1), Equals(a, i_1))
    
    def test_evaluate_subexpression(self):
        i_P_10_12 = Plus(Int(10), Int(12))
        # Replace subexpression fails no var replacement (should use substitute)
        # with self.assertRaises(Exception):
        #     Var("a").rewrite_subexpression(Var("a"), Int(2))
        # Atomic replace subexpression within atomic expression
        self.assertEqual(Int(12).rewrite_subexpression(Int(12), Int(12)), Int(12))
        # Atomic replace subexpression doesn't exist within atomic expression
        self.assertEqual(Int(12).rewrite_subexpression(Int(13), Int(12)), Int(12))
        # Atomic replace subexpression with unequivalent within atomic expression
        self.assertEqual(Int(12).rewrite_subexpression(Int(12), Int(13)), Int(12))
        # Atomic replace subexpression with non-atomic expression
        self.assertEqual(Int(12).rewrite_subexpression(Int(12), Plus(Int(3), Int(9))), Plus(Int(3), Int(9)))
        # Atomic replace subexpression within non-atomic expression
        self.assertEqual(Plus(Int(10), Int(12)).rewrite_subexpression(Int(12), Plus(Int(3), Int(9))), Plus(Int(10), Plus(Int(3), Int(9))))
        # Non-atomic replace subexpression
        self.assertEqual(i_P_10_12.rewrite_subexpression(i_P_10_12, Int(22)), Int(22))
        # Non-atomic replace subexpression doesn't exist within non-atomic expression
        self.assertEqual(i_P_10_12.rewrite_subexpression(Int(13), Int(13)), i_P_10_12)
        # Non-atomic replace subexpression with unequivalent within non-atomic expression
        self.assertEqual(Plus(Int(10), Plus(Int(11), Int(12))).rewrite_subexpression(Plus(Int(11), Int(12)), Int(22)), Plus(Int(11), Int(12)))
    
