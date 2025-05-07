from Pet import Pet
from bird import Bird
from Omnivore import Omnivore

class Parrot(Bird, Omnivore, Pet):
    def __init__(self, wings=2, legs=2, colour = 'yellow'):
        super().__init__(wings, legs)
        self.colour = colour
    def sleep(self)->None:
        print('Parrots sleep around 10 to 12 hours each night, often tucked under their wings. They may also take naps during the day.')
    
    def move(self)->None:
        print('I can move in various ways. I can fly, walk, climb and even use a unique method called "beakiation" to traverse narrow branches')
    
    def reproduce(self)->str:
        return super().reproduce() + '\nParrots often take a few days to lay a full clutch of eggs. This can be as many as three to four eggs.'
    
    def eat(self) -> None:
        Omnivore.eat(self)
        print('I eat both plant and animal matter. My natural diet includes a variety of foods like seeds, nuts, fruits, vegetables, flowers, buds, and insects.')
    
    def pet(self)->str:
        return super().pet()
    
    def __repr__(self) -> str:
        return Bird.__repr__(self) + '\nSpecies: Parrot' + '\n'+Pet.__repr__(self)+ '\n'+Omnivore.__repr__(self)
    
if __name__ == '__main__':
    p1 = Parrot()
    print(p1)
    p1.eat()