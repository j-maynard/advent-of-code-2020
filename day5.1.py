#!/usr/bin/python3

def find_row(row):
    rows = []
    for i in range(128):
        rows.append(i)
    for x in list(row):
        half = int(len(rows) / 2)
        if x == "F":
            start_index = half
        else:
            start_index = 0
        for i in range(half):
            rows.pop(start_index)
    return rows[0]

def find_col(col):
    cols = []
    for i in range(8):
        cols.append(i)
    for x in list(col):
        half = int(len(cols) / 2)
        if x == "L":
            start_index = half
        else:
            start_index = 0
        for i in range(half):
            cols.pop(start_index)
    return cols[0]

def calc_seat_id(col, row):
    return row * 8 + col

def occupy_seat(seat):
    row_str = seat[0:7]
    col_str = seat[7:10]
    row = find_row(row_str)
    col = find_col(col_str)
    plane[row][col] = calc_seat_id(col, row)
    #print("Row = ", row, ", Col = ", col, ", Seat ID = ", calc_seat_id(col, row))

plane = []
seat_total = 0
for r in range(128):
    row = []
    for c in range(8):
        seat_total += 1
        row.append(0)
    plane.append(row)

f = open("day5-input.txt", "r")
finput = f.read().split("\n")
finput.pop()
count = 0
for s in finput:
    count += 1
    occupy_seat(s)

highest_seat_id = 0
for r in range(len(plane)):
    for s in range(len(plane[r])):
        if plane[r][s] > highest_seat_id:
            highest_seat_id = plane[r][s]

print("Highest Seat ID = ", highest_seat_id)
