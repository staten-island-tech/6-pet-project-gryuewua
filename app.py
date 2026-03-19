class Pet:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
        self.happiness = 100
        self.money = 100
        self.hunger = 100
        
    def play(self, activity):
        self.happiness += 10
        self.hunger -= 10
        print (f"{self.name} is now playing {activity}.")
        if self.hunger <= 0:
            print(f"{self.name} starved to death.")
            exit()

    def show_status(self):
        print (f"{self.name} ends the day with:")
        print (f"{self.happiness} happiness.")
        print (f"{self.money} bucks.")
        print (f"{self.hunger} hunger.")
        exit()

    def make_unbalanced_moveset(self):
        self.happiness += 10
        self.money += 10
        self.hunger -+ 10
        print (f"{self.name} somehow made ten bucks after making an unbalanced moveset.")
        if self.hunger <= 0:
            print(f"{self.name} starved to death.")
            exit()
    
    def buy(self, item, cost, amount):
        self.money -= cost*amount
        total = cost*amount
        if amount > 1:
            print (f"{self.name} bought {amount} {item}s for {total} bucks in total.")
        elif amount == 1:
            print (f"{self.name} bought {amount} {item} for {total} bucks in total.")
        if self.money <= 0:
            self.happiness -= 50
            print (f"{self.name} went broke and cried himself to sleep.")
            exit()

    def feed(self, food):
        self.happiness += 10 
        self.hunger += 25
        print (f"{self.name} ate a {food}")

Pboy = Pet("Pboy", ["PC"])
Pboy.play("jjs")
Pboy.make_unbalanced_moveset()
Pboy.buy("racket", 30, 2)
Pboy.feed("hotpot")
Pboy.show_status()