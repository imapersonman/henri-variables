from Question import Question
from Expression import Int, Plus, Equals, Var, Minus, Times, Negative

documentation = [
    "expr.to_pos_neg(): If expr looks like 'a - b', it is converted to 'a + -b'",
    "expr.pos_neg_to_minus(): If expr looks like 'a + -b', it is converted to 'a - b'",
    "expr.associate_l_to_r(): If expr looks like '(a + b) + c', it is converted to 'a + (b + c)'.  You can replace '+' with '*'.",
    "expr.associate_r_to_l(): Converts an expression that looks like 'a + (b + c)' to '(a + b) + c'.  You can replace '+' with '*'",
    "expr.rewrite_subexpression(sub_expr, equal_expr): Rewrites every expression equal to subexpr inside of expr to equal_expr, but only if equal_expr means the same thing as sub_expr.",
    "expr.commute(): If expr looks like 'a + b', it is converted to 'b + a'.  You can replace '+' with '*'"
]

def check_answer(a0):
    return lambda a: a == a0

def conv_q(expr1_str, expr2_str, af):
    return Question("Convert the expression '{}' to '{}'".format(expr1_str, expr2_str), af)

questions = [
    conv_q("1 * (2 * (3 * 4))", "((1 * 2) * 3) * 4", check_answer(Times(Times(Times(Int(1), Int(2)), Int(3)), Int(4)))),
    conv_q("5 + 6", "6 + 5", check_answer(Plus(Int(6), Int(5)))),
    conv_q("(2 + 3) + 1", "1 + (2 + 3)", check_answer(Plus(Int(1), Plus(Int(2), Int(3))))),
    conv_q("(2 + 3) + 1", "(3 + 2) + 1", check_answer(Plus(Plus(Int(3), Int(2)), Int(1)))),
    conv_q("-1 + 2", "2 - 1", check_answer(Minus(Int(2), Int(1)))),
    conv_q("(1 - 3) - 2", "(1 - 2) - 3", check_answer(Minus(Minus(Int(1), Int(2)), Int(3)))),
    conv_q("1 + (2 + 3)", "3 + (2 + 1)", check_answer(Plus(Int(3), Plus(Int(2), Int(1))))),
    conv_q("(-3 - 2) - 1", "(-1 - 2) - 3", check_answer(Minus(Minus(Negative(Int(1)), Int(2)), Int(3)))),
    conv_q("1 + (2 + (3 + 4))", "4 + (3 + (2 + 1))", check_answer(Plus(Int(4), Plus(Int(3), Plus(Int(2), Int(1))))))
]