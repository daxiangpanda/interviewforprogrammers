__author__ = '31351'

import SandQ
#s=myStack.Stack()
import stacksort
stack = SandQ.Stack()
for i in [1,4,2,8,5,7]:
    stack.push(i)
stack.printStack()

stacksort.sortstackbystack(stack)
stack.printStack()
