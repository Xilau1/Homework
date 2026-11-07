while True:
    num = int(input("Число:"))
    if num == 0:
        print("Number is equal to zero")
    elif num == 7:
        print("Good bye!")
        break
    elif num > 0:
        print("Number is positive")
    else:
        print("Number is negative")