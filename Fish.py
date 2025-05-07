from Animal import Animal

class Fish(Animal):
    def __init__(self, fins=0, tail=False):
        super().__init__(fins, tail)
    def reproduce(self):
        return super().reproduce() + '\nFish reproduction varies largely, some give birth to live young while others lay eggs.'
    def __repr__(self):
        return super().__repr__() + '\nClass: Fish'