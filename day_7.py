def load_file(input_file:str)-> [str]:
    with open(input_file) as data_file:
        lines = data_file.read().splitlines()
    return lines

def gen_dict(data: [str])-> dict:
    bag_dict = {}
    for line in data:
        line = line.replace(".", "").replace(",","").replace("contain", "")
        words = line.split()
        key = " ".join(words[:2])
        sliced_words = words[3:]
        values = []
        for index, word in enumerate(sliced_words):
            if word == "bags" or word == "bag":
                values.append(sliced_words[index-2]+ " " + sliced_words[index - 1])
        temp_dict = {key : values}
        bag_dict.update(temp_dict)
    return bag_dict

def check_bags(bag_contents):
    check_dict = {}
    for bag, contents in bag_contents.items():
        for content in contents:
            if content != "no other":
                if content not in check_dict:
                    check_dict[content] = set({})
                check_dict[content].add(bag)
    searched_colours = {"shiny gold"}
    halt = True
    while halt:
        halt = False
        l = len(searched_colours)
        for colour in searched_colours:
            if colour in check_dict:
                searched_colours = searched_colours | check_dict[colour]
        if len(searched_colours) > l:
            halt = True
    return len(searched_colours) - 1
    
def day_7_q1(input_file: str)-> int:
    lines = load_file(input_file)
    bag_dict = gen_dict(lines)
    total_correct = check_bags(bag_dict)
    return total_correct

def gen_dict_nums(data: [str])-> dict:
    bag_dict = {}
    for line in data:
        line = line.replace(".", "").replace(",","").replace("contain", "")
        words = line.split()
        key = " ".join(words[:2])
        sliced_words = words[3:]
        values = []
        for index, word in enumerate(sliced_words):
            if word == "bags" or word == "bag":
                values.append(sliced_words [index-3] + " " + sliced_words[index-2]+ " " + sliced_words[index - 1])
        temp_dict = {key : values}
        bag_dict.update(temp_dict)
    return bag_dict

def calculate_num_bags(bag_nums_dict: {}):
    for bags in bag_nums_dict.keys():
        pass

def day_7_q2(input_file: str):
    lines = load_file(input_file)
    bag_nums_dict = gen_dict_nums(lines)
    check_dict = {}
    for bag, contents in bag_nums_dict.items():
        for content in contents:
            if content != "bags no other":
                num = content[0]
                colour = content[2:]
                if bag not in check_dict:
                    check_dict[bag] = set({})
                check_dict[bag].add((colour, num))
            else:
                check_dict[bag] = set({})
    return sum_colours("shiny gold",check_dict)

def sum_colours(colour: str, check_dict: {}):
    total = 0
    for outer_colour, num in check_dict[colour]:
        total += int(num) * (1 + sum_colours(outer_colour,check_dict))
    return total

print(day_7_q2("day_7.txt"))
