# Object oriented programming. Polymorphism.
class GameCharacter:

    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print ("Hi, my name is " + self.name + ".")

class Villain(GameCharacter):

    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self):
        print ("Hi, my name is " + self.name + " and I will kill you.")

    def kill(self, other):
        other.health = 0
        print ("Bang-bang, now you're dead.")

drogan_12 = GameCharacter("drogan_12", 23444, 67)
vlad_45 = Villain("vlad_45", 2325567, 150)
print (drogan_12.health)
drogan_12.speak()
vlad_45.speak()
vlad_45.kill(drogan_12)
print (drogan_12.health)
