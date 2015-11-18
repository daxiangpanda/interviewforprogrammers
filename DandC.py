__author__ = '31351'
# -*- coding:utf-8 -*-
import SandQ
class Pet:
    def __init__(self,type):
        self.type = type

    def getPetType(self):
        return self.type


class Dog(Pet):
    def __init__(self):
        self.type = "Dog"
        Pet.__init__(self,self.type)


class Cat(Pet):
    def __init__(self):
        self.type = "Cat"
        Pet.__init__(self,self.type)


class PetEnterQueue(Pet):
    def __init__(self,pet,count):
        self.pet = Pet(self)
        self.count = count

    def getPet(self):
        return self.pet

    def getCount(self):
        return self.count

    def getEnterType(self):
        return self.pet.getPetType()

class DogCatQueue:
    def __init__(self):
        self.dogQ = SandQ.myQueue()
        self.catQ = SandQ.myQueue()
        self.count = 0

    def add(self,pet):
        if pet.getPetType() == "Dog":
            self.dogQ.add(PetEnterQueue(pet,self.count))
            self.count+=1
        elif pet.getPetType() == "Cat":
            self.catQ.add(PetEnterQueue(pet,self.count))
            self.count+=1
        else:
            raise TypeError("not cat or dog")

    def pollAll(self):
        if not self.dogQ.isEmpty() and not self.dogQ.isEmpty():
            if self.dogQ.peek().getCount() < self.dogQ.peek().getCount():
                return self.dogQ.poll().getPet()
            else:
                return self.catQ.poll().getPet()
        elif not self.dogQ.isEmpty():
            return self.dogQ.poll().getPet()
        elif not self.catQ.isEmpty():
            return self.catQ.poll().getPet()
        else:
            raise TypeError("err,queue is empty")

    def pollDog(self):
        if not self.dogQ.isEmpty():
            return self.dogQ.poll().getPet()
        else:
            raise TypeError("err,dog queue is empty")

    def pollCat(self):
        if not self.catQ.isEmpty():
            return self.catQ.poll().getPet()
        else:
            raise TypeError("err,cat queue is empty")

    def isEmpty(self):
        return self.dogQ.isEmpty() and self.catQ.isEmpty()

    def isDogQueueEmpty(self):
        return self.dogQ.isEmpty()

    def isCatQueueEmpty(self):
        return self.catQ.isEmpty()

