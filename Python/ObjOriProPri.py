'''
Object Oriented Programming Principles
'''
from abc import ABC, abstractmethod

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False

class Owl(Bird):

    def reproduce(self):
        self.babies += 6

    def eat(self):
        return "Peck peck"

class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1

class Eagle(Bird):
    Fly = True
    extinct = False

    def noise(self):
        return "Screech"
    
    def repoduce(self):
        self.babies += 1

    def eat(self):
        return "Ouchie"

freedom = Eagle()
print(f"{freedom.noise()} + {freedom.eat()}")