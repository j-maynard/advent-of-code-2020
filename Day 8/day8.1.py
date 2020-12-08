#!/usr/bin/python3
f = open("day8-input.txt", "r")
finput = f.read().split("\n")
finput.pop()

acc = 0
jump = 0
instruction_set = []
instructions_run = []
index = 0

for i in finput:
    instruction_set.append({
        "instruction" : i.split(' ')[0],
        "value": int(i.split(' ')[1]),
        "run": False
    })

while instruction_set[index]['run'] == False:
    instruction_set[index]['run'] = True

    i = instruction_set[index]
    if i['instruction'] == "acc":
        acc += i['value']
        index += 1
    elif i['instruction'] == "jmp":
        index += i['value']
    else:
        index += 1

print('acc = ', acc)
