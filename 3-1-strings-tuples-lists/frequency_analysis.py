out = list()
while s := input():
    if s.strip().startswith('#'):
        continue
    idx = s.find('#')
    if idx != -1:
        out.append(s[:idx].rstrip())
for i in out:
    print(i)
