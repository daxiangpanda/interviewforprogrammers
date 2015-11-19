#!/usr/bin/env python
# encoding: utf-8

def hanoi1(num,left,mid,right):
    RESULT = 0
    if num<1:
        return 0
    return process(num,left,mid,right,left,right)
RESULT = 0
def process(num,left,mid,right,fr,to):
    global RESULT
    if num == 1:
        if fr == mid or to == mid:
            RESULT+=1
            #print str(RESULT)+" Move 1 from "+ fr + " to "+to
            return 1
        else:
            RESULT+=1
            #print str(RESULT)+" Move 1 from "+ fr + " to "+mid
            RESULT+=1
            #print str(RESULT)+" Move 1 from "+ mid + " to "+to
            return 2
    if fr == mid or to == mid:
        another = (fr == left or to == left) and right or left
        part1 = process(num-1,left,mid,right,fr,another)
        part2 = 1
        RESULT+=1
        #print str(RESULT)+" Move "+ str(num) + " from " + fr + " to "+to
        part3 = process(num-1,left,mid,right,another,to)
        return part1+part2+part3
    else:
        part1 = process(num-1,left,mid,right,fr,to)
        part2 = 1
        RESULT+=1
        #print str(RESULT)+" Move "+ str(num) + " from " + fr + " to "+mid
        part3 = process(num-1,left,mid,right,to,fr)
        part4 = 1
        RESULT+=1
        #print str(RESULT)+" Move "+ str(num) + " from " + mid + " to "+to
        part5 = process(num-1,left,mid,right,fr,to)
        return part1+part2+part3+part4+part5

hanoi1(100,"left","mid","right")
print RESULT