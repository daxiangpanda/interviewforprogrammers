#!/usr/bin/env python
# encoding: utf-8
import SandQ
import sys
class Action:
    No = 0
    LToM = 1
    MToL = 2
    MToR = 3
    RToM = 4

def hanoi2(num,left,mid,right):
    lS = SandQ.Stack()
    mS = SandQ.Stack()
    rS = SandQ.Stack()
    lS.push(sys.maxint)
    mS.push(sys.maxint)
    rS.push(sys.maxint)
    for i in range(num,0,-1):
        lS.push(i)
    record = Action()
    step = 0
    while(rS.size() != num+1):
        step+=fStackToStack(record,Action.MToL,Action.LToM,lS,mS,left,mid)
        step+=fStackToStack(record,Action.LToM,Action.MToL,mS,lS,mid,left)
        step+=fStackToStack(record,Action.RToM,Action.MToR,mS,rS,mid,right)
        step+=fStackToStack(record,Action.MToR,Action.RToM,rS,mS,right,mid)\
    return step
def fStackToStack(record,preNoAct,nowAct,fStack,tStack,from,to):
