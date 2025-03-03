a = map(int, input().split())


seen = set()
duplicates = []

for i in a:
    if i in seen:
        duplicates.append(i)
    else:
        seen.add(i)

if duplicates:
    print(True)
else:
    print(False)
