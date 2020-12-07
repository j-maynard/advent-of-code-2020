#!/usr/bin/python3                                                          
import json
import re

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
        
        if int(p["byr"]) < 1920 or int(p["byr"]) > 2002:
            continue

        if int(p["iyr"]) < 2010 or int(p["iyr"]) > 2020:
            continue

        if int(p["eyr"]) < 2020 or int(p["eyr"]) > 2030:
            continue

        if "cm" in p["hgt"] or "in" in p["hgt"]:
            if "cm" in p["hgt"]:
                hgt = int(p["hgt"].replace("cm", ""))
                if hgt < 150 or hgt > 193:
                    continue
            if "in" in p["hgt"]:
                hgt = int(p["hgt"].replace("in", ""))
                if hgt < 59 or hgt > 76:
                    continue
        else:
            continue
        
        if not re.search(r'^#(([0-9a-fA-F]{2}){3}|([0-9a-fA-F]){3})$', p["hcl"]):
            continue
        
        if len(p["pid"]) != 9:
            continue

        if p["ecl"] == "amb" \
        or p["ecl"] == "blu" \
        or p["ecl"] == "brn" \
        or p["ecl"] == "gry" \
        or p["ecl"] == "grn" \
        or p["ecl"] == "hzl" \
        or p["ecl"] == "oth":
            count = count + 1
            #p.pop('cid', None)
            #print(json.dumps(p, sort_keys=True))

    except KeyError:
        continue

print("Count = ", count)

