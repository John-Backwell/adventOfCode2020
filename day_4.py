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
        elif len(fields) == 7 and "cid" not in tags:
                count_correct +=1
    return count_correct    

def day_4_q2(input_file: str):
    with open(input_file) as data_file:
        text = data_file.read()
    total_correct = 0   
    passports = text.split("\n\n")
    key_dict = {"byr": check_byr,"iyr": check_iyr,"eyr": check_eyr,"hgt": check_hgt,"hcl": check_hcl,"ecl": check_ecl,"pid": check_pid}
    for passport in passports:
        correct_fields = 0
        fields_dict = {}
        fields = passport.split()
        for field in fields:
            fields_dict.setdefault(field[:3], field[4:])
        for key in fields_dict.keys():
            current_func = key_dict.get(key,return_false)
            if current_func(fields_dict[key]):
                correct_fields +=1
        if correct_fields == 7:
            total_correct +=1
    return total_correct

def check_byr(string : str):
    return int(string) >= 1920 and int(string) <=2002

def check_iyr(string : str):
    return int(string) >= 2010 and int(string) <=2020

def check_eyr(string : str):
    return int(string) >= 2020 and int(string) <=2030

def check_hgt(string : str):
    unit = string[-2:]
    if unit == "cm":
        return int(string[:-2]) >= 150 and int(string[:-2]) <=193
    if unit == "in":
        return int(string[:-2]) >= 59 and int(string[:-2]) <=76

def check_hcl(string : str):
    return string[0] == '#' and string[1:].isalnum() and len(string) == 7
      
def check_ecl(string : str):
    valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if string in valid_colours:
        return True
    return False   

def check_pid(string : str):
    return len(string) == 9 and string.isnumeric()

def return_false(string:str):
    return False

day_4_q1("day_4.txt")
print(day_4_q2("day_4.txt"))
