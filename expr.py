# Remember, turn off any write-code-for-you editor extensions like Copilot!
import abc


minOpenReg = 1
lineNum = 0

def incrementLine(originalLine):
    global lineNum
    lineNum = originalLine+1
    originalLine = str(originalLine)
    if(len(originalLine) == 1):
        originalLine = "0" + originalLine
    return originalLine

def incrementRegister(originalReg):
    global minOpenReg
    minOpenReg+=1
    return str(originalReg)

# An abstract class that serves as an interface.
class Expr(abc.ABC):
    """Represents an arithmetic expression."""

    @abc.abstractmethod
    def eval(self) -> str:
        """Evaluate this expression to a numeric answer."""
        ...

    @abc.abstractmethod
    def __str__(self) -> str:
        ...

    @abc.abstractmethod
    def __repr__(self) -> str:
        ...


class Constant(Expr):
    """Represent a numeric constant."""

    def __init__(self, value: float):
        self.value = value

    def eval(self) -> str:
        value =  incrementLine(lineNum) + " setn r" + incrementRegister(minOpenReg) + " " + str(self.value)
        print(value)
        return value

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return f"Constant({self.value})"


class Sum(Expr):
    """Represent the sum of two subexpressions."""

    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def eval(self) -> str:
        value =  incrementLine(lineNum) + " add " + "idealRegister" + " " + "left'sRegister " + "right'sRegister"
        print(value)
        return value

    def __str__(self) -> str:
        return f"({self.left} + {self.right})"

    def __repr__(self) -> str:
        return f"Sum({self.left}, {self.right})"


class Product(Expr):
    """Represent the product of two subexpressions."""

    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def eval(self) -> str:
        value =  incrementLine(lineNum) + " mul " + "idealRegister" + " " + "left'sRegister " + "right'sRegister"
        print(value)
        return value

    def __str__(self) -> str:
        return f"({self.left} * {self.right})"

    def __repr__(self) -> str:
        return f"Product({self.left}, {self.right})"

class Quotient(Expr):
    """Represent the remainder when dividing two subexpressions."""

    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def eval(self) -> str:
        value =  incrementLine(lineNum) + " div " + "idealRegister" + " " + "left'sRegister " + "right'sRegister"
        print(value)
        return value

    def __str__(self) -> str:
        return f"({self.left} / {self.right})"

    def __repr__(self) -> str:
        return f"Quotient({self.left}, {self.right})"

class Modulus(Expr):
    """Represent the remainder when dividing two subexpressions."""

    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def eval(self) -> str:
        value =  incrementLine(lineNum) + " mod " + "idealRegister" + " " + "left'sRegister " + "right'sRegister"
        print(value)
        return value

    def __str__(self) -> str:
        return f"({self.left} % {self.right})"

    def __repr__(self) -> str:
        return f"Modulus({self.left}, {self.right})"
