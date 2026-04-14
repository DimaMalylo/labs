# 1. Vehicle і Car

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self):
        print(f"Driving at {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand


# Демонстрація
car = Car(120, "Toyota")
print(f"Car brand: {car.brand}")
car.drive()


# 2. Person і Student

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old")


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old, I study at {self.university}")


# Демонстрація
student = Student("Dmytro", 18, "NULP")
student.introduce()


# 3. Teacher, Researcher, Professor (множинне наслідування)

class Teacher:
    def teach(self):
        print("Teaching")


class Researcher:
    def research(self):
        print("Researching")


class Professor(Teacher, Researcher):
    def teach(self):
        print("Teaching at university")


# Демонстрація
prof = Professor()
prof.teach()
prof.research()


# 4. ElectricDevice, BatteryPowered, Smartphone

class ElectricDevice:
    def turn_on(self):
        print("Device is turned on")


class BatteryPowered:
    def __init__(self, battery_level):
        self.battery_level = battery_level


class Smartphone(ElectricDevice, BatteryPowered):
    def __init__(self, battery_level):
        BatteryPowered.__init__(self, battery_level)

    def use_app(self, app_name):
        print(f"Using app: {app_name}")


# Демонстрація
phone = Smartphone(85)
phone.turn_on()
print(f"Battery level: {phone.battery_level}%")
phone.use_app("Instagram")


# 5. Shape, Circle, Rectangle

import math

class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Демонстрація
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle area: {circle.area()}")
print(f"Rectangle area: {rectangle.area()}")


# 6. Порядок виклику конструкторів (MRO)

class A:
    def __init__(self):
        print("A")
        super().__init__()


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()


class E(D):
    def __init__(self):
        print("E")
        super().__init__()


# Демонстрація
print("MRO:", [cls.__name__ for cls in E.mro()])
e = E()


# 7. Наслідування vs композиція

class Engine:
    def start(self):
        print("Engine started")


# Наслідування
class CarInheritance(Engine):
    pass


# Композиція
class CarComposition:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()


# Демонстрація
car_inh = CarInheritance()
car_inh.start()

car_comp = CarComposition()
car_comp.start()


