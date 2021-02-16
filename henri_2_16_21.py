from Question import Question
from Expression import Int, Plus, Equals, Var, Minus, Times

def check_q(i):
    return lambda a: a == i

def check_q_table(expr, pairs):
    table = dict(pairs)
    return lambda a: a == table

questions = [
    Question("Evaluate 'c * 7' when c = 9 // copy-paste Times(Var(\"c\"), Int(7))", check_q(63)),
    Question("Evaluate '3 * (w - 62)' when w = 71 // copy-paste Times(Int(3), Minus(Var(\"w\"), Int(62)))", check_q(27)),
    Question("Evaluate 'd + (3 * 20)' when d = 12 // copy-paste Plus(Var(\"d\"), Times(Int(3), Int(20)))", check_q(72)),
    Question(
        "Make a dictionary of '7 + a' for a = 1, 2, 3, 9, 41, and 132",
        check_q_table(
            Plus(Int(7), Var("a")),
            [[Int(1), Int(8)], [Int(2), Int(9)], [Int(3), Int(10)], [Int(9), Int(16)], [Int(41), Int(48)], [Int(132), Int(139)]])),
    Question(
        "Make a dictionary of '86 - d' for d = 1, 2, 3, 16, 55, and 79",
        check_q_table(
            Minus(Int(7), Var("a")),
            [[Int(1), Int(85)], [Int(2), Int(84)], [Int(3), Int(83)], [Int(16), Int(70)], [Int(55), Int(31)], [Int(79), Int(7)]])),
    Question(
        "Make a dictionary of 'k * 4' for k = 1, 2, 3, 8, 40, and 70",
        check_q_table(
            Times(Var("k"), Int(4)),
            [[Int(1), Int(4)], [Int(2), Int(8)], [Int(3), Int(12)], [Int(8), Int(32)], [Int(40), Int(160)], [Int(70), Int(280)]])),
    Question(
        "Make a dictionary of '(6 * m) - 3' for m = 1, 2, 3, 6, 50, and 100",
        check_q_table(
            Minus(Times(Int(6), Var("m")), Int(3)),
            [[Int(1), Int(3)], [Int(2), Int(9)], [Int(3), Int(15)], [Int(6), Int(33)], [Int(50), Int(297)], [Int(100), Int(597)]])),
    Question(
        "Make a dictionary of '21 + (3 * r)' for r = 1, 2, 3, 7, 20, and 50",
        check_q_table(
            Plus(Int(21), Times(Int(3), Var("r"))),
            [[Int(1), Int(24)], [Int(2), Int(27)], [Int(3), Int(30)], [Int(7), Int(42)], [Int(20), Int(81)], [Int(50), Int(171)]])),
    Question(
        "Make a dictionary of '2 * (45 - w)' for k = 1, 2, 3, 15, 20, and 35",
        check_q_table(
            Plus(Int(21), Times(Int(3), Var("r"))),
            [[Int(1), Int(88)], [Int(2), Int(86)], [Int(3), Int(84)], [Int(15), Int(60)], [Int(20), Int(50)], [Int(35), Int(20)]]))
]
