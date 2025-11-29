class Stack:
    def __init__(self):   # fixed constructor
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def __str__(self):    # display contents nicely
        return str(self.data)


stack = Stack()
stack.push(4)
stack.push(5)
stack.push(6)
print(stack)   # Output: [4, 5, 6]
