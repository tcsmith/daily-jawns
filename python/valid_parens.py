"""
20. Valid Parentheses

Given a string s containing only the characters:

()[]{}

Determine if the input string is valid.

Rules:
1. Open brackets must be closed by the same type.
2. Open brackets must be closed in correct order.
3. Every closing bracket must have a matching opening bracket.

Return:
True  -> valid
False -> invalid


Examples
========

Input:
s = "()"

Output:
True

Explanation:
Opening parenthesis is closed correctly.


-------------------------

Input:
s = "()[]{}"

Output:
True

Explanation:
Multiple independent bracket pairs.
All closed correctly.


-------------------------

Input:
s = "(]"

Output:
False

Explanation:
Bracket types do not match.
Opened with "("
Closed with "]"


-------------------------

Input:
s = "([)]"

Output:
False

Explanation:
Order is invalid.

Expected:
(
[
]
)

Actual:
(
[
)
]


-------------------------

Input:
s = "{[]}"

Output:
True

Explanation:
Nested brackets closed correctly.


Constraints
===========

1 <= len(s) <= 10_000

Only characters:
()[]{}


Interview checklist
===================

Clarify:
- Empty string possible?
- Only these chars?
- Return bool?

Think:
- Brute force?
- Better data structure?

State:
- Target complexity

Code:
- Simple first

Test:
- Normal
- Nested
- Invalid
- Empty
"""


def valid_parens_1(text: str) -> bool:
    assert len(text) >= 1 and len(text) <= 10_000

    # ()
    parens_stack = []

    opens = "({["
    closed = ")}]"
    for c in text:
        # print(c)
        if c in opens:
            parens_stack.append(c)
        elif c in closed:
            # we have a closed, now we need to have an open, and its matching
            if len(parens_stack) == 0:
                return False
            paren = parens_stack.pop()
            if paren in opens:
                if (paren == "(" and c == ")") or (paren == "{" and c == "}") or (paren == "[" and c == "]"):
                    return True
                else:
                    return False
            else:
                return False
        else:
            raise ValueError(f"Text contains invalid character '{c}'")

    return True


def valid_parens_2(text: str) -> bool:
    parens_stack = []
    parens_map = {
        ")":"(",
        "}":"{",
        "]":"[",
    }

    opens = "({["
    for c in text:
        if c in opens:
            parens_stack.append(c)
        elif len(parens_stack) > 0:
            opener = parens_stack.pop()
            if parens_map.get(c) != opener:
                return False
    if len(parens_stack) > 0:
        return False
    else:
        return True



def valid_parens(text: str) -> bool:
    return valid_parens_2(text=text)

def main() -> None:
    s = "()"
    assert valid_parens(s) == True
    s = ")("
    assert valid_parens(s) == False
    s = "()[]{}"
    assert valid_parens(s) == True
    s = "(]"
    assert valid_parens(s) == False
    s = "([)]"
    assert valid_parens(s) == False
    s = "{[]}"
    assert valid_parens(s) == True



if __name__ == "__main__":
    main()