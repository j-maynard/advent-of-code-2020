#!/usr/bin/python3
f = open("day8-input.txt", "r")
finput = f.read().split("\n")
finput.pop()

def get_instruction_set():
    instruction_set = []
    for i in finput:
        instruction_set.append({
            "instruction" : i.split(' ')[0],
            "value": int(i.split(' ')[1]),
            "order": []
        })
    return instruction_set

def run_instruction_set(change, change_line):
    order = 0
    acc = 0
    index = 0
    i_set = get_instruction_set()
    i_set[change_line]['instruction'] = change
    run = True
    while run:
        i_set[index]['order'].append(order)
        order += 1

        i = i_set[index]
        if i['instruction'] == "acc":
            acc += i['value']
            index += 1
        elif i['instruction'] == "jmp":
            index += i['value']
        else:
            index += 1
        
        if (len(i_set) - 1) == index:
            run = False
            return True, acc
        
        if len(i['order']) > 10:
            run = False
            return False, 0
    

def find_change():
    instruction_set = get_instruction_set()
    for i in range(len(instruction_set)):
        suc = False
        acc = 0
        if instruction_set[i]['instruction'] == 'jmp':
            suc, acc = run_instruction_set('nop', i)
        elif instruction_set[i]['instruction'] == 'nop':
            suc, acc = run_instruction_set('jmp', i)
        if suc:
            print("Run ", i, "Success, Accumulator = ", acc)
            break


find_change()
