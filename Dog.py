from Pet import Pet
from Mammal import Mammal
from Omnivore import Omnivore

class Dog(Pet, Omnivore, Mammal):
    def __init__(self, legs=4, ears=2, tail=True):
        super().__init__(legs, tail)
        self.ears = ears
        
    def reproduce(self) -> str:
        return super().reproduce() + '\nI can typically reproduce twice a year, my litter typically ranges from 1-12, I birth my young after 57-65 days'
    def sleep(self) -> None:
        print('I am diurnal, and typically sleep 12-14 hours every 24 hours')
    def move(self) -> None:
        print('I walk on my four legs to move around')
    def eat(self) -> None:
        Omnivore.eat(self)
        
    def __repr__(self) -> str:
        return Mammal.__repr__(self) + '\nSpecies: Dog' + '\n'+Pet.__repr__(self)+ '\n'+Omnivore.__repr__(self)
if __name__ == '__main__':
    d1 = Dog()
    d1.eat()