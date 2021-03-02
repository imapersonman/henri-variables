from Question import Question
from Expression import Int, Plus, Equals, Var, Minus, Times
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

extra_stuff = [
    Times(Times(Var("n"), Var("n")), Var("n")),
    Minus(Int("n"), Int("n")),
    Plus(Int(11), Minus(Var("n"), Var("n"))),
    Plus(Plus(Int(3), Int(1)), Var("d")),

]

documentation = [
    "Expression.to_pos_neg(): Converts an expression that looks like 'a - b' to 'a + -b'",
    "Expression.pos_neg_to_minus(): Converts an expression that looks like 'a + -b' to 'a - b'",
    "Expression.associate_l_to_r(): Converts an expression that looks like '(a + b) + c' to 'a + (b + c)'.  You can replace '+' with '*'",
    "Expression.associate_r_to_l(): Converts an expression that looks like 'a + (b + c)' to '(a + b) + c'.  You can replace '+' with '*'",
]

# I need to teach Henri the associative property at some point, but I won't today.
# Actually, I might need to.  Teaching it would be simplified if Henri had the option to convert all subtractions to
# +-s.  Fpr example, (11 + n) - n would become (11 + n) + -n.  The associative property can then be used to turn the
# expression into (11)

expression_map = {
    "4 - 3": Minus(Int(4), Int(3)),
    "6 - (3 - 4)": Minus(Int(6), Minus(Int(3), Int(4))),
    "1 + (2 + 3)": Plus(Int(1), Plus(Int(2), Int(3))),
    "(1 + 2) + (3 + 4)": Plus(Plus(Int(1), Int(2)), Plus(Int(3), Int(4)))
}

questions = [
    Question("What do you get when you call '3 - 4'.to_pos_neg()?", check_str_no_ws("3 + -4")),
    Question("What do you get when you call '6 - (3 - 4)'.to_pos_neg()?", check_str_no_ws("6 + -(3 + -4)")),
    Question("What do you get when you call '1 - (2 - (3 - 4))'.to_pos_neg()?", check_str_no_ws("1 + -(2 + -(3 + -4))")),
    Question("What do you get when you call '(1 + 2) + 3'.associate_l_to_r()", check_str_no_ws("1 + (2 + 3)")),
    Question("What do you get when you call '1 + (2 + 3)'.associate_r_to_l()", check_str_no_ws("(1 + 2) + 3")),
    Question("What do you get when you call '(a + 4) + (3 - 2)'.associate_l_to_r()", check_str_no_ws("a + (4 + (3 - 2))")),
    Question("What do you get when you call '(a + 4) + (3 - 2)'.associate_r_to_l()", check_str_no_ws("(a + 4) + (3 - 2)")),
    conv_q("1 + (2 - 3)", "(1 + 2) - 3", check_answer(Minus(Plus(Int(1), Int(2)), Int(3)))),
    conv_q('(a + 4) + (3 - 2)', '((a + 4) + 3) - 2)', check_answer(Minus(Plus(Plus(Var("a"), Int(4)), Int(3)), Int(2)))),
]