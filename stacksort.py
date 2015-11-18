__author__ = '31351'
import SandQ
def sortstackbystack(stack):
    help = SandQ.Stack()
    while not stack.isEmpty():
        cur = stack.pop()
        while not help.isEmpty() and help.peek() > cur:
            stack.push(help.pop())
        help.push(cur)
    while not help.isEmpty():
        stack.push(help.pop())
