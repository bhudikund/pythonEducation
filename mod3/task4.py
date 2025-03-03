line = input()

zero = line.count("0")
one = line.count("1")

if zero == one:
    print("yes")
else:
    print("no")