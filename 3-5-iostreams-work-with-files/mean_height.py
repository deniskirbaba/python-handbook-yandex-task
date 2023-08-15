from sys import stdin

diff = []
for line in stdin:
    name, h_past, h_now = line.split()
    diff.append(int(h_now) - int(h_past))
print(round(sum(diff) / len(diff)))
