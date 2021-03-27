from Question import Question
from Expression import Int, Plus, Equals, Var, Minus, Times, Negative

documentation = [
    "expr.pn(): same as expr.to_pos_neg()",
    "expr.pnm(): same as expr.pos_neg_to_minus()",
    "expr.alr(): same as expr.associate_l_to_r()",
    "expr.arl(): same as expr.associate_r_to_l()",
    "expr.comm(): same as expr.commute()",
    "expr.sub_alr(sub_expr): Changes sub_expr in expr using associate_l_to_r()",
    "expr.sub_arl(sub_expr): Changes sub_expr in expr using associate_r_to_l()",
    "expr.sub_comm(sub_expr): Changes sub_expr in expr using commute()",
    "expr.minus_to_zero(): If expr looks like 'n - n', it is converted to '0'",
    "expr.mz(): same as expr.minus_to_zero()",
    "expr.sub_mz(): Changes sub_expr in expr using minus_to_zero()",
    "expr.remove_add_zeroes(): Removes all zeroes being added inside of expr"
]

def check_answer(a0):
    return lambda a: a == a0

def conv_q(expr1_str, expr2_str, af):
    return Question("Convert the expression '{}' to '{}'".format(expr1_str, expr2_str), af)

questions = [
    conv_q("1 + (2 + (3 + 4))", "1 + ((2 + 3) + 4)", check_answer(Plus(Int(1), Plus(Plus(Int(2), Int(3)), Int(4))))),
    conv_q("1 + ((2 + 3) + 4)", "1 + (2 + (3 + 4))", check_answer(Plus(Int(1), Plus(Int(2), Plus(Int(3), Int(4)))))),
    conv_q("(2 + 1) + 3", "(1 + 2) + 3", check_answer(Plus(Plus(Int(1), Int(2)), Int(3)))),
    conv_q("1 + (2 + 3)", "(2 + 1) + 3", check_answer(Plus(Plus(Int(2), Int(1)), Int(3)))),
    conv_q("1 - 1", "0", check_answer(Int(0))),
    conv_q("2 + 0", "2", check_answer(Int(2))),
    conv_q("-6 + 6", "0", check_answer(Int(0))),
    conv_q("(0 + 2) + 0", "2", check_answer(Int(2))),
    conv_q("2 + (1 - 1)", "2", check_answer(Int(2))),
    conv_q("-1 + (2 + 1)", "0", check_answer(Int(2))),
    conv_q("(-1 + 2) + (1 - 2)", "0", check_answer(Int(0))),
    conv_q("(1 + 2) + (3 + -1)", "2 + 3", check_answer(Plus(Int(2), Int(3)))),
]