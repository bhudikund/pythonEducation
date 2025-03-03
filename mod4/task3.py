def NOD(a,b):
    while(True):
        if a > b:
            a = a % b
            if(a == 0):
                return b
        else:
            b = b % a
            if(b == 0):
                return a


first,second = input().split(" ")
print(NOD(int(first),int(second)))