def add():
    a, b = 20, 40
    print(a + b)
add()

def add1():
    a = int(input("please input your first number:\n"))
    b = int(input("please input your second number:\n"))
    print(a + b)
#add1()

def add2():
    a = int(input("please input your number:\n"))
    b = int(input("please input your second number:\n"))
    if a % b == 0:
        print(f"{a} dosen't give remainder")
    else:
        print(f"{a} does give remainder")
        
add2()
