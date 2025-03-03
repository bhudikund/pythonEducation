line = input()

arrayList = []
current_word = ""
string = ""
for i in reversed(line):
    string = i
    break


a= 0
for i in line:
    if i == string:
        a+=1
    else:
        break


print(a)