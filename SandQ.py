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

    def printStack(self):
        for i in self.items:
            print i

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


class myQueue:
    def __init__(self):
        self.stackPush = Stack()
        self.stackPop = Stack()

    def add(self,pushInt):
        self.stackPush.push(pushInt)

    def poll(self):#out the queue
        if self.stackPush.isEmpty() and self.stackPop.isEmpty():
            raise TypeError("Queue empty")
        elif self.stackPop.isEmpty():
            while not self.stackPush.isEmpty():
                self.stackPop.push(self.stackPush.pop())
        return self.stackPop.pop()

    def peek(self):#the 1st of the queue
        if self.stackPop.isEmpty() and self.stackPush.isEmpty():
            raise TypeError("Queue empty")
        elif self.stackPop.isEmpty():
            while not self.stackPush.isEmpty():
                self.stackPop.push(self.stackPush.pop())
        return self.stackPop.peek()

    def printQueue(self):
        self.stackPop.printStack()


def getAndRemoveLast(s):
    result = s.pop()
    if s.isEmpty():
        return result
    else:
        last = getAndRemoveLast(s)
        s.push(result)
        return last


def reverse(s):
    if s.isEmpty():
        return
    i = getAndRemoveLast(s)
    reverse(s)
    s.push(i)