#object oriented programming(oop)
#class, objects, properties(x-tics, attributes, features), 
#methods, constructors,
#principles of oop(abstruction, encaptsolation, inheritence, and polymorphism)
#overloadind, overriding
#oop is the programming concept(paradigm/belief) that advocate writing software based on real world projects
#objects are gotten from classes or they are classified.
#claases are identified in singular. the numbers of individual are the ones that make them plural
#a class is a blue print of an object
#an object is an instance of a class
#classes define the features, attributes, x-tics of the corresponding objects
#blue print means the original copy, format or a skeleton of something
#date, time, venue, name, contact, E and E 
#name, price, color, type, origin, size,
#name, age, gender, country, marital status, number of kids 
#"is a" is a phrase used to identify a class of a particular object
#an object should fulfill all properties of a class

students = ["Emma", "John", "Solomon", "Allan", "Faith", "Liz"]
student1 = {"name": "Emma", "Gender": "Male", "school": "Refactory academy"}

class laptop():
    pass
#name of the class should start with a capital letter
class food():
#these are the properties of the class food
    name = ""
    taste = ""
    calories = 0
    price = 0
    value = ""

#creating objects out of the class food
matooke = (food)

matooke.name = "matooke"
matooke.taste = "sweet"
matooke.calories = 0
matooke.price = 25000
matooke.value = "one"

rice = (food)

rice.name = "rice"
rice.taste = "salty"
rice.calories = 0
rice.price = 30000
rice.value = "two"

print(rice.name)
print(rice.taste)