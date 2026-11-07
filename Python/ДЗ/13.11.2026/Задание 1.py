A = int(input("От:"))
B = int(input("До:"))

summaeven = 0
summaodd = 0
summanine = 0

arithmeticeven = 0
arithmeticodd = 0
arithmeticnine = 0

for i in range(A, B + 1):
    if i % 2 == 0:
        summaeven += i
        arithmeticeven += 1
    else:
        summaodd += i
        arithmeticodd += 1
    if i % 9 == 0:
        summanine += i
        arithmeticnine += 1

arithmeticeven2 = summaeven / arithmeticeven
arithmeticodd2 = summaodd / arithmeticodd
arithmeticnine2 = summanine / arithmeticnine

print(f"Четные: Сумма: {summaeven}, среднее арифмитическое: {arithmeticeven2}, всего: {arithmeticeven}")
print(f"Нечетные: Сумма: {summaodd}, среднее арифмитическое: {arithmeticodd2}, всего: {arithmeticodd}")
print(f"Кратные 9: Сумма: {summanine}, среднее арифмитическое: {arithmeticnine2}, всего: {arithmeticnine}")