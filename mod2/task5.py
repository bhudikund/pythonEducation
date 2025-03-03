line= input()

domains = []
current_domain = ""
for i in reversed(line):
    if i == '.':
        domains.append(current_domain[::-1])
        current_domain=""
    else:
        current_domain += i
if current_domain:
    domains.append(current_domain[::-1])

domains.reverse()
for d in domains:
    print(d)