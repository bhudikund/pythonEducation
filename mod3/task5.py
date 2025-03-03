line = input()

string = line.split(" ")
word = ""
for i in string:
    word += i[-1]
print(word)