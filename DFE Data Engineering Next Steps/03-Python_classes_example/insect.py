from animal import Animal

class Insect(Animal):
    '''
    An animal with 2 sets of wings and 3 pairs of legs
    '''

    def __init__(self, species, name, sound, can_fly=True):
        super().__init__(species, name, sound)
        self._can_fly = can_fly

    @property
    def can_fly(self):
        return self._can_fly
    

if __name__ == '__main__':
    mon = Insect('monarch butterfly', 'Mary', None)
    scar = Insect('scarab beetle', 'Rupert', 'Buzz')

    for insect in mon, scar:
        flying_status = 'can' if insect.can_fly else "can't"
        print(f'Hi! I am a {insect.name} the {insect.species} and I {flying_status} fly!')
        insect.make_sound()
        print()

print(Animal.zoo_size())