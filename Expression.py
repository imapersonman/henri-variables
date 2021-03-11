class Expression:
    def __init__(self):
        pass

    def interpret(self):
        raise Exception("interpret unimplemented")
    
    def substitute(self, v, expr):
        raise Exception("substitute unimplemented")

    def rewrite_subexpression(self, subexpression, equivalent):
        raise Exception("evalute_subexpression unimplemented")

    def pos_neg_to_minus(self):
        raise Exception("pos_neg_to_minus unimplemented")

    def to_pos_neg(self):
        raise Exception("to_pos_neg unimplemented")

    def associate_l_to_r(self):
        raise Exception("associate_l_to_r unimplemented")

    def associate_r_to_l(self):
        raise Exception("associate_r_to_l unimplemented")

    def to_python_string(self):
        raise Exception("to_python_string unimplemented")

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
        if value < 0:
            raise Exception("Int value must be greater than or equal to 0")
        self.value = value
    
    def interpret(self):
        return self.value
    
    def substitute(self, v, expr):
        return self

    def rewrite_subexpression(self, subexpression, equivalent):
        if subexpression == self and equivalent.interpret() == self.interpret():
            return equivalent
        return self
    
    def to_python_string(self):
        return "Int({})".format(self.value)
    
    def pos_neg_to_minus(self):
        return self
    
    def to_pos_neg(self):
        return self

    def associate_l_to_r(self):
        return self

    def associate_r_to_l(self):
        return self
    
    def __repr__(self):
        return "{}".format(self.value)
    
    def __eq__(self, other):
        return isinstance(other, Int) and self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
    
class Negative(IntExpression):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr
    
    def interpret(self):
        expr_interpreted = self.expr.interpret()
        if type(expr_interpreted) == InterpreterError:
            return expr_interpreted
        if (type(expr_interpreted) != int):
            return InterpreterError("'{}' interprets to '{}', which is not an integer.  Only integers can be combined with negative.".format(self.expr, expr_interpreted))
        return expr_interpreted

    def substitute(self, v, new_expr):
        return Negative(self.expr.substitute(v, new_expr))

    def pos_neg_to_minus(self):
        return Negative(self.expr.pos_neg_to_minus())

    def rewrite_subexpression(self, subexpression, equivalent):
        if subexpression == self and equivalent.interpret() == self.interpret():
            return equivalent
        return Negative(self.expr.rewrite_subexpression(subexpression, equivalent))
    
    def to_pos_neg(self):
        return Negative(self.expr.to_pos_neg())
    
    def to_python_string(self):
        return "Negative({})".format(self.expr.to_python_string())

    def associate_l_to_r(self):
        return self

    def associate_r_to_l(self):
        return self
    
    def __repr__(self):
        if isinstance(self.expr, BinaryExpression):
            return "-({})".format(self.expr)
        return "-{}".format(self.expr)
    
    def __eq__(self, other):
        return isinstance(other, Negative) and self.expr == other.expr
    
    def __hash__(self):
        return hash(self.expr)

class BinaryExpression(IntExpression):
    def __init__(self, name: str, l: IntExpression, r: IntExpression, f):
        super().__init__()
        self.name = name
        self.l = l
        self.r = r
        self.f = f
        if (not isinstance(self.l, Expression)):
            raise Exception("{} is not an Expression!".format(self.l))
        if (not isinstance(self.r, Expression)):
            raise Exception("{} is not an Expression!".format(self.r))
    
    def interpret(self):
        l_interpreted = self.l.interpret()
        if (type(l_interpreted) == InterpreterError):
            return l_interpreted
        if (type(l_interpreted) != int):
            return InterpreterError("'{}' interprets to '{}', which is not an integer.  Only integers can be combined with '{}'.".format(self.l, l_interpreted, self.name))
        r_interpreted = self.r.interpret()
        if (type(r_interpreted) == InterpreterError):
            return r_interpreted
        if (type(l_interpreted) != int):
            return InterpreterError("'{}' interprets to '{}', which is not an integer.  Only integers can be combined with '{}'".format(self.r, r_interpreted, self.name))
        return self.f(l_interpreted, r_interpreted)

    def rewrite_subexpression(self, subexpression, equivalent):
        if subexpression == self and equivalent.interpret() == self.interpret():
            return equivalent
        return BinaryExpression(self.name, self.l.rewrite_subexpression(subexpression, equivalent), self.r.rewrite_subexpression(subexpression, equivalent), self.f)
    
    def substitute(self, v, expr):
        return BinaryExpression(self.name, self.l.substitute(v, expr), self.r.substitute(v, expr), self.f)
    
    def to_binary_python_string(self, class_name):
        return "{}({}, {})".format(class_name, self.l.to_python_string(), self.r.to_python_string())

    def associate_l_to_r(self):
        # This is redundant and I don't like it but I'm too lazy to actually clean up this code.
        if not isinstance(self.l, BinaryExpression):
            return self
        if self.name == "+" and self.l.name == "+":
            return Plus(self.l.l, Plus(self.l.r, self.r))
        elif self.name == "*" and self.l.name == "*":
            return Times(self.l.l, Times(self.l.r, self.r))
        return self

    def associate_r_to_l(self):
        # This is redundant and I don't like it but I'm too lazy to actually clean up this code.
        if not isinstance(self.r, BinaryExpression):
            return self
        if self.name == "+" and self.r.name == "+":
            return Plus(Plus(self.l, self.r.l), self.r.r)
        elif self.name == "*" and self.r.name == "*":
            return Times(Times(self.l, self.r.l), self.r.r)
        return self
    
    def commute(self):
        if self.name == "+":
            return Plus(self.r, self.l)
        if self.name == "*":
            return Times(self.r, self.l)
        return self
    
    def __repr__(self):
        l_repr = "({})".format(self.l) if isinstance(self.l, BinaryExpression) else self.l
        r_repr = "({})".format(self.r) if isinstance(self.r, BinaryExpression) else self.r
        return "{} {} {}".format(l_repr, self.name, r_repr)
    
    def __eq__(self, other):
        return isinstance(other, BinaryExpression) and self.name == other.name and self.l == other.l and self.r == other.r
    
    def __hash__(self):
        return hash((self.name, self.l, self.r))


