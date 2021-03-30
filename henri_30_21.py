from Question import Question
from Expression import Int, Negative, Plus, Var, Equals, Minus, Times

def check_answer(a0):
    return lambda a: a == a0

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
    "expr.remove_add_zeroes(): Removes all zeroes being added inside of expr",
    # "expr.plus_to_times(): Changes all subexpressions of the form 'n + n + ... + n' to 'm * n'",
    # "expr.both_sides_plus(expr_to_add): Adds expr_to_add to both sides of the equal sign",
    # "expr.both_sides_minus(expr_to_add): Adds expr_to_add to both sides of the equal sign"
]

quesitons = [
    Question("What is the result of '3 - 5'.pn() using Expressions?", check_answer(Plus(Int(3), Negative(Int(5))))),
    Question("What is the result of calling '3 + -5'.pn() using Expressions?", check_answer(Plus(Int(3), Negative(Int(5))))),
    Question("What is the result of calling '(2 - 3) + 6'.comm() using Expressions?", check_answer(Plus(Int(6), Minus(Int(2), Int(3))))),
    Question("What is the result of calling '(2 - 3) + 6'.mz() using Expressions?", check_answer(Plus(Minus(Int(2), Int(3)), Int(6)))),
    Question("What is the result of calling '(2 - 3) + 6'.sub_comm('2 - 3') using Expressions?", check_answer(Plus(Minus(Int(2), Int(3)), Int(6)))),
    Question("What is the result of calling '(2 - 2) + 6'.mz() using Expressions?", check_answer(Plus(Minus(Int(2), Int(3)), Int(6)))),
    Question("What is the result of calling '(2 + 3) - 6'.comm() using Expressions?", check_answer(Minus(Plus(Int(2), Int(3)), Int(6)))),
    Question("What is the result of calling '(2 + 3) - 6'.sub_comm('2 + 3') using Expressions?", check_answer(Minus(Plus(Int(3), Int(2)), Int(6)))),
    Question("What is the result of calling '(2 - 2) + 6'.sub_mz('2 - 2') using Expressions?", check_answer(Plus(Int(0), Int(6)))),
]