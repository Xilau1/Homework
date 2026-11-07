summa = 0
maximum = None
minimum = None

while True:
    num = int(input("Число:"))
    if num == 7:
        print("Good bye!")
        break
    summa += num
    if maximum is None or num > maximum:
        maximum = num
        
    if minimum is None or num < minimum:
        minimum = num
    print(f"Сумма: {summa}, Максимум: {maximum}, Минимум: {minimum}")