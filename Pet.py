from abc import ABCMeta, abstractmethod
class Pet(object, metaclass = ABCMeta):
    def __init__(self, legs = 0, wings=0, fins=0, tail = False):
        super().__init__(legs,wings,fins,tail)
        
    def pet(self) -> str:
        return 'You can pet this animal'
    
    def __repr__(self) -> str:
        return 'This animal is a pet'