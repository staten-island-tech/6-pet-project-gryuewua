class Pet:
    def __init__(self, name, happiness, money):
        self.name = name
        self.happiness = happiness
        self.money = money
    
    def play(self, activity):
        self.happiness += 10
        print (f"{self.name} is now playing {activity}.")

    def show_status(self):
        print (f"{self.name} now has {self.happiness} happiness.")
        print (f"{self.name} now has {self.money} bucks.")

    def make_unbalanced_moveset(self):
        self.happiness += 10
        self.money += 10
        print (f"{self.name} somehow made ten bucks after making an unbalanced moveset.")
    
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
        


Pboy = Pet("Pboy", 50,100)
Pboy.play("jjs")
Pboy.make_unbalanced_moveset()
Pboy.buy("racket", 30, 2)
Pboy.show_status()