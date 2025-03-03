line= input()

number = []
current_number = ""
for i in reversed(line):
    if i == '.' or i == '-' or i == '(' or i == ')' or i == ' ' or i == '':
        number.append(current_number[::-1])
        current_number=""
    else:
        current_number += i
if current_number:
    number.append(current_number[::-1])

number.reverse()

string = ''
for j in number:
    string += str(j)+ ''
print(string)
