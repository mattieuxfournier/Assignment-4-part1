from Animal import Animal

class Amphibian(Animal):
    def __init__(self, legs=0, tail=False):
        super().__init__(legs, tail)
        
    def reproduce(self)->str:
        return super().reproduce() + '\nAmphibians reproduce by laying soft eggs in the water.'
    
    def __repr__(self)->str:
        return super().__repr__() + '\nClass: Amphibian'