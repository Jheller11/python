class Person(object):
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def greeting(self):
        print(f"{self.name} says hi.")

    def how_old(self):
        print(f"I am {self.age} years old.")

    def where(self):
        print(f"I live in {self.location}.")

    def get_older(self):
        self.age += 1
        self.how_old()


a = Person('Jeff', 32, 'NYC')
a.greeting()
a.how_old()
a.where()

aging = input('Should I age by one year? (True/False) ')

if aging:
    a.get_older()
