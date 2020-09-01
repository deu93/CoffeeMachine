class CoffeeMachine:
    def __init__(self):
        pass

    def process(self):
        print("Starting to make a coffee\nGrinding coffee beans\nBoiling water\nMixing boiled water with crushed "
              "coffee beans\nPouring coffee into the cup\nPouring some milk into the cup\nCoffee is ready!")

    def reagents(self):
        self.cup_quanity = int(input("Write how many cups of coffee you will need: \n"))
        self.milk_quanity = 50 * self.cup_quanity
        self.water_quanity = 200 * self.cup_quanity
        self.beans_quanity = 15 * self.cup_quanity
        print("For 25 cups of coffee you will need:")
        print(f"{self.water_quanity} of water\n{self.milk_quanity} of milk\n{self.beans_quanity} of coffee beans")

    def amount_cups(self):
        self.water_rest = int(input("Write how many ml of water the coffee machine has:\n"))
        self.milk_rest = int(input("Write how many ml of milk the coffee machine has:\n"))
        self.coffee_beans_rest = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
        self.cup_quanity1 = int(input("Write how many cups of coffee you will need: \n"))
        self.cup_count = int(min(self.water_rest // 200, self.milk_rest // 50, self.coffee_beans_rest // 15))
        if self.cup_count < self.cup_quanity1:
            print(f"No, I can make only {self.cup_count} cups of coffee")
        elif self.cup_count == self.cup_quanity1:
            print("Yes, I can make that amount of coffee")
        else:
            self.cup_more = self.cup_count - self.cup_quanity1
            print(f"Yes, I can make that amount of coffee (and even {self.cup_more} more than that)")


my_machine = CoffeeMachine()
my_machine.amount_cups()
