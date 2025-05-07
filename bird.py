from Animal import Animal

class Bird(Animal):
    def __init__(self, wings=2, legs = 2):
        super().__init__(wings, legs)
    def reproduce(self) -> str:
       return super().reproduce() + '\nBirds typically reproduce by hatching and incubating their eggs.'
    def __repr__(self)->str:
        return super().__repr__() + '\nClass: Bird'