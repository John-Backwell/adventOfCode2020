def split_input(line):
    beginning, middle, password = line.split(" ")
    minimum, maximum = [int(i) for i in beginning.split("-")]
    test_char = middle[0]
    return password,minimum,maximum,test_char

def day_2_q1(input_file: str):
    with open("day_2.txt") as data_file:
        data = [line for line in data_file]
    total_correct_lines = 0
    for line in data:
        password,minimum, maximum, test_char = split_input(line)
        total_chars = password.count(test_char)
        if total_chars >= minimum and total_chars <= maximum:
            total_correct_lines +=1  
    return total_correct_lines

def day_2_q2(input_file:str):
    with open("day_2.txt") as data_file:
        data = [line for line in data_file]
    total_correct_lines = 0
    for line in data:
        password, index_1, index_2, test_char = split_input(line)
        bool_1 = password[index_1-1] == test_char
        bool_2 = password[index_2-1] == test_char
        valid_line = bool_1 != bool_2
        if valid_line:
            total_correct_lines +=1
    return total_correct_lines

print(day_2_q1("day_2.txt"))
print(day_2_q2("day_2.txt"))
