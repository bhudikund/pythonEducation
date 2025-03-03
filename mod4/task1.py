def func(numbers):
    if all(x == numbers[0] for x in numbers):
        print("Все числа равны")
    elif len(numbers) == len(set(numbers)):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

line = input()
number = list(map(int, line.split()))
func(number)