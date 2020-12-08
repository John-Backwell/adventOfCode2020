def load_file(input_file:str):
    with open(input_file) as data_file:
        data = data_file.read()
    return data

def day_6_q1(input_file:str):
    data = load_file(input_file)
    groups = data.split("\n\n")
    total = 0
    for group in groups:
        answered = set()
        lines = group.split("\n")
        for line in lines:
            for char in line:
                answered.update(char)       
        total += len(answered)
    return total

def day_6_q2(input_file:str):
    data = load_file(input_file)
    groups = data.split("\n\n")
    total = 0
    for group in groups:
        answer_sets = []
        lines = group.split("\n")
        for line in lines:
            answer = set()
            for char in line:
                answer.update(char)
            answer_sets.append(answer)
        intersection_answers = answer_sets[0].intersection(*answer_sets)
        total += len(intersection_answers)
    return total
