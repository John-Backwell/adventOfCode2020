def load_file(input_file:str)-> [str]:
    with open(input_file) as data_file:
        lines = data_file.read().splitlines()
    return lines

def gen_dict(data: [str])-> dict:
    bag_dict = {}
    for line in data:
        line = line.replace(".", "").replace(",","")
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
    total_correct = 0
    for bag in bag_contents.keys():
        for bags in bag_contents[bag]:
            if bags == "shiny gold":
                total_correct +=1
            """ bag_path = []
            if(check_bag(bags, bag_path)):
                total_correct += 1
                break """
    return total_correct
 
def check_bag(bag, bag_path):
    for bags in bag:
        if bags in bag_path:
            return False
        if bags == "shiny gold":
            return True
        else:
            bag_path.append(bags)
            check_bag(bags,bag_path)
    
def day_7_q1(input_file: str)-> int:
    lines = load_file(input_file)
    bag_dict = gen_dict(lines)
    total_correct = check_bags(bag_dict)
    return total_correct

print(day_7_q1("day_7.txt"))

