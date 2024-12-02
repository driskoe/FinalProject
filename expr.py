# Remember, turn off any write-code-for-you editor extensions like Copilot!
import abc
import heapq


#global variables
#all free registers from r1 to r13
freeRegisters = [f"r{i}" for i in range(1,14)]
heapq.heapify(freeRegisters)
#current line num
lineNum = 0


def allocateReg():
    """removes the first register in the priority queue and returns it"""
    if not freeRegisters:
        raise RuntimeError("No free registers available")
    return heapq.heappop(freeRegisters)

def freeReg(reg):
    """after done with the register, adds it back into the priority queue of free registers"""
    heapq.heappush(freeRegisters, reg)

def incrementLine(value):
    """both increments the overall line number and returns the useable string for the current line number"""
    global lineNum
    lineNum+=1
    return lineNumString(value)

def lineNumString(lineNum):
    """Converts a numerical line number into a 2+ digit string to be used in HMMM code"""
    lineString = str(lineNum)
    if(len(lineString)==1):
        return "0" + lineString
    return lineString

def incrementRegister(originalReg):
    global minOpenReg
    minOpenReg+=1
    return str(originalReg)

# An abstract class that serves as an interface. 
class Expr(abc.ABC):
    """Represents an arithmetic expression."""

    @abc.abstractmethod
    def eval(self) -> str:
        """Evaluate this expression to a HMMM equivalent."""
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
        self.register = -1

    def eval(self) -> str:
        self.register = allocateReg()
        value =  f"{incrementLine(lineNum)} setn {self.register} {str(self.value)}"
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
        self.register = -1

    def eval(self) -> str:
        self.register = allocateReg()
        value = f"{incrementLine(lineNum)} add {self.register} {self.left.register} {self.right.register}"
        print(value)
        freeReg(self.right.register)
        freeReg(self.left.register)
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
        self.register = -1

    def eval(self) -> str:
        self.register = allocateReg()
        value =  f"{incrementLine(lineNum)} mul {self.register} {self.left.register} {self.right.register}"
        print(value)
        freeReg(self.right.register)
        freeReg(self.left.register)
        return value

    def __str__(self) -> str:
        return f"({self.left} * {self.right})"

    def __repr__(self) -> str:
        return f"Product({self.left}, {self.right})"

class Quotient(Expr):
    """Represent the quotient of two subexpressions."""

    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right
        self.register = -1

    def eval(self) -> str:
        self.register = allocateReg()
        value = f"{incrementLine(lineNum)} div {self.register} {self.left.register} {self.right.register}"
        print(value)
        freeReg(self.right.register)
        freeReg(self.left.register)
        return value 
    
    def __str__(self) -> str:
        return f"({self.left} / {self.right})"

    def __repr__(self) -> str:
        return f"Quotient({self.left}, {self.right})"

class Difference(Expr):
    """Represent the difference of two subexpressions."""

    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right
        self.register = -1

    def eval(self) -> str:
        self.register = allocateReg()
        value = f"{incrementLine(lineNum)} sub {self.register} {self.left.register} {self.right.register}"
        print(value)
        freeReg(self.right.register)
        freeReg(self.left.register)
        return value 
    
    def __str__(self) -> str:
        return f"({self.left} - {self.right})"

    def __repr__(self) -> str:
        return f"Difference({self.left}, {self.right})"

class Modulus(Expr):
    """Represent the remainder when dividing two subexpressions."""

    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right
        self.register = -1

    def eval(self) -> str:
        self.register = allocateReg()
        value = f"{incrementLine(lineNum)} mod {self.register} {self.left.register} {self.right.register}"
        print(value)
        freeReg(self.right.register)
        freeReg(self.left.register)
        return value

    def __str__(self) -> str:
        return f"({self.left} % {self.right})"

    def __repr__(self) -> str:
        return f"Modulus({self.left}, {self.right})"

class Negation(Expr):
    """Represent the additive inverse of an expression."""

    def __init__(self, value: Expr):
        self.value = value
        self.register = -1

    def eval(self) -> str:
        self.register = allocateReg()
        value = f"{incrementLine(lineNum)} neg {self.register} {self.value.register}"
        print(value)
        freeReg(self.value.register)
        return value

    def __str__(self) -> str:
        return f"(-{self.value})"

    def __repr__(self) -> str:
        return f"Negation({self.left}, {self.right})"
