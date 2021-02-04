from Question import Question
from Expression import Int, Plus, Equals, Var

questions = [
    Question("How do you write '1 = 1' using Equals?", lambda a: a == Equals(Int(1), Int(1))),
    Question("Is 1 = 1 True or False?", lambda a: a),
    Question("How do you write '(1 + 2) + 3 = 1 + (2 + 3)' using Equals?", lambda a: a == Equals(Plus(Plus(Int(1), Int(2)), Int(3)), Plus(Int(1), Plus(Int(2), Int(3))))),
    Question("Is (1 + 2) + 3 = 1 + (2 + 3) True or False?", lambda a: a),
    Question("How do you write 'x' using Var?", lambda a: a == Var("x")),
    Question("How do you write 'y' using Var?", lambda a: a == Var("y")),
    Question("How do you write 'y = x + 19' using Var?", lambda a: a == Equals(Var("y"), Plus(Var("x"), Int(19)))),
    Question("If a = 1, what is another way of writing 'a'?", lambda a: a == Int(1)),
    Question("If a = 1, what is another way of writing 'b'?", lambda a: a == Var("b")),
    Question("If x = 3, what is another way of writing 'x + y?'", lambda a: a == Plus(Int(3), Var("y"))),
    Question("Use substitute to make '11 + a = 17' True", lambda a: a == Equals(Plus(Int(11), Int(6)), Int(17))),
    Question("Use substitute to make '30 + 50 = x' True", lambda a: a == Equals(Plus(Int(30), Int(50)), Int(80)))
]