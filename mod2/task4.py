a = int(input())

def convert_to(number, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result


print(f"{convert_to(a,2)}, {convert_to(a,8)}, {convert_to(a,16)}")