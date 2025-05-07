from Animal import Animal

class Mammal(Animal):
    def __init__(self, legs=0, fins=0, wings=0):
        super().__init__(legs, fins, wings)
        
    def reproduce(self) -> str:
        result = ' Mammals give birth to live young, and raise them until they become independant'
        return super().reproduce() + result
    
    def __repr__(self) -> str:
        return super().__repr__() + '\nClass: Mammal'