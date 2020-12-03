#!/usr/bin/python3                                                          
f = open("day3-input.txt", "r")                                             
finput = f.read().split("\n")                                               
finput.pop()

trees_hit = 0
y_cord = 0
x_cord = 0

def get_line(finput, y_cord, x_cord):
    line = finput[y_cord]
    while len(line) <= x_cord:
        line = line + finput[y_cord]
    return line

for x in range(len(finput)-1):
    x_cord = x_cord + 3
    y_cord = y_cord + 1
    line = get_line(finput, y_cord, x_cord)
    print("y_cord = %d, x_cord = %d, line_length = %d" % (y_cord, x_cord, len(line)))
    if line[x_cord] == "#":
        trees_hit = trees_hit + 1

print("Trees hit = ", trees_hit)
    

