#!/usr/bin/python3                                                          
import json

f = open("day4-input.txt", "r")                                             
finput = f.read().split("\n")                                               
finput.pop()

valid_passports = 0
passports = "" 
# Seperate passports and turn them to JSON
passports_str = "{ \"passport\": ["
passport_data = ""
for line in finput:
    if line.strip() == '':
        passport_data = passport_data.strip().replace(" ", "\", \"")
        passport_data = passport_data.replace(":", "\": \"")
        passport_data = "{\"" + passport_data + "\"}, "
        passports_str = passports_str + passport_data
        passport_data = ""
        continue
    passport_data = passport_data + " " + line.strip()
passports_str = passports_str + "]}"
passports = json.loads(passports_str.replace("}, ]}", "}]}"))

count = 0

for p in passports["passport"]:
    try:
        if p["byr"] is None \
        or p["iyr"] is None \
        or p["eyr"] is None \
        or p["hgt"] is None \
        or p["hcl"] is None \
        or p["ecl"] is None \
        or p["pid"] is None:
            continue
        count = count + 1
    except KeyError:
        continue

print("Count = ", count)

