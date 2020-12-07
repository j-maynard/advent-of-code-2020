#!/usr/bin/python3
f = open("day2-input.txt", "r")
finput = f.read().split("\n")

valid_passwords = 0
count = 0

for line in finput:
    if line == '':
        break
    policy = line.split(":")[0]
    passwd = line.split(":")[1].strip()
    posa = int(policy.split(" ")[0].split("-")[0]) - 1
    posb = int(policy.split(" ")[0].split("-")[1]) - 1
    letter = policy.split(" ")[1]
    #print("passwd = %s, policy = %s, letter = %s, posa = %d, posb = %d, letter at pos a = %s, letter at pos b = %s" % (passwd, policy, letter, posa, posb, passwd[posa], passwd[posb]))
    if passwd[posa] == letter and passwd[posb] == letter:
        continue
    if passwd[posa] == letter or passwd[posb] == letter:
        valid_passwords = valid_passwords + 1

print("Total valid passwords = %d" % (valid_passwords))
