#!/usr/bin/python3
f = open("day6-input.txt", "r")
finput = f.read().split("\n")

groups = []
group = ""
for g in finput:
    if g.strip() == "":
        groups.append(group)
        group = ""
        continue
    group += g.strip()

t = 0

for g in groups:
    l = list(g)
    ans = set(l)
    t = t + len(ans)

print("Total answers = ", t)
