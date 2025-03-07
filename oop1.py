#classes
class Animal():
   name = "cow"
   type = "jersey"
   sounds = "moo"
   sizes = "big"
   color = "white"
   speed = "fast"

Lion = Animal()
#dot operator is used to access attributes, names of properties
Lion.name = "Lion"
Lion.type = "wild"
Lion.sounds = "roar"
Lion.sizes = " Small"
Lion.color = "black"
Lion.speed = "fast"

print(Lion.name)
print(Lion.type)
print(f"Lion: {Lion.name} - {Lion.type} - {Lion.speed} - {Lion.color} - {Lion.sizes}")
