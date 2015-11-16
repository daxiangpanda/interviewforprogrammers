__author__ = '31351'


class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class MyStack:
    def __init__(self):
        self.stackData = Stack()
        self.stackMin = Stack()

    def isEmpty(self):
        return len(self.stackData) == 0

    def push(self,item):
        if self.stackMin.isEmpty():
            self.stackMin.push(item)
        elif item <= self.getMin():
            self.stackMin.push(item)
        self.stackData.push(item)

    def pop(self):
        if self.stackData.isEmpty():
            raise TypeError("stack empty")
        value = self.stackData.pop()
        if value == self.getMin():
            self.stackMin.pop()
        return value

    def getMin(self):
        if self.stackMin.isEmpty():
            raise TypeError("stack empty")
        return self.stackMin.peek()

