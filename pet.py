class Pet:
    def __init__(self,name, hungerLvls, energyLvls, happinessLvls):
        self.name = name
        self.hunger = hungerLvls
        self.energy = energyLvls
        self.happiness = happinessLvls
        self.tricks=[]

    def eat(self):

        if self.hunger <= 3:
            print("Cannot subtract")
        else:
            self.hunger = self.hunger -3 
            self.happiness = self.happiness + 1
    def sleep(self):
        # increase energy by 5
        if (self.energy < 10):
            self.energy = self.energy + 5
            print(f"increases energy by 5 to {self.energy}")
            

    def play(self):
        print(f"Before play energy : {self.energy}, happiness : {self.happiness} and hunger : {self.hunger}")
        # decrease energy by 2, increase happiness by 2 and  increase hunger by 1
        self.energy = self.energy - 2
        self.happiness = self.happiness + 2
        self.hunger = self.hunger + 1
        print(f"After play energy : {self.energy}, happiness : {self.happiness} and hunger : {self.hunger}")  
    def get_status(self):
        # print the current status of the object
        print(f"Status of pet \n Energy: {self.energy} \n Happiness: {self.happiness} \n  Hunger: {self.hunger}") 
    def train(self):
        new_trick  = input("Enter any trick for your pet ?: ")
        self.tricks.append(new_trick)

    def show_tricks(self):
        i = 1
        for item in self.tricks:
            print(f"trick {i} is {item}")
            i  = i + 1             
pet1 = Pet("Jupiter", 8, 8, 8)
pet1.eat()
pet1.sleep()
pet1.play()
pet1.get_status()
pet1.train()
pet1.show_tricks()
      
      
