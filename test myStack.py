__author__ = '31351'

import SandQ
#s=myStack.Stack()
import DandC
dac = DandC.DogCatQueue()
cat = DandC.Cat()
dog = DandC.Dog()
dac.add(cat)
dac.add(cat)
dac.add(dog)
dac.add(dog)
dac.add(cat)
dac.add(dog)
dac.add(cat)

dac.pollCat()
print dac.isEmpty()
print dac.isCatQueueEmpty()
print dac.isDogQueueEmpty()