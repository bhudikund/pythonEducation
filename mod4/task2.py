def recursion(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        return recursion((a*a),n / 2)
    else:
        return a * recursion(a, n - 1)


a,b = input().split(" ")

print(recursion(int(a), int(b)))