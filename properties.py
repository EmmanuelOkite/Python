#properties/ principles of oop
#Abstructions:something that is not clear/definitive
#encapsulation:ability to control or hide something from the internal functionality of it's data. eg football team
#polymorphisms:is the ability to take on more than one form
#inheritence is two individual classes sharing the same 
#inheritence is the ability of a sub/child-class to take on more than one attributes of a super/parent/base class

class Animal():
    name = ""
    color = ""
    owner = ""
#function within a class is called a method
#the statement you write in a method are rferred to as behavior
    def sound(self):
        print("I bark")
#creating a name
dog = Animal()
dog.sound() 

