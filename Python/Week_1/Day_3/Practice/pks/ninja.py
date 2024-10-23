from pets import Pet

class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food ,pet):
        # def super().__init__(name,type,tricks,health,energy):
        self.fist_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet

    def walk(self):
        self.pet.play()  
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self

nousa=Pet("nousa","cat","intelegent","100 "," 100")
ninja1=Ninja("Batman","Mask","chiken wings","makrouna",nousa)
ninja1.feed().walk().bathe()
print(nousa.health)
