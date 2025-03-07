names = ["Emma", "Mike", "John", "Jojo" ]
for n in names:
    if n == "John":
      break
print(n)

names = ["John", "Emma", "Mike", "Jojo" ]
for n in names:
    if n == "Mike":
      break
    print(n)
#continue statements

names = ["John", "Emma", "Mike", "Jojo" ]
for n in names:
    if n == "Emma":
      continue
    print(n)

#range statements
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]
for n in digits:
   print(n)
   if n == "6":
      break
   
   for p in range (10):
      print(p)

#while loop
count = 1
while count <= 5:
   print(count)
   count += 1

numbers = [10, 20, 30, 40, 50, 60, 70, 80, ]
def evens():
   for item in numbers: 
      if item % 2 == 0:
         print(item)
def fruits():
   for item in fruits:
      print(item)
      

