line = input()

numbers = []
start = 0
for i in range(len(line)):
    if line[i] == ' ':
        numbers.append(int(line[start:i]))
        start = i + 1

numbers.append(int(line[start:]))

a, b, c = numbers
if a <= b <= c or c <= b <= a:
    print(b)
elif b <= a <= c or c <= a <= b:
    print(a)
else:
    print(c)