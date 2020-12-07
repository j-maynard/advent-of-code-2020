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
        if qty == 'no':
            continue
        type = str(c).strip('[]').replace(',','').replace("'", '').strip()
        contents.append({ "qty": int(qty), "type": type })
    bags.append({"type":bag,"contents":contents})

def find_bag(bags, search):
    bag = None
    for b in bags:
        if b['type'] == search:
            return b

def find_contents(bags, contents, search):
    bag = find_bag(bags, search)
    x = 0
    for c in bag['contents']:
        for i in range(c['qty']):
            find_contents(bags, contents, c['type'])
            contents.append(c['type'])

contents = []
find_contents(bags, contents, "shiny gold")test
print(len(contents))