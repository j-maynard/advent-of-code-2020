#!/usr/bin/python3
f = open("day2-input.txt", "r")
finput = f.read().split("\n")

valid_passwords = 0

for line in finput:
    if line == '':
        break
    policy = line.split(":")[0]
    passwd = line.split(":")[1]
    mino = int(policy.split(" ")[0].split("-")[0])
    maxo = int(policy.split(" ")[0].split("-")[1])
    count = len(passwd.split(policy.split(" ")[1]))
    if count >= mino+1 and count <= maxo+1:
        valid_passwords = valid_passwords + 1

print("Total valid passwords = %d" % (valid_passwords))
