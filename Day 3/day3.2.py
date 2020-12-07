#!/usr/bin/python3                                                          
f = open("day3-input.txt", "r")                                             
finput = f.read().split("\n")                                               
finput.pop()

routes = [ 
    {"right": 1, "down": 1, "result": 0},
    {"right": 3, "down": 1, "result": 0},
    {"right": 5, "down": 1, "result": 0},
    {"right": 7, "down": 1, "result": 0},
    {"right": 1, "down": 2, "result": 0}
]

def get_line(finput, y_cord, x_cord):
    line = finput[y_cord]
    while len(line) <= x_cord:
        line = line + finput[y_cord]
    return line

def get_trees_hit(finput, right, down):
    trees_hit = 0
    y_cord = 0
    x_cord = 0

    for x in range(len(finput)-1):
        x_cord = x_cord + right
        y_cord = y_cord + down
        if y_cord > len(finput):
            return trees_hit
        line = get_line(finput, y_cord, x_cord)
        if line[x_cord] == "#":
            trees_hit = trees_hit + 1
    return trees_hit
        
#trees_hit = get_trees_hit(finput, 3, 1)
for route in routes:
    route["result"] = get_trees_hit(finput, route["right"], route["down"])

total_trees_hit = 1
for route in routes:
    total_trees_hit = total_trees_hit * route["result"]

print("Trees hit = ", total_trees_hit)

