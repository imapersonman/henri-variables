from Question import Question
from Expression import Int, Plus, Equals, Var, Minus, Times, Negative
import re

def remove_all_whitespace(s):
    return re.sub(r"\s+", "", s, flags=re.UNICODE)

def check_or_answer(a1, a2):
    return lambda a: a == a1 or a == a2

def check_answer(a0):
    return lambda a: a == a0

def check_str_no_ws(a0):
    return lambda a: remove_all_whitespace(a) == remove_all_whitespace(a0)

def conv_q(expr1_str, expr2_str, af):
    return Question("Convert the expression '{}' to '{}'".format(expr1_str, expr2_str), af)

documentation = [
    "expr.to_pos_neg(): If expr looks like 'a - b', it is converted to 'a + -b'",
    "expr.pos_neg_to_minus(): If expr looks like 'a + -b', it is converted to 'a - b'",
    "expr.associate_l_to_r(): If expr looks like '(a + b) + c', it is converted to 'a + (b + c)'.  You can replace '+' with '*'.",
    "Expression.associate_r_to_l(): Converts an expression that looks like 'a + (b + c)' to '(a + b) + c'.  You can replace '+' with '*'",
    "Expression.rewrite_subexpression(sub_expr, equal_expr): "
]

# I need to teach Henri the associative property at some point, but I won't today.
# Actually, I might need to.  Teaching it would be simplified if Henri had the option to convert all subtractions to
# +-s.  Fpr example, (11 + n) - n would become (11 + n) + -n.  The associative property can then be used to turn the
# expression into (11)

questions = [
    # (1 + 2) + 3 --> 1 + (2 + 3)
    conv_q("(1 + 2) + 3", "1 + (2 + 3)", check_answer(Plus(Int(1), Plus(Int(2), Int(3))))),
    # 9 - 4 --> 9 + -4
    conv_q("9 - 4", "9 + -4", check_answer(Plus(Int(9), Negative(Int(4))))),
    # (a + -4) + -8 --> (a - 4) - 8
    conv_q("(a + -4) + -8", "(a - 4) - 8", check_answer(Minus(Minus(Var("a"), Int(4)), Int(8)))),
    # 1 + (2  - 3) --> 1 + (2 + -3) --> 1 + (2 - 3)
    conv_q("1 + (2 - 3)", "(1 + 2) - 3", check_answer(Minus(Plus(Int(1), Int(2)), Int(3)))),
    # (1 - 2) - 3 --> (1 + -2) + -3 --> 1 + (-2 + -3) --> 1 + (-2 - 3)
    conv_q("(1 - 2) - 3", "1 + (-2 - 3)", check_answer(Plus(Int(1), Minus(Negative(Int(2)), Int(3))))),
    # (a + 4) + (3 - 2) --> (a + 4) + (3 + -2) --> ((a + 4) + 3) + -2 --> ((a + 4) + 3) - 2
    conv_q("(a + 4) + (3 - 2)", "((a + 4) + 3) - 2)", check_answer(Minus(Plus(Plus(Var("a"), Int(4)), Int(3)), Int(2)))),
    # 1 + ((2 + 3) + 4) --> 1 + (2 + (3 + 4))
    conv_q("1 + ((2 + 3) + 4)", "1 + (2 + (3 + 4))", check_answer(Plus(Int(1), Plus(Int(2), Plus(Int(3), Int(4))))))
]