class StackOverflowException(Exception)
    pass
class StackUnderflowException(Exception)
    pass
class StackOutOfBoundsException(Exception)
    pass

class Stack:
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        if self.data:
            return self.data[-1]
        else:
            raise StackOutOfBoundsException()
