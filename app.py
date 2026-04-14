class Pet:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.happiness = 100
        self.money = 100
        self.hunger = 100
        
    def play(self, activity):
        self.happiness += 10
        self.hunger -= 15
        print (f"{self.name} is now playing {activity}.")
        if self.hunger <= 0:
            print(f"{self.name} starved to death.")
            exit()

    def end_day(self):
        print (f"{self.name} ends the day with:")
        print (f"{self.happiness} happiness.")
        print (f"{self.money} bucks.")
        print (f"{self.hunger} hunger.")
        self.Next = (input("Continue? "))
        if self.Next == "Yes":
            print (f"{self.name} wakes up on the next day.")
        elif self.Next == "No":
            exit()
        
    def show_status(self):
        print (f"{self.name} has {self.happiness} happiness, {self.money} bucks, and {self.hunger} hunger.")

    def make_unbalanced_moveset(self):
        self.happiness += 10
        self.money += 10
        self.hunger -+ 20
        print (f"{self.name} somehow made ten bucks after making an unbalanced moveset.")
        if self.hunger <= 0:
            print(f"{self.name} starved to death.")
            exit()

    def work(self):
        self.happiness -= 30
        self.money += 50
        self.hunger -= 30
        print (f"{self.name} dilly dallied at his job.")
        if self.hunger <= 0:
            print(f"{self.name} starved to death.")
            exit()
        if self.happiness <= 0:
            print(f"{self.name} broke down in tears.")
            exit()

    def buy(self, item, cost, amount):
        self.money -= cost*amount
        total = cost*amount
        self.inventory.append(item)
        if amount > 1:
            print (f"{self.name} bought {amount} {item}s for {total} bucks in total.")
        elif amount == 1:
            print (f"{self.name} bought {amount} {item} for {total} bucks in total.")
        if self.money <= 0:
            print (f"{self.name} went broke and cried himself to sleep.")
            exit()

    def feed(self, food):
        self.happiness += 10 
        self.hunger += 25
        self.money -= 30
        print (f"{self.name} ate {food}")
        if self.money <= 0:
            print (f"{self.name} went broke and cried himself to sleep.")
            exit()

    def backpack(self):
        print(self.inventory)

Pboy = Pet("Pboy", ["PC"])
Pboy.backpack()
Pboy.show_status()
Pboy.buy("thing", 5, 5)
Pboy.backpack()
Pboy.show_status()