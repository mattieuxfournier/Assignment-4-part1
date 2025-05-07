from Animal import Animal

class Reptile(Animal):
    def __init__(self, legs=0, tail=False):
        super().__init__(legs, tail)
    def reproduce(self):
        return super().reproduce() + '\nReptiles reproduce by laying eggs typically on land rather than water.'
    
    def __repr__(self):
        return super().__repr__() + '\nClass: Reptile'