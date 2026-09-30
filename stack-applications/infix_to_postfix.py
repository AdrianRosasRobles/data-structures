class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data.pop()
    
stack = ArrayStack()

def infix_to_postfix(expression):
    stack = ArrayStack()
    output = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            output.append(token)

        elif token in precedence:
            while (not stack.is_empty() and
                   stack.top() in precedence and
                   precedence[stack.top()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)

        elif token == '(':
            stack.push(token)

        elif token == ')':
            while stack.top() != '(':
                output.append(stack.pop())
            stack.pop()

    while not stack.is_empty():
            output.append(stack.pop())

    return " ".join(output)
print(infix_to_postfix("3 + 5 * 2"))
