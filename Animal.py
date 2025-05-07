from abc import ABCMeta, abstractmethod

class Animal(object, metaclass = ABCMeta):
    def __init__(self, legs = 0, fins = 0, wings = 0, tail=False):
        self.legs = legs
        self.fins = fins
        self.wings = wings
        self.tail = tail
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def reproduce(self) -> str:
        return 'Members of this kingdom reproduce by finding mates of the same species '
    
    def __repr__(self) -> str:
        return 'Kingdom: Animalia'
