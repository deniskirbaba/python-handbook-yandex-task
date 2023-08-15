out = []
while s := input():
    if s.endswith("@@@"):
        continue
    elif s.startswith("##"):
        out.append(s[2:])
    else:
        out.append(s)
for i in out:
    print(i)
