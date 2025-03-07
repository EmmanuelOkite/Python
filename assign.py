def enter_number():
    enter_number = int(input("the number of entries"))
    capture = {input("enter key: "): input("enter value") for _ in range(enter_number)}
    print (capture)
#
enter_number()
