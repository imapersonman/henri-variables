from Question import Question
from Expression import Int, Plus, Equals, Var, Minus, Times

def check_q(i):
    return lambda a: a == i

def check_q_table(expr, pairs):
    table = dict(pairs)
    return lambda a: a == table

def eval_in_for(se, e, v, n, answer):
    return Question("Rewrite the expression '{}' in '{}' for {} = {}".format(se, e, v, n), check_q(answer))

def eval_in(se, e, answer):
    return Question("Rewrite the expression '{}' in '{}'".format(se, e), check_q(answer))

questions = [
    eval_in_for("3 * r", "21 + (3 * r)", "r", 1, Plus(Int(21), Int(3))),
    eval_in("21 + 3", "21 + 3", Int(24)),
    eval_in_for("3 * r", "21 + (3 * r)", "r", 2, Plus(Int(21), Int(6))),
    eval_in("21 + 6", "21 + 6", Int(27)),
    eval_in_for("3 * r", "21 + (3 * r)", "r", 3, Plus(Int(21), Int(9))),
    eval_in("21 + 9", "21 + 9", Int(30)),
    eval_in_for("3 * r", "21 + (3 * r)", "r", 7, Plus(Int(21), Int(21))),
    eval_in("21 + 21", "21 + 21", Int(42)),
    eval_in_for("3 * r", "21 + (3 * r)", "r", 20, Plus(Int(21), Int(60))),
    eval_in("21 + 60", "21 + 60", Int(81)),
    eval_in_for("3 * r", "21 + (3 * r)", "r", 50, Plus(Int(21), Int(150))),
    eval_in("21 + 150", "21 + 150", Int(171)),
    Question(
        "Make a dictionary of '21 + (3 * r)' for r = 1, 2, 3, 7, 20, and 50",
        check_q_table(
            Plus(Int(21), Times(Int(3), Var("r"))),
            [[Int(1), Int(24)], [Int(2), Int(27)], [Int(3), Int(30)], [Int(7), Int(42)], [Int(20), Int(81)], [Int(50), Int(171)]])),
    eval_in_for("45 - w", "2 * (45 - w)", "w", 1, Times(Int(2), Int(44))),
    eval_in("2 * 44", "2 * 44", Int(88)),
    eval_in_for("45 - w", "2 * (45 - w)", "w", 2, Plus(Int(21), Int(43))),
    eval_in("2 * 43", "2 * 43", Int(27)),
    eval_in_for("45 - w", "2 * (45 - w)", "w", 3, Plus(Int(21), Int(42))),
    eval_in("2 * 42", "2 * 42", Int(30)),
    eval_in_for("45 - w", "2 * (45 - w)", "w", 15, Plus(Int(21), Int(30))),
    eval_in("2 * 30", "2 * 30", Int(42)),
    eval_in_for("45 - w", "2 * (45 - w)", "w", 20, Plus(Int(21), Int(25))),
    eval_in("2 * 25", "2 * 25", Int(81)),
    eval_in_for("45 - w", "2 * (45 - w)", "w", 35, Plus(Int(21), Int(10))),
    eval_in("2 * 10", "2 * 10", Int(171)),
    Question(
        "Make a dictionary of '2 * (45 - w)' for k = 1, 2, 3, 15, 20, and 35",
        check_q_table(
            Plus(Int(21), Times(Int(3), Var("r"))),
            [[Int(1), Int(88)], [Int(2), Int(86)], [Int(3), Int(84)], [Int(15), Int(60)], [Int(20), Int(50)], [Int(35), Int(20)]]))
]