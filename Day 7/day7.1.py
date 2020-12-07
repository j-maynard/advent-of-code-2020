#!/usr/bin/python3
f = open("day7-input.txt", "r")
finput = f.read().split("\n")
finput.pop()

bags = []
for b in finput:
    b = b.replace('bags', '').replace('bag', '').replace('.', '').strip()
    bag = b.split("contain")[0].strip()
    con = b.split("contain")[1].split(',')
    contents = []
    for c in con:
        c = c.split(' ')
        c.pop(0)
        qty = c.pop(0)
        type = str(c).strip('[]').replace(',','').replace("'", '').strip()
        contents.append({ "qty": qty, "type": type })
    bags.append({"type":bag,"contents":contents})

def find_parents(bags, h, search):
    for b in bags:
        contents = []
        for c in b['contents']:
            contents.append(c['type'])
        
        if contents.count(search) > 0:
            h.add(b['type'])
            find_parents(bags, h, b['type'])

p = set()
find_parents(bags, p, 'shiny gold')
print(len(p))