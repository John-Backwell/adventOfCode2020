def load_file(input_file: str):
    with open(input_file) as data_file:
        return data_file.read().splitlines()

def day_8_q1(input_file: str)-> int:
    lines = load_file(input_file)
    visited_lines = []
    acc = 0
    x = 0
    while x < len(lines):
        if x in visited_lines:
            return acc
        visited_lines.append(x)
        instruction = lines[x][0:3]
        operation = lines[x][4:]
        if instruction == "acc":
            acc_amount = parse_instruction(operation)
            acc += acc_amount
            x +=1
        elif instruction == "jmp":
            jmp_amount = parse_instruction(operation)
            x+= jmp_amount
        elif instruction == "nop":
            x +=1
    return acc

def parse_instruction(instruction : str)->int:
    sign = instruction[0]
    if sign == "+":
        return int(instruction[1:])
    elif sign == "-":
        return -(int(instruction[1:]))

def day_8_q2(input_file:str)-> int:
    lines = load_file(input_file)
    target_index = len(lines)
    acc = 0
    x = 0
    for index, line in enumerate(lines):
        acc = 0
        visited_lines = []
        instruction = line[0:3]
        tail = line[3:]
        if instruction == "jmp":
            new_instruction = "nop"
            lines_copy = lines.copy()
            lines_copy[index] = new_instruction + tail
            acc = check_loop(lines_copy,visited_lines, acc, target_index )
            if acc > 0:
                return acc
        elif instruction == "nop":
            new_instruction == "jmp"
            lines_copy = lines.copy()
            lines_copy[index] == new_instruction + tail
            acc = check_loop(lines_copy,visited_lines, acc, target_index )
            if acc > 0:
                return acc

def check_loop(lines, visited_lines, acc, target_index):
    x = 0
    while x < len(lines):
            if x in visited_lines:
                return 0
            visited_lines.append(x)
            instruction = lines[x][0:3]
            operation = lines[x][4:]
            if instruction == "acc":
                acc_amount = parse_instruction(operation)
                acc += acc_amount
                x +=1
            elif instruction == "jmp":
                jmp_amount = parse_instruction(operation)
                x+= jmp_amount
            elif instruction == "nop":
                x +=1
            if x == target_index:
                return acc

print(day_8_q2("day_8.txt"))