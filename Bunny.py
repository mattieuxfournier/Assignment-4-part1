from Pet import Pet
from Mammal import Mammal
from Herbivore import Herbivore

class Bunny(Mammal, Herbivore, Pet):
    def __init__(self, legs = 4, ears = 2, tail=True):
        super().__init__(legs, tail)
        self.ears = ears
    
    def __repr__(self) -> str:
        result = '\nSpecies: Bunny'
        result = Mammal.__repr__(self)+ result
        result += '\n' +Pet.__repr__(self)
        return result + '\n' + Herbivore.__repr__(self)
    
    def reproduce(self) -> str:
        result = 'Bunnies can produce multiple litters per year, potentially having 3-8 kids per litter'
        print(super().reproduce() +'\n'+ result)

    def move(self) -> None:
        print('I move by hopping and I can see behind me')

    def sleep(self) -> None:
        print('Bunnies are nocturnal animals, typically around 12-14 hours a day in short, intermittent periods.')

    def eat(self) -> None:
        Herbivore.eat(self)
        print('I mostly eat fresh hay and grass, as well as leafy greens and pellets. I should only be given fruits and root vegetables, like carrots, as an occasional treat')

if __name__ == '__main__':
    b1 = Bunny()
    print(b1)
    print()
    b1.reproduce()
    print()
    b1.sleep()
    print()
    b1.move()
    print()
    b1.eat()
