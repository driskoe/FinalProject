"""A Simple Calculator"""

from expr import Expr, Sum, Negation, Difference, Product, Quotient, Modulus, Constant
import re 


def parse(s: str) -> Expr:
    """Parse a string into an expression."""
    # e.g., "(2 + 3)" becomes ["(", "2", "+", "3", ")"]

    #add whitespace between content and end parenthesis  
    s = re.sub(r'([^)^(])(\))', r'\1 \2', s)
    #split if parenthesis or if it ends in a whitespace
    words = re.findall(r'[()]|\S+', s)

    answer = parse_list(words)
    if len(words) > 0:
        raise ValueError(f"Extra junk at end of input: {words!r}")
    return answer

def parse_list(words: list[str]) -> Expr:
    """
    REWRITE THIS

    Parse & remove a *prefix* of the list as an expression.

    Removes the corresponding words from the list,
    but leaves any further words in the list. E.g., after

    L = ["(", "2", "+", "3", ")", "*", "7", ")"]
    E = parse(["(", "2", "+", "3", ")", ])

    Then
        E is now Sum(Constant(2), Constant(3))
              (corresponding to the first five strings)
        L is now ["*", "7", ")"]
              (the leftover strings after getting E)
    """
    if len(words) == 0:
        raise ValueError("Missing expression")

    next = words.pop(0)  # get the first word from the list

    if next == "(":
        # It's a parenthesized expression!

        #prefix notation (only for 2) *need to expand
        op = words.pop(0)  
        e1 = parse_list(words)  
        e2 = parse_list(words)  

        after = words.pop(0)  # there should be a ) after the e2
        if after != ")":
            raise ValueError(f"Expected ), but found {after!r}")

        if op == "+":
            result = Sum(e1, e2)
            result.eval()
            return result
        if op == "-":
            result = Difference(e1, e2)
            result.eval()
            return result
        elif op == "*":
            result = Product(e1, e2)
            result.eval()
            return result
        elif op == "quotient":
            result = Quotient(e1, e2)
            result.eval()
            return result
        elif op == "mod":
            result =  Modulus(e1, e2)
            result.eval()
            return result

        else:
            raise ValueError(f"Unrecognized binary operator {op!r}")

    elif next == "-": #unary negation
        e1 = parse_list(words) #there should be one expression
        return Negation(e1) #interprets as difference between 0 and the singular epression
    
    else:
        # if we expect an expression, and it doesn't start with a left paren,
        # it must be a number
        result =  Constant(int(next))
        result.eval()
        return result


def main():
    """The main calculator loop."""

    # Start with a demo
    s1 = "4"
    e1 = parse(s1)

    print(s1)
    print(repr(e1))
    # print(str(e1))
    print(e1.eval())

    # Print a prompt
    print()
    print("...and now it's your turn!\n")

    print("Enter an expression.")
    print("   Whitespace between words is required.")
    print("   Parentheses around binary operations are required.")
    print("   Supported binary operations are + and *.")
    print("   Just press Enter to quit.")
    print()

    # Calculator loop
    while True:
        global lineNum
        lineNum = 0
        s = input("> ").strip()
        if s == "":
            break
        try:
            e = parse(s)
            print(repr(e))
            print(e.eval())
            print()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # What to do if someone runs "python calc.py"
    main()
