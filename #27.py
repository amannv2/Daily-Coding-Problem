# Given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.


class Stack:

    def __init__(self):
        self.stack = ['$']

    def peek(self):
        return self.stack[-1]

    def push(self, data):
        self.stack.append(data)
        return True

    def pop(self):
        if len(self.stack) == 1:
            print('Stack Empty')
        else:
            self.stack.pop()

    def display(self):
        print(self.stack)


def test(b_list):
    import re

    if not bool(re.match('^[({\[\]})]+$', b_list)):
        print('Invalid input')
        return False

    stack = Stack()

    for char in b_list:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)

        else:
            if (char == ')' and stack.peek() != '(') or \
                    (char == '}' and stack.peek() != '{') or \
                    (char == ']' and stack.peek() != '['):
                return False

            else:
                stack.pop()

    if stack.peek() != '$':
        return False
    else:
        return True


bracket_list = input('Enter the string of brackets: ')
print(test(bracket_list))

