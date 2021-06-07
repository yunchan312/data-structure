class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def push(self, e):
        self.items.append(e)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.items.pop()
    '''
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
    '''
    '''
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.items[-1]
    '''

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")