#how you  declare a class under encapsulation
class Animal:
#this  is a constructor defined wiyh two  underscores
#a constructor  is used to initialize/ give a value of an object of a class
#self is used to identify the properties of a class, you can use any word
#animal name is the property of the class animal

    def __init__(self, name, size, color,):
        self.animalname = name
        self.animalsize = size
        self.animalcolor = color

cat = Animal("cat", "small", "black")
dog = Animal("dog", "big", "black")

print(cat.get_animal_details()) 
