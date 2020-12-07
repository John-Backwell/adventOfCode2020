import re

def day_4_q1(input_file : str):
    with open(input_file) as data_file:
        text = data_file.read()
    passports = text.split("\n\n")
    count_correct = 0
    for passport in passports:
        fields = passport.split()
        tags = []
        for field in fields:
            tag = field[0:3]
            tags.append(tag)
        if len(fields) == 8:
            count_correct +=1
        else:
            if len(fields) == 7 and "cid" not in tags:
                count_correct +=1
    return count_correct    

print(day_4_q1("day_4.txt"))      