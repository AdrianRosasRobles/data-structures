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
def evaluate_postfix(expression):
    stack = ArrayStack()
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
    return stack.pop()
print(evaluate_postfix("3 5 + 2 *"))