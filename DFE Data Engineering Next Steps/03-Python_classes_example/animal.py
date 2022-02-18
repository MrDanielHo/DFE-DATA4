from re import A

from matplotlib import animation


class Animal():
    count = 0

    def __init__(self, species, name, sound):
        self._species = species
        self._name = name
        self._sound = sound
        Animal.count += 1
    @property
    def species(self):
        return self._species

    @classmethod
    def kill(cls):
        cls.count -=1
        
    @property
    def name(self):
        return self._name
    
    def make_sound(self):
        print(self._sound)
    
    @classmethod
    def remove(cls):
        cls.count -= 1
    
    @classmethod
    def zoo_size(cls):
        return cls.count

if __name__ == "__main__":
    leo = Animal("African lion", "Leo", "Big roar")
    garfield = Animal("cat", "Garfield", "Small meow")
    felix = Animal("cat", "Felix", "Small meow")

    print(f'{leo.name} is a {leo.species} --', end=' ')
    leo.make_sound()

    print(f'{garfield.name} is a {garfield.species} --', end=' ')
    garfield.make_sound()

    print(f'{felix.name} is a {felix.species} --', end=' ')
    felix.make_sound()

    print(Animal.zoo_size())