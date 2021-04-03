class Expression:
    def __init__(self):
        pass

    def interpret(self):
        raise Exception("interpret unimplemented")
    
    def substitute(self, v, expr):
        raise Exception("substitute unimplemented")

    def rewrite_subexpression(self, subexpression, equivalent):
        raise Exception("evalute_subexpression unimplemented")
    
    def rw_se(self, subexpression, equivalent):
        return self.rewrite_subexpression(subexpression, equivalent)
    
    def dumb_rw_se(self, sube, equiv):
        raise Exception("dumb_rw_se unimplemented")
    
    def combine_like_terms(self, likeness):
        raise Exception("combine_like_terms unimplemented")
    
    def is_like_terms_with(self, other, likeness):
        raise Exception("is_like_terms_with unimplemented")

    def pos_neg_to_minus(self):
        raise Exception("pos_neg_to_minus unimplemented")

    def pnm(self):
        return self.pos_neg_to_minus()
    
    def comm(self):
        return self.commute()
    
    def commute(self):
        raise Exception("commute unimplemented")

    def to_pos_neg(self):
        raise Exception("to_pos_neg unimplemented")
    
    def pn(self):
        return self.to_pos_neg()

    def associate_l_to_r(self):
        raise Exception("associate_l_to_r unimplemented")
    
    def remove_add_zeroes(self):
        raise Exception("remove_add_zeroes unimplemented")
    
    def alr(self):
        return self.associate_l_to_r()

    def arl(self):
        return self.associate_r_to_l()
    
    def sub_alr(self, sub):
        return self.rewrite_subexpression(sub, sub.associate_l_to_r())
    
    def sub_arl(self, sub):
        return self.rewrite_subexpression(sub, sub.associate_r_to_l())
    
    def sub_comm(self, sub):
        return self.rewrite_subexpression(sub, sub.commute())

    def associate_r_to_l(self):
        raise Exception("associate_r_to_l unimplemented")
    
    def minus_to_zero(self):
        raise Exception("minus_to_zero unimplemented")
    
    def mz(self):
        return self.minus_to_zero()
    
    def sub_mz(self, sub):
        return self.rewrite_subexpression(sub, sub.mz())

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
    
    def minus_to_zero(self):
        return self
    
    def remove_add_zeroes(self):
        return self

class Int(IntExpression):
    def __init__(self, value: int):
        super().__init__()
        if value < 0:
            raise Exception("Int value must be greater than or equal to 0")
        self.value = value
    
    def combine_like_terms(self, likeness):
        return self
    
    def interpret(self):
        return self.value
    
    def substitute(self, v, expr):
        return self

    def rewrite_subexpression(self, subexpression, equivalent):
        if subexpression == self and equivalent.interpret() == self.interpret():
            return equivalent
        return self
    
    def dumb_rw_se(self, sube, equiv):
        if (sube == self):
            return equiv
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
    
    def combine_like_terms(self, likeness):
        return self.expr.combine_like_terms(likeness)
    
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
    
    def dumb_rw_se(self, sube, equiv):
        if sube == self:
            return equiv
        return Negative(self.expr.dumb_rw_se(sube, equiv))
    
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

    # CURRENTLY BROKEN
    def pos_neg_to_minus(self):
        if (self.name != "+"):
            return self
        if isinstance(self.r, Negative):
            return Minus(self.l.pos_neg_to_minus(), self.r.expr.pos_neg_to_minus())
        return Plus(self.l.pos_neg_to_minus(), self.r.pos_neg_to_minus())
    
    def remove_add_zeroes(self):
        if self.name == "+" and self.l == Int(0):
            return self.r.remove_add_zeroes()
        if self.name == "+" and self.r == Int(0):
            return self.l.remove_add_zeroes()
        return BinaryExpression(self.name, self.l.remove_add_zeroes(), self.r.remove_add_zeroes(), self.f)

    def rewrite_subexpression(self, subexpression, equivalent):
        if subexpression == self and equivalent.interpret() == self.interpret():
            return equivalent
        return BinaryExpression(self.name, self.l.rewrite_subexpression(subexpression, equivalent), self.r.rewrite_subexpression(subexpression, equivalent), self.f)
    
    def dumb_rw_se(self, sube, equiv):
        if (sube == self):
            return equiv
        return BinaryExpression(self.name, self.l.dumb_rw_se(sube, equiv), self.r.dumb_rw_se(sube, equiv), self.f)
    
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
    
    def minus_to_zero(self):
        if self.name == "-" and self.l == self.r:
            return Int(0)
        return self
    
    def to_pos_neg(self):
        if self.name == "-":
            return Plus(self.l.to_pos_neg(), Negative(self.r.to_pos_neg()))
        return BinaryExpression(self.name, self.l.to_pos_neg(), self.r.to_pos_neg(), self.f)
    
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
    
    def combine_like_terms(self, likeness):
        l = self.l.combine_like_terms(likeness)
        r = self.r.combine_like_terms(likeness)
        if l == likeness and r == likeness:
            return Times(Int(2), likeness)
        if l == likeness and isinstance(r, Times) and isinstance(r.l, Int) and r.r == likeness:
            return Times(Int(r.l.value + 1), likeness)
        if r == likeness and isinstance(l, Times) and isinstance(l.l, Int) and l.r == likeness:
            return Times(Int(l.l.value + 1), likeness),
        if isinstance(l, Times) and isinstance(r, Times) and isinstance(l.l, Int) and isinstance(r.l, Int) and l.r == likeness and r.r == likeness:
            return Times(Int(l.l.value + r.l.value), likeness)
        return Plus(l, r)
    
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
    
    def to_python_string(self):
        return self.to_binary_python_string("Minus")
    
    def pos_neg_to_minus(self):
        return Minus(self.l.pos_neg_to_minus(), self.r.pos_neg_to_minus())
    
    def combine_like_terms(self, likeness):
        return Minus(self.l.combine_like_terms(likeness), self.r.combine_like_terms(likeness))

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
    
    def combine_like_terms(self, likeness):
        return Times(self.l.combine_like_terms(likeness), self.r.combine_like_terms(likeness))

class BooleanExpression(BinaryExpression):
    def __init__(self):
        self.type = "boolean"

class Equals(BooleanExpression):
    def __init__(self, l: Expression, r: Expression):
        super().__init__()
        self.l = l
        self.r = r
    
    def combine_like_terms(self, likeness):
        return Equals(self.l.combine_like_terms(likeness), self.r.combine_like_terms(likeness))
    
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
    
    def dumb_rw_se(self, sube, equiv):
        return Equals(self.l.dumb_rw_se(sube, equiv), self.r.dumb_rw_se(sube, equiv))
    
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

    def combine_like_terms(self, likeness):
        return self
    
    def interpret(self):
        return InterpreterError("{} cannot be interpreted".format(self))
    
    def dumb_rw_se(self, sube, equiv):
        if self == sube:
            return equiv
        return self
    
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