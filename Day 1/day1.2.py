#!/usr/bin/python3
f = open("day1-input.txt", "r")
finput = f.read().split("\n")

found = False

for i in finput:
    for x in finput:
        if x == '':
            break
        for y in finput:
            if y == '':
                break
            product = int(i) + int(x) + int(y)
            if product == 2020:
                result = int(i) * int(x) * int (y)
                print("%d * %d * %d = %d" % (int(i), int(x), int(y), result))
                found = True
                break
        if found:
            break
    if found:
        break
