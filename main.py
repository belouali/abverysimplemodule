from abverysimplemodule.extras.multiply import multiply
from abverysimplemodule.extras.divide import divide
from abverysimplemodule.add import add
from abverysimplemodule.subtract import subtract


class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return add(self.x, self.y)

    def mul(self):
        return multiply(self.x, self.y)

    def div(self):
        return divide(self.x, self.y)

    def sub(self):
        return subtract(self.x, self.y)


if __name__ == "__main__":

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    obj = Calculator(a, b)
    choice = 1
    while choice != 0:
        print("0. Exit")
        print("1. Add")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("Result: ", obj.addition())
        elif choice == 2:
            print("Result: ", obj.sub())
        elif choice == 3:
            print("Result: ", obj.mul())
        elif choice == 4:
            print("Result: ", round(obj.div(), 2))
        elif choice == 0:
            print("Exiting!")
        else:
            print("Invalid choice!!")

    print()
