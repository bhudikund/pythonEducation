def palindrome(word):
    if word == word[::-1]:
        return True

line = input().split(" ")

for i in line:
    if palindrome(i):
        print(i)