class Plus(BinaryExpression):
    def __init__(self, l: IntExpression, r: IntExpression):
        super().__init__("+", l, r, lambda x, y: x + y)
    
    def to_pos_neg(self):
        return Plus(self.l.to_pos_neg(), self.r.to_pos_neg())
    
    def pos_neg_to_minus(self):
        if isinstance(self.r, Negative):
            return Minus(self.l.pos_neg_to_minus(), self.r.expr.pos_neg_to_minus())
        return Plus(self.l.pos_neg_to_minus(), self.r.pos_neg_to_minus())
    
    def to_python_string(self):
        return self.to_binary_python_string("Plus")

    def associate_l_to_r(self):
        if isinstance(self.l, Plus):
            return Plus(self.l.l, Plus(self.l.r, self.r))
        return self

    def associate_r_to_l(self):
        if isinstance(self.r, Plus):
            return Plus(Plus(self.l, self.r.l), self.r.r)
        return self

class Minus(BinaryExpression):
    def __init__(self, l, r):
        super().__init__("-", l, r, lambda x, y: x - y)
    
    def to_pos_neg(self):
        return Plus(self.l.to_pos_neg(), Negative(self.r.to_pos_neg()))
    
    def to_python_string(self):
        return self.to_binary_python_string("Minus")
    
    def pos_neg_to_minus(self):
        return Minus(self.l.pos_neg_to_minus(), self.r.pos_neg_to_minus())

class Times(BinaryExpression):
    def __init__(self, l, r):
        super().__init__("*", l, r, lambda x, y: x * y)
    
    def to_pos_neg(self):
        return Times(self.l.to_pos_neg(), self.r.to_pos_neg())
    
    def pos_neg_to_minus(self):
        return Times(self.l.pos_neg_to_minus(), self.r.pos_neg_to_minus())
    
    def to_python_string(self):
        return self.to_binary_python_string("Times")

    def associate_l_to_r(self):
        if isinstance(self.l, Times):
            return Times(self.l.l, Times(self.l.r, self.r))
        return self

    def associate_r_to_l(self):
        if isinstance(self.r, Times):
            return Times(Times(self.l, self.r.l), self.r.r)
        return self

class BooleanExpression(BinaryExpression):
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
    
    def substitute(self, v, expr):
        return Equals(self.l.substitute(v, expr), self.r.substitute(v, expr))
    
    def to_pos_neg(self):
        return Equals(self.l.to_pos_neg(), self.r.to_pos_neg())
    
    def to_python_string(self):
        return "Equals({}, {})".format(self.l.to_python_string(), self.r.to_python_string())
    
    def pos_neg_to_minus(self):
        return Equals(self.l.pos_neg_to_minus(), self.r.pos_neg_to_minus())
    
    def __repr__(self):
        l_repr = "({})".format(self.l) if type(self.l) == Equals else self.l
        r_repr = "({})".format(self.r) if type(self.r) == Equals else self.r
        return "{} = {}".format(l_repr, r_repr)
    
    def __eq__(self, other):
        return isinstance(other, Equals) and self.l == other.l and self.r == other.r
    
    def __hash__(self):
        return hash(("=", self.l, self.r))

class Var(Expression):
    def __init__(self, id: str):
        super().__init__()
        self.id = id
    
    def interpret(self):
        return InterpreterError("{} cannot be interpreted".format(self))
    
    def substitute(self, v, expr):
        return expr if self == v else self
    
    def to_pos_neg(self):
        return self
    
    def to_python_string(self):
        return "Var(\"{}\")".format(self.id)

    def associate_l_to_r(self):
        return self

    def associate_r_to_l(self):
        return self

    def pos_neg_to_minus(self):
        return self

    def __repr__(self):
        return str(self.id)
    
    def __eq__(self, other):
        return isinstance(other, Var) and self.id == other.id
    
    def __hash__(self):
        return hash(("var", self.id))