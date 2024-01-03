def request_input() -> int:
    while True:
        try:
            input_value = int(input())
            return input_value
        except ValueError:
            print("Please enter an integer")


class CoffeeMachine:
    supplies = {'water': 400, 'milk': 540, 'coffee_beans': 120, 'cups': 9}
    money = 550
    espresso = {'water': 250, 'milk': 0, 'coffee_beans': 16, 'cups': 1, 'price': 4}
    latte = {'water': 350, 'milk': 75, 'coffee_beans': 20, 'cups': 1, 'price': 7}
    cappuccino = {'water': 200, 'milk': 100, 'coffee_beans': 12, 'cups': 1, 'price': 6}

    def show_supplies(self):
        print("The coffee machine has:")
        print(f"{self.supplies['water']} ml of water")
        print(f"{self.supplies['milk']} ml of milk")
        print(f"{self.supplies['coffee_beans']} g of coffee beans")
        print(f"{self.supplies['cups']} disposable cups")
        print(f"${self.money} of money")

    def get_user_choice(self):
        print("Write action (buy, fill, take, remaining, exit):")
        while True:
            user_choice = input()
            if user_choice.lower() in ["buy", "fill", "take", "remaining", "exit"]:
                return user_choice.lower()
            else:
                print("Please select one of the actions: buy, fill, take, remaining, exit")

    def check_if_enough_supplies(self, coffee_type: int) -> list:
        not_enough_supplies = []
        if coffee_type == 1:
            not_enough_supplies = [key for key in self.supplies.keys() if self.espresso[key] > self.supplies[key]]
        elif coffee_type == 2:
            not_enough_supplies = [key for key in self.supplies.keys() if self.latte[key] > self.supplies[key]]
        elif coffee_type == 3:
            not_enough_supplies = [key for key in self.supplies.keys() if self.cappuccino[key] > self.supplies[key]]
        return not_enough_supplies

    def make_coffee(self, coffee_type: int):
        if coffee_type == 1:
            for key in self.supplies.keys():
                self.supplies[key] -= self.espresso[key]
            self.money += self.espresso['price']
        elif coffee_type == 2:
            for key in self.supplies.keys():
                self.supplies[key] -= self.latte[key]
            self.money += self.latte['price']
        elif coffee_type == 3:
            for key in self.supplies.keys():
                self.supplies[key] -= self.cappuccino[key]
            self.money += self.cappuccino['price']

    def buy_coffee(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        while True:
            selected_option = input()
            if selected_option in ["1", "2", "3", "back"]:
                break
            else:
                print("Please enter 1, 2, or 3 if you want a coffee. Type \"back\" to return to the previous step")
        if selected_option == "back":
            pass
        else:
            if len(self.check_if_enough_supplies(int(selected_option))) == 0:
                print("I have enough resources, making you a coffee!")
                self.make_coffee(int(selected_option))
            else:
                print(f"Sorry, not enough {', '.join(self.check_if_enough_supplies(int(selected_option)))}!")

    def fill_machine(self):
        print("Write how many ml of water you want to add:")
        self.supplies["water"] += request_input()
        print("Write how many ml of milk you want to add:")
        self.supplies["milk"] += request_input()
        print("Write how many grams of coffee beans you want to add:")
        self.supplies["coffee_beans"] += request_input()
        print("Write how many disposable cups you want to add:")
        self.supplies["cups"] += request_input()

    def take_money(self):
        print(f"I gave you {self.money}")
        self.money = 0


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    while True:
        choice = coffee_machine.get_user_choice()
        if choice == "buy":
            coffee_machine.buy_coffee()
        elif choice == "fill":
            coffee_machine.fill_machine()
        elif choice == "take":
            coffee_machine.take_money()
        elif choice == "remaining":
            coffee_machine.show_supplies()
        elif choice == "exit":
            break
