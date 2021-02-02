class Expression:
    def __init__(self):
        pass

    def interpret(self):
        raise Exception("interpret unimplemented")

class InterpreterError:
    def __init__(self, msg):
        self.msg = msg
    
    def __repr__(self):
        return "Error: {}".format(self.msg)

class IntExpression(Expression):
    def __init__(self):
        self.type = "int"

class Int(IntExpression):
    def __init__(self, value: int):
        super().__init__()
        self.value = value
    
    def interpret(self):
        return self.value
    
    def __repr__(self):
        return "{}".format(self.value)

class Plus(IntExpression):
    def __init__(self, l: IntExpression, r: IntExpression):
        super().__init__()
        self.l = l
        self.r = r
        if (not isinstance(self.l, Expression)):
            raise Exception("{} is not an Expression!".format(self.l))
        if (not isinstance(self.r, Expression)):
            raise Exception("{} is not an Expression!".format(self.r))
    
    def interpret(self):
        l_interpreted = self.l.interpret()
        if (type(l_interpreted) == InterpreterError):
            return l_interpreted
        if (type(l_interpreted) != int):
            return InterpreterError("'{}' interprets to '{}', which is not an integer.  Only integers can be added.".format(self.l, l_interpreted))
        r_interpreted = self.r.interpret()
        if (type(r_interpreted) == InterpreterError):
            return r_interpreted
        if (type(l_interpreted) != int):
            return InterpreterError("'{}' interprets to '{}', which is not an integer.  Only integers can be added.".format(self.r, r_interpreted))
        return l_interpreted + r_interpreted
    
    def __repr__(self):
        l_repr = "({})".format(self.l) if type(self.l) == Plus else self.l
        r_repr = "({})".format(self.r) if type(self.r) == Plus else self.r
        return "{} + {}".format(l_repr, r_repr)

class BooleanExpression(Expression):
    def __init__(self):
        self.type = "boolean"

class Equals(BooleanExpression):
    def __init__(self, l: Expression, r: Expression):
        super().__init__()
        self.l = l
        self.r = r
    
    def interpret(self):
        l_interpreted = self.l.interpret()
        if (type(l_interpreted) == InterpreterError):
            return l_interpreted
        r_interpreted = self.r.interpret()
        if (type(r_interpreted) == InterpreterError):
            return r_interpreted
        return l_interpreted == r_interpreted
    
    def __repr__(self):
        l_repr = "({})".format(self.l) if type(self.l) == Equals else self.l
        r_repr = "({})".format(self.r) if type(self.r) == Equals else self.r
        return "{} = {}".format(l_repr, r_repr)

class Var(Expression):
    def __init__(self, id: str):
        super().__init__()
        self.id = id
    
    def interpret(self):
        return InterpreterError("{} cannot be interpreted".format(self))

    def __repr__(self):
        return str(self.id)