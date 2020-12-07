#!/usr/bin/python3
f = open("day6-input.txt", "r")
finput = f.read().split("\n")

groups = []
group = []
for g in finput:
    if g.strip() == "":
        groups.append(group)
        group = []
        continue
    group.append(list(g.strip()))
t = 0
for g in groups:
    answers = set()
    for p in g:
        answers |= set(p)
    
    for a in answers:
        commonanswer = 0
        for p in g:
            if p.count(a) == 1:
                commonanswer += 1
        if len(g) == commonanswer:
            t += 1

print("Total answers = ", t)
