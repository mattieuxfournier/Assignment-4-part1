from Animal import Animal

class Fish(Animal):
    def __init__(self, fins=0, tail=True):
        super().__init__(fins, tail)
    def reproduce(self) -> str:
        return super().reproduce() + '\nFish reproduction varies largely, some give birth to live young while others lay eggs.'
    def __repr__(self) -> str:
        return super().__repr__() + '\nClass: Fish'