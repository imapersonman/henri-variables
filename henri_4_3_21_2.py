from henri_4_8_21 import questions, documentation
from QuestionMachine import QuestionMachine
from Expression import Int, Var, Plus, Minus, Times, Equals, Negative

qm = QuestionMachine(questions)



qm.ask()

expr = Plus(Var("n"), Var("n"))
qm.check(expr.combine_like_terms(Var("n")))
qm.check(Plus(Int(1), Int(1)).combine_like_terms(Int(1)))
expr = Plus(Var("n"), Plus(Var("n"), Var("n")))
qm.check(expr.combine_like_terms(Var("n")))
expr = Plus(Plus(Var("n"), Var("n")), Var("n"))
qm.check(expr.combine_like_terms(Var("n")))
qm.check(Plus(Var("a"), Times(Int(4), Var("a"))).combine_like_terms(Var("a")))
expr = Plus(Var("a"), Times(Var("a"), Int(4)))
qm.check(expr.sub_comm(Times(Var("a"), Int(4))).combine_like_terms(Var("a")))
expr = Plus(Times(Int(3), Var("a")), Times(Var("a"), Int(4)))
qm.check(expr.sub_comm(Times(Var("a"), Int(4))).combine_like_terms(Var("a")))
expr = Plus(Plus(Int(3), Var("a")), Times(Var("a"), Int(4)))
qm.check(expr.sub_comm(Times(Var("a"), Int(4))).alr().combine_like_terms(Var("a")))