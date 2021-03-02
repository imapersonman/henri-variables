import unittest
from Expression import Var, Int, Plus, Minus, Equals, Times, Negative

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
    
    def test_to_pos_neg(self):
        self.assertEqual(Int(12).to_pos_neg(), Int(12))
        self.assertEqual(Var("a").to_pos_neg(), Int("a"))
        self.assertEqual(Negative(Int(12).to_pos_neg()), Negative(Int(12)))
        self.assertEqual(Plus(Int(3), Int(5)).to_pos_neg(), Plus(Int(3), Int(5)))
        self.assertEqual(Times(Int(3), Int(5)).to_pos_neg(), Times(Int(3), Int(5)))
        self.assertEqual(Minus(Int(3), Int(5)).to_pos_neg(), Plus(Int(3), Negative(Int(5))))
        self.assertEqual(Negative(Minus(Int(3), Int(5))).to_pos_neg(), Negative(Plus(Int(3), Negative(Int(5)))))
        self.assertEqual(Times(Minus(Int(3), Int(5)), Minus(Int(6), Int(7))).to_pos_neg(), Times(Plus(Int(3), Negative(Int(5))), Plus(Int(6), Negative(Int(7)))))
        self.assertEqual(Plus(Minus(Int(3), Int(5)), Minus(Int(6), Int(7))).to_pos_neg(), Plus(Plus(Int(3), Negative(Int(5))), Plus(Int(6), Negative(Int(7)))))
        self.assertEqual(Equals(Minus(Int(3), Int(5)), Minus(Int(6), Int(7))).to_pos_neg(), Equals(Plus(Int(3), Negative(Int(5))), Plus(Int(6), Negative(Int(7)))))
    
    def test_associate(self):
        self.assertEqual(Int(12).associate_l_to_r(), Int(12))
        self.assertEqual(Int(12).associate_r_to_l(), Int(12))
        self.assertEqual(Var("a").associate_l_to_r(), Var("a"))
        self.assertEqual(Var("a").associate_r_to_l(), Var("a"))
        self.assertEqual(Plus(Int(1), Int(2)).associate_l_to_r(), Plus(Int(1), Int(2)))
        self.assertEqual(Times(Int(1), Int(2)).associate_l_to_r(), Times(Int(1), Int(2)))
        # self.assertEqual(Plus(Int(1), Int(2)).associate_r_to_l(), Plus(Int(1), Int(2)))
        # self.assertEqual(Times(Int(1), Int(2)).associate_r_to_l(), Times(Int(1), Int(2)))
        # (1 + 2) + 3 -> 1 + (2 + 3)
        # self.assertEqual(Plus(Plus(Int(1), Int(2)), Int(3)).associate_l_to_r(), Plus(Int(1), Plus(Int(2), Int(3))))
        # 1 + (2 + 3) -> (1 + 2) + 3
        # self.assertEqual(Plus(Int(1), Plus(Int(2), Int(3))).associate_r_to_l(), Plus(Plus(Int(1), Int(2)), Int(3)))
        # (1 * 2) * 3 -> 1 * (2 * 3)
        # self.assertEqual(Times(Times(Int(1), Int(2)), Int(3)).associate_l_to_r(), Times(Int(1), Times(Int(2), Int(3))))
        # 1 * (2 * 3) -> (1 * 2) * 3
        # self.assertEqual(Times(Int(1), Times(Int(2), Int(3))).associate_r_to_l(), Times(Times(Int(1), Int(2)), Int(3)))
        # 1 - (2 - 3) -> 1 - (2 - 3)
        # self.assertEqual(Minus(Int(1), Minus(Int(2), Int(3))).associate_r_to_l(), Minus(Int(1), Minus(Int(2), Int(3))))
        # (1 - 2) - 3 -> (1 - 2) - 3
        # self.assertEqual(Minus(Minus(Int(1), Int(2)), Int(3)).associate_l_to_r(), Minus(Minus(Int(1), Int(2)), Int(3)))
        # # ((1 + (2 + 3)) * (1 + (2 + 3)))
        # self.assertEqual(Times(Plus(Int(1), Plus(Int(2), Int(3))), Plus(Int(1), Plus(Int(2), Int(3)))).associate_r_to_l(), Times(Plus(Int(1), Plus(Int(2), Int(3))), Plus(Int(1), Plus(Int(2), Int(3)))))
        # # (((1 + 2) + 3) * ((1 + 2) + 3))
        # self.assertEqual(Times(Plus(Plus(Int(1), Int(2)), Int(3)), Plus(Plus(Int(1), Int(2)), Int(3))).associate_l_to_r(), Times(Plus(Plus(Int(1), Int(2)), Int(3)), Plus(Plus(Int(1), Int(2)), Int(3))))
        # # ((1 + (2 + 3)) - (1 + (2 + 3)))
        # self.assertEqual(Minus(Plus(Int(1), Plus(Int(2), Int(3))), Plus(Int(1), Plus(Int(2), Int(3)))).associate_r_to_l(), Minus(Plus(Int(1), Plus(Int(2), Int(3))), Plus(Int(1), Plus(Int(2), Int(3)))))
        # # (((1 + 2) + 3) - ((1 + 2) + 3))
        # self.assertEqual(Minus(Plus(Plus(Int(1), Int(2)), Int(3)), Plus(Plus(Int(1), Int(2)), Int(3))).associate_l_to_r(), Minus(Plus(Plus(Int(1), Int(2)), Int(3)), Plus(Plus(Int(1), Int(2)), Int(3))))
