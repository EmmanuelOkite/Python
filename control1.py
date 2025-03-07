#code to interprete
num1 = int(input("input your first number"))
num2 = int(input("input your second number"))
#
#operator = input("choose the operator")

if num1 >= num2:#full column, the next line should be indented by four spaces
    print("Error: First number should be less than the second number")
if num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}")# means num1 is divisible by num2 since it gives no remainder
#    
if num1 != 0:
    num2 += num1
    print(num2)