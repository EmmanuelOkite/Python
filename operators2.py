 #comparison operators compares two values and return a boolean
comp1 = 200
comp2 = 300
print(comp1 < comp2)
print(comp1 > comp2)
print(comp1 >=comp2)
print(comp1 <= comp2)
print(comp1 != comp2)#this is how we say not eguals to
print(comp1 == comp2)
#write comment ontop of the line you want to comment about

#Logical operators
#and, (&) or, (||) not, (!)
log1 = 5
log2 = 6
print((log1 > log2) and (log2<log1))
print( not (log2 < log1))
print((log1 > log2) or (log2<log1))
print(True and True)
print(True and False)
print(not True)
print(True or True)
print(True or False)
print(False or False)

#membership operators
numbers = {20, 30, 40, 50}
print(20 in numbers)
print(20 not in numbers)

name = "ozzy"
print("o" not in name)
print("O" not in name)

      
#identity operators
#we have is,

print(20 is 20)
