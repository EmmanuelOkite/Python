#the numbers of values in a parenthesis is called a parameter list
#both static and dynamic functions return values
#arguments must fulfill the parameter lists

def add():
    #static
    num1, num2, = 20, 30
    #print(num1 + num2)
    return num1 + num2
    print(num1)
#calling the function
#function add does not allow access to values
#the return ststement marks the end ofexecution in the function
add()
print(add())
num3 = add()
print(num3)



    