#!/usr/bin/python3
f = open("day1-input.txt", "r")
finput = f.read().split("\n")

found = False

for i in finput:
    for x in finput:
        if x == '':
            break
        product = int(i) + int(x)
        if product == 2020:
            result = int(i) * int(x)
            print("%d * %d = %d" % (int(i), int(x), result))
            found = True
            break
    if found:
        break
