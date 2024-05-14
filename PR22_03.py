class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Назва: {self.title}, Автор: {self.author}, Жанр: {self.genre}")

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("Двигун запущено")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Здійснено успішний внесок {amount}. Новий баланс: {self.balance}")
        else:
            print("Сума для внесення повинна бути більше 0.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Здійснено успішне зняття {amount}. Новий баланс: {self.balance}")
            else:
                print("Недостатньо коштів на рахунку.")
        else:
            print("Сума для зняття повинна бути більше 0.")

