number_of_tickets = int(input('Введите желаемое количество билетов: '))
total = 0
result = ' '
for i in range(number_of_tickets):
    if number_of_tickets > 3:
        total -= round(total/100*10, 1)
    age = int(input('Введите возраст: '))
    if 18 <= age < 25:
        total += 990
    elif age >= 25:
        total += 1390
    else:
        total += 0
result = str(total)
print(result, 'рублей')
