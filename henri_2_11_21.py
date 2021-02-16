# We'll start evaluating expressions in today's session, I'm not sure how to do that.
#
from Question import Question
from Expression import Int, Plus, Equals, Var, Minus

def check_q(i):
    return lambda a: a == i

questions = [
    # Evaluate 12 + a when a = 4.
    # 12 + a = 12 + 4 = 16
    # (12 + a).substitute(a, 4).evaluate_subexpression(12 + 4, 16)
    Question("Evaluate '12 + a' when a = 4 // copy-paste Plus(Int(12), Var(\"a\"))", check_q(16)),
    # Evaluate 14 - b when b = 3.
    # 14 - b = 14 - 3 = 11
    # (14 - b).substitute(b, 3).evaluate_subexpression(14 - 3, 11)
    Question("Evaluate '14 - b' when b = 3 // copy-paste Minus(Int(14), Var(\"b\"))", check_q(11)),
    # Evaluate n - 4 when n = 9.
    # n - 4 = 9 - 4 = 5
    # (n - 4).substitute(n, 9).evaluate_subexpression(9 - 4, 5)
    Question("Evaluate 'n - 4' when n = 9 // copy-paste Minus(Var(\"n\"), Int(4))", check_q(5)),
    # Evaluate 2 * 14 - z when z = 6.
    # 2 * 14 - z = 2 * 14 - 6 = 28 - 6 = 22
    # (2 * 14 - z).substitute(z, 6).evaluate_subexpression(2 * 14, 28).evaluate_subexpression(28 - 6, 22)
    Question("Evaluate '(2 * 14) - z' when z = 6 // copy-paste Minus(Times(Int(2), Int(14)), Var(\"z\"))", check_q(22)),
    # Evaluate 12 + 18 - s when s = 5.
    # 12 + 18 - s = 12 + 18 - 5 = 30 - 5 = 25
    # (12 + 18 - s).substitute(s, 5).evaluate_subexpression(12 + 18, 30).evaluate_subexpression(30 - 5, 25)
    Question("Evaluate '(12 + 18) - s' when s = 5 // copy-paste Minus(Plus(Int(12), Int(18)), Var(\"s\"))", check_q(25)),
    # Evaluate c * 7 when c = 9.
    # c * 7 = 9 * 7 = 63
    # (c * 7).substitute(c, 9).evaluate_subexpression(9 * 7, 63)
    Question("Evaluate 'c * 7' when c = 9 // copy-paste Times(Var(\"c\"), Int(7))", check_q(63)),
    # Evaluate 3 * (w - 62) when w = 71.
    # 3 * (w - 62) = 3 * (71 - 62) = 3 * 9 = 27
    # (3 * (w - 62)).substitute(w, 71).evaluate_subexpression(71 - 62, 9).evaluate_subexpression(3 * 9, 27)
    Question("Evaluate '3 * (w - 62)' when w = 71 // copy-paste Times(Int(3), Minus(Var(\"w\"), Int(62)))", check_q(27)),
    # Evaluate d + 3 * 20 when d = 12.
    # d + 3 * 20 = 12 + 3 * 20 = 12 + 60 = 72
    # (d + 3 * 20).substitute(d, 12).evaluate_subexpression(3 * 20, 60).evaluate_subexpression(12 + 60, 72)
    Question("Evaluate 'd + (3 * 20)' when d = 12 // copy-paste Plus(Var(\"d\"), Times(Int(3), Int(20)))", check_q(72))
]
