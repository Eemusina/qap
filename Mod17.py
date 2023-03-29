try:
    number_sequence = [int(x) for x in input("Введите целые числа в любом порядке через пробел: ").split()]
    if number_sequence is type(float):
        raise Exception
except ValueError:
    print("Ошибка: не соответствует условиям ввода. Нужно ввести целые числа через пробел!")
    number_sequence = [int(x) for x in input("Введите целые числа в любом порядке через пробел: ").split()]
    for i in range(len(number_sequence)):
        for j in range(len(number_sequence) - i - 1):
            if number_sequence[j] > number_sequence[j + 1]:
                number_sequence[j], number_sequence[j + 1] = number_sequence[j + 1], number_sequence[j]
    print(number_sequence)
else:
    for i in range(len(number_sequence)):
        for j in range(len(number_sequence) - i - 1):
            if number_sequence[j] > number_sequence[j + 1]:
                number_sequence[j], number_sequence[j + 1] = number_sequence[j + 1], number_sequence[j]
    print(number_sequence)


try:
    num = int(input("Введите любое целое число: "))
    if num is type(float):
        raise Exception
except ValueError:
    print("Ошибка: не соответствует условиям ввода. Нужно ввести целое число!")
    num = int(input("Введите любое целое число: "))

def bi_search(a: int, number_sequence: list) -> int:
    left, right = 0, len(number_sequence)
    while left < right:
        middle = (left + right) // 2
        if number_sequence[middle] < a:
            left = middle + 1
        else:
            right = middle
    return left
print(bi_search(num, number_sequence))
