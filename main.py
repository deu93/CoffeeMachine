class CoffeeMachine:
    def __init__(self):
        self.water_amount = 400
        self.milk_amount = 540
        self.coffee_beans_amount = 120
        self.disposable_cups = 9
        self.money_amount = 550
        self.cup_count_espresso = int(min(self.water_amount // 250, self.coffee_beans_amount // 16))
        self.cup_count_latte = int(min(self.water_amount // 350, self.milk_amount // 75, self.coffee_beans_amount // 20, self.disposable_cups // 1))
        self.cup_count_cappuccino = int(min(self.water_amount // 200, self.milk_amount // 100, self.coffee_beans_amount // 12, self.disposable_cups // 1))
        self.cup_count = 0
        self.cup_quanity1 = 1

    def process(self):
        print("Starting to make a coffee\nGrinding coffee beans\nBoiling water\nMixing boiled water with crushed "
              "coffee beans\nPouring coffee into the cup\nPouring some milk into the cup\nCoffee is ready!")

    def reagents_count(self):
        self.cup_quanity = int(input("Write how many cups of coffee you will need: \n"))
        self.milk_quanity = 50 * self.cup_quanity
        self.water_quanity = 200 * self.cup_quanity
        self.beans_quanity = 15 * self.cup_quanity
        print("For 25 cups of coffee you will need:")
        print(f"{self.water_quanity} of water\n{self.milk_quanity} of milk\n{self.beans_quanity} of coffee beans")
           
        
    def remaining(self):
        print()
        print(f"The coffee machine has:\n{self.water_amount} of water")
        print(f"{self.milk_amount} of milk")
        print(f"{self.coffee_beans_amount} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.money_amount} of money")
        print()
        
    def menu(self):
        print("Write action (buy, fill, take, remaining, exit):")
        while True:
            self.menu_choice = input()
            if self.menu_choice == "buy":
                self.buy()
                return self.menu()
            elif self.menu_choice == "fill":
                self.fill()
                return self.menu()
            elif self.menu_choice == "take":
                self.take()
                return self.menu()
            elif self.menu_choice == "exit":
                exit()
            
            elif self.menu_choice == "remaining":
                self.remaining()
                return self.menu()
            else:
                print("Wrong command")

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        self.coffee_choice = input()
        if self.water_amount >= 350:
            if self.coffee_beans_amount >= 20:
                if self.milk_amount >= 75:
                    if self.disposable_cups >= 1:
                        if self.coffee_choice == "1":
                            self.water_amount -= 250
                            self.coffee_beans_amount -= 16
                            self.disposable_cups -= 1
                            self.money_amount += 4
                            print("I have enough resources, making you a coffee!")
                            print()
                            return self.menu
                            
                        elif self.coffee_choice == "2":
                            self.water_amount -= 350
                            self.milk_amount -= 75
                            self.coffee_beans_amount -= 20
                            self.disposable_cups -= 1
                            self.money_amount += 7
                            print("I have enough resources, making you a coffee!")
                            print()
                            return self.menu
                            
                        elif self.coffee_choice == "3":
                            self.water_amount -= 200
                            self.milk_amount -= 100
                            self.coffee_beans_amount -= 12
                            self.disposable_cups -= 1
                            self.money_amount += 6
                            print("I have enough resources, making you a coffee!")
                            print()
                            return self.menu
                            
                        elif self.coffee_choice == "back":
                            return self.menu()

                        elif self.coffee_choice == "remaining":
                            self.remaining()   
                            
                        elif self.coffee_choice == "exit":
                            exit()

                        else:
                            print("Wrong command")
                            return self.buy()
                    else:
                        print("Sorry, not enough disposable cups!")
                else:
                    print("Sorry, not enough milk!")
            else:
                print("Sorry, not enough coffee beans!")
        else:
            print("Sorry, not enough water!")
    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water_amount += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk_amount += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans_amount += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.disposable_cups += int(input())
        

    def take(self):
        print(f"I gave you ${self.money_amount}")
        self.money_amount -= self.money_amount
        


my_machine = CoffeeMachine()
# my_machine.remaining()
my_machine.menu()