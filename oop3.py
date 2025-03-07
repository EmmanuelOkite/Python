class Fruit:
#we use the first item to identify in the parenthesis
    def __init__(emma, name, color,size, taste, price):
        emma.name = name
        emma.size = size
        emma.color = color
        emma.taste = taste
        emma.price = price
mango = Fruit("mango", "yellow", "small", "yummy", "2000")
apple = Fruit("apple", "green", "small", "sweet", "1000")
#remember self is not a keyword, we can use any work as a keyword

class Animal:
#this is a constructor, it starts with self
    def __init__(self, name, breed, color, age, size):
        self.animalname = name
        self.animalbreed = breed
        self.animalcolor = color
        self.animalage = age
        self.animalsize = size

    def details(self):
        print(f"animalname: {self.animalname}, animalbreed: {self.animalbreed} animalcolor: {self.animalcolor}, animalage: {self.animalage}")
#dog class has inherited from animal class. it now has two methods
#when u inherit class, u also inherit the methods
class Dog(Animal):
    def sound(self):
        print("dog Woofs")

class Bulldog(Dog):
    def great(self):
        print("Bulldog wigs")
dog = Dog("max", "german shepherd", "brown", "big", 10)
dog.details()
