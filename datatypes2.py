#sequence
num1, num2, num3 = 100, 300, 500
numbers = [100, 300, 500]
numbers1 = [num1, num2, num3]
numbers2 = []
things = [100, "Hello", 300.0, True, [1, 2, 3]]
print(type(num1))
print(numbers[2])
print(things[1])
print(things[4])
trouble = [20, [30,[100, 20,[500]]]]
print(trouble[1][1][2][0])
#a list in python is a collection of values in one single location/ variable identified with a square bracket
trouble.append(40)
print(trouble)
trouble.pop()
print(trouble)

#tuple are read only sequences
mytuple = (100, 300, 500)
