from Question import Question
from Expression import Int, Plus, Equals, Var

a = Var("a")

questions = [
    Question("How do you write '10' using Int?", lambda a: a == Int(10)),
    Question("How do you write '812' using Int?", lambda a: a == Int(812)),
    Question("How do you write '-812' using Int?", lambda a: a == Int(-812)),
    Question("How do you write '1,000' using Int?", lambda a: a == Int(1000)),
    Question("How do you write '4 + 5' using Plus?", lambda a: a == Plus(Int(4), Int(5))),
    Question("How do you write '4 + -5' using Plus?", lambda a: a == Plus(Int(4), Int(-5))),
    Question("How do you write '(1 + 2) + 3' using Plus?", lambda a: a == Plus(Plus(Int(1), Int(2)), Int(3))),
    Question("What is '(1 + 2) + 3' equal to?", lambda a: a == 6),
    Question("How do you write '1 + (2 + 3)' using Plus?", lambda a: a == Plus(Int(1), Plus(Int(2), Int(3)))),
    Question("What is '1 + (2 + 3)' equal to?", lambda a: a == 6),
    Question("How do you write '1 = 2' using Equals?", lambda a: a == Equals(Int(1), Int(2))),
    Question("Is 1 = 2 True or False?", lambda a: a == False),
    Question("How do you write '1 = 1' using Equals?", lambda a: a == Equals(Int(1), Int(1))),
    Question("Is 1 = 1 True or False?", lambda a: a),
    Question("How do you write '(1 + 2) + 3 = 1 + (2 + 3)' using Equals?", lambda a: a == Equals(Plus(Plus(Int(1), Int(2)), Int(3)), Plus(Int(1), Plus(Int(2), Int(3))))),
    Question("Is (1 + 2) + 3 = 1 + (2 + 3) True or False?", lambda a: a),
    Question("How do you write 'x' using Var?", lambda a: a == Var("x")),
    Question("How do you write 'y' using Var?", lambda a: a == Var("y")),
    Question("How do you write 'y = x + 19' using Var?", lambda a: a == Equals(Var("y"), Plus(Var("x"), Int(19)))),
    Question("If a = 1, what is another way of writing 'a'?", lambda a: a == Int(1)),
    Question("If a = 1, what is another way of writing 'b'?", lambda a: a == Var("b")),
    Question("If x = 3, what is another way of writing 'x + y?'", lambda a: a == Plus(Int(3), Var("y")))
]