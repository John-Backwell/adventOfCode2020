def upper(nums :[int]):
    return nums[-(len(nums)//2):]

def lower(nums: [int]):
    return nums[:len(nums)//2] 

def load_file(input_file: str):
    with open(input_file) as data_file:
        data = data_file.read().splitlines()
    return data

def day_5_q1(input_file: str):
    data = load_file(input_file)
    commands_dict = {"F": lower, "B":upper, "R":upper, "L": lower}
    highest_id = 0
    for line in data:
        FB = line[:-3]
        RL = line[-3:]
        max_row = [i for i in range (128)]
        max_column = [i for i in range (8)]
        for char in FB:
            func = commands_dict.get(char)
            max_row = func(max_row)
        for char in RL:
            func = commands_dict.get(char) 
            max_column = func(max_column)
        unique_id = calculate_unique_id(max_row[0], max_column[0])
        if unique_id > highest_id:
            highest_id = unique_id
    return highest_id
    
def calculate_unique_id(row:int, column :int):
    return (row*8) + column

def day_5_q2(input_file: str):
    data = load_file(input_file)
    commands_dict = {"F": lower, "B":upper, "R":upper, "L": lower}
    id_list = []
    for line in data:
        FB = line[:-3]
        RL = line[-3:]
        max_row = [i for i in range (128)]
        max_column = [i for i in range (8)]
        for char in FB:
            func = commands_dict.get(char)
            max_row = func(max_row)
        for char in RL:
            func = commands_dict.get(char) 
            max_column = func(max_column)
        unique_id = calculate_unique_id(max_row[0], max_column[0])
        id_list.append(unique_id)
    return check_missing(id_list)

def check_missing(nums : [int])-> int:
    nums = sorted(nums)
    for index, num in enumerate(nums):
        if nums[index+1] - nums[index] > 1:
            return nums[index] + 1

print(day_5_q1("day_5.txt"))
print(day_5_q2("day_5.txt"))