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
    "expr.remove_add_zeroes(): Removes all zeroes being added inside of expr",
    "expr.combine_like_terms(): Changes all subexpressions of the form 'n + n + ... + n' to 'm * n'",
    # "expr.both_sides_plus(expr_to_add): Adds expr_to_add to both sides of the equal sign",
    "expr.both_sides_minus(expr_to_add): Adds expr_to_add to both sides of the equal sign"
]

def check_or_answer(a1, a2):
    return lambda a: a == a1 or a == a2

def check_answer(a0):
    return lambda a: a == a0

def conv_q(expr1_str, expr2_str, af):
    return Question("Convert the expression '{}' to '{}'".format(expr1_str, expr2_str), af)

def simp_q(expr_str, af):
    return Question("Simplify the expression '{}'".format(expr_str), af)

def solve_q(start_str, v, af):
    return Question("Solve for '{}' in '{}'".format(v, start_str), af)

questions = [
    # solve_q("x = 3", Var("x"), check_answer(Equals(Var("x"), Int(3)))),
    # solve_q("x + n = n", Var("x"), check_answer(Equals(Var("x"), Int(0)))),
    conv_q("n + n", "2 * n", check_answer(Times(Int(2), Var("n")))),
    conv_q("1 + 1", "2 * 1", check_answer(Times(Int(2), Int(1)))),
    conv_q("n + (n + n)", "3 * n", check_answer(Times(Int(3), Var("n")))),
    conv_q("(n + n) + n", "3 * n", check_answer(Times(Int(3), Var("n")))),
    conv_q("a + (4 * a)", "5 * a", check_answer(Times(Int(5), Var("a")))),
    conv_q("a + (a * 4)", "5 * a", check_answer(Times(Int(5), Var("a")))),
    conv_q("(3 + a) + (a * 4)", "7 * a", check_answer(Times(Int(7), Var("a")))),
]