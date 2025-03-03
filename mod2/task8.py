line = input()

arrayList = []
current_word = ""
for i in line:
    if i == ' ':
        arrayList.append(current_word)
        current_word=""
    else:
        current_word += i
if current_word:
    arrayList.append(current_word)

newWord = ""
for i in arrayList:
    newWord += i[-1]

print(newWord)