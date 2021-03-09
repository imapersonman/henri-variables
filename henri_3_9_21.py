from Question import Question
from Expression import Int, Plus, Equals, Var, Minus, Times, Negative

def check_or_answer(a1, a2):
    return lambda a: a == a1 or a == a2

def check_answer(a0):
    return lambda a: a == a0

def conv_q(expr1_str, expr2_str, af):
    return Question("Convert the expression '{}' to '{}'".format(expr1_str, expr2_str), af)

documentation = [
    "expr.to_pos_neg(): If expr looks like 'a - b', it is converted to 'a + -b'",
    "expr.pos_neg_to_minus(): If expr looks like 'a + -b', it is converted to 'a - b'",
    "expr.associate_l_to_r(): If expr looks like '(a + b) + c', it is converted to 'a + (b + c)'.  You can replace '+' with '*'.",
    "expr.associate_r_to_l(): Converts an expression that looks like 'a + (b + c)' to '(a + b) + c'.  You can replace '+' with '*'",
    "expr.rewrite_subexpression(sub_expr, equal_expr): Rewrites every expression equal to subexpr inside of expr to equal_expr, but only if equal_expr means the same thing as sub_expr."
]

# I need to teach Henri the associative property at some point, but I won't today.
# Actually, I might need to.  Teaching it would be simplified if Henri had the option to convert all subtractions to
# +-s.  Fpr example, (11 + n) - n would become (11 + n) + -n.  The associative property can then be used to turn the
# expression into (11)

questions = [
     # 1 + (2  - 3) --> 1 + (2 + -3) --> 1 + (2 - 3)
    conv_q("1 + (2 - 3)", "(1 + 2) - 3", check_answer(Minus(Plus(Int(1), Int(2)), Int(3)))),
    # (1 * 2) * 3 --> 1 * (2 * 3)
    conv_q("(1 * 2) * 3", "1 * (2 * 3)", check_answer(Times(Int(1), Times(Int(2), Int(3))))),
    # (1 * -2) * 3 --> 1 * (-2 * 3)
    conv_q("(1 * -2) * 3", "1 * (-2 * 3)", check_answer(Times(Int(1), Times(Negative(Int(2)), Int(3))))),
    # 1 * ((2 * 3) * 4) --> (1 * (2 * 3)) * 4
    conv_q("1 * ((2 * 3) * 4)", "(1 * (2 * 3)) * 4", check_answer(Times(Times(Int(1), Times(Int(2), Int(3))), Int(4)))),
    # 1 * (2 * (3 * 4)) --> 1 * ((2 * 3) * 4) --> (1 * (2 * 3)) * 4
    conv_q("1 * (2 * (3 * 4))", "(1 * (2 * 3)) * 4", check_answer(Times(Times(Int(1), Times(Int(2), Int(3))), Int(4)))),
    # 1 * (2 * (3 * 4)) --> 1 * ((2 * 3) * 4) --> (1 * (2 * 3)) * 4 --> ((1 * 2) * 3) * 4
    conv_q("1 * (2 * (3 * 4))", "((1 * 2) * 3) * 4", check_answer(Times(Times(Times(Int(1), Int(2)), Int(3)), Int(4))))
]