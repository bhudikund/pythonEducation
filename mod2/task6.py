line = input()

a = 0
b = 0
for i in line:
    if i == "1":
        a += 1
    elif i == "0":
        b +=1

if a == b:
    print("yes")
else:
    print("no")