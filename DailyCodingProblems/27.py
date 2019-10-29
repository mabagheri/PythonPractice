"""
Problem 27
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def is_balanced(s):
    brace_map = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    stack = list()
    for char in s:
        if stack and char in brace_map and stack[-1] == brace_map[char]:
            stack.pop()
        else:
            stack.append(char)
    return not stack

assert is_balanced("")
assert is_balanced("{}")
assert is_balanced("([])")
assert is_balanced("([])[]({})")
assert not is_balanced("(")
assert not is_balanced("]")
assert not is_balanced("((()")
assert not is_balanced("([)]")
