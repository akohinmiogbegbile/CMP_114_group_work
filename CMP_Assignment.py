class Maths:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def power(self, x, y):
        return x ** y


class Physics:
    def velocity(self, d, t):
        return d / t

    def acceleration(self, v1, v2, t):
        return (v2 - v1) / t

    def momentum(self, m, v):
        return m * v

    def force(self, m, a):
        return m * a

    def energy(self, m, v):
        return 0.5 * m * v ** 2


while True:
    print("Choose a subject:")
    print("1. Maths")
    print("2. Physics")
    subject = int(input())

    if subject == 1:
        calculator = Maths()
        break
    elif subject == 2:
        calculator = Physics()
        break
    else:
        print("Invalid choice. Try again.")

while True:
    print("Choose an operation:")
    if subject == 1:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
    elif subject == 2:
        print("1. Velocity")
        print("2. Acceleration")
        print("3. Momentum")
        print("4. Force")
        print("5. Energy")
    operation = int(input())

    if operation < 1 or operation > 5:
        print("Invalid choice. Try again.")
    else:
        break

if subject == 1:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    if operation == 1:
        result = calculator.add(x, y)
    elif operation == 2:
        result = calculator.subtract(x, y)
    elif operation == 3:
        result = calculator.multiply(x, y)
    elif operation == 4:
        result = calculator.divide(x, y)
    elif operation == 5:
        result = calculator.power(x, y)

    print(f"Result: {result}")

elif subject == 2:
    if operation == 1:
        d = float(input("Enter the distance: "))
        t = float(input("Enter the time: "))
        result = calculator.velocity(d, t)
    elif operation == 2:
        v1 = float(input("Enter the initial velocity: "))
        v2 = float(input("Enter the final velocity: "))
        t = float(input("Enter the time: "))
        result = calculator.acceleration(v1, v2, t)
    elif operation == 3:
        m = float(input("Enter the mass: "))
        v = float(input("Enter the velocity: "))
        result = calculator.momentum(m, v)
    elif operation == 4:
        m = float(input("Enter the mass: "))
        a = float(input("Enter the acceleration: "))
        result = calculator.force(m, a)
    elif operation == 5:
        m = float(input("Enter the mass: "))
        v = float(input("Enter the velocity: "))
        result = calculator.energy(m, v)

    print(f"Result:")