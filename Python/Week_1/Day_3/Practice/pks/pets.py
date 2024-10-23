class Pet:
    def __init__(self,name,type,tricks,health,energy):
        
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=health
        self.energy=energy

    def sleep(self):
        self.energy+=25
        return self
    def eat(self):
        self.energy+=str(5)
        self.health+=str(10)
        return self
    def play(self):
        self.health+=str(5)
        return self
    def noise(self):
        print("baw")
        return self      
    

