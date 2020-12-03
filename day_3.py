def load_file(input_file: str):
    with open(input_file) as data_file:
        data = data_file.read().splitlines()
    return data

def propagate_slope(slope : [str], scale_factor: int):
    ski_slope = [line * 100 for line in slope]
    return ski_slope

def day_1_q1(input_file : str, slope_right : int, slope_down: int):
    slope = load_file(input_file)
    ski_slope = propagate_slope(slope,100)
    total_trees = 0
    y = 0
    x = 0
    while x < len(ski_slope):
        if ski_slope[x][y] == "#":
            total_trees +=1
        x += slope_down   
        y += slope_right
    return total_trees

def day_2_q2(input_file:str):
    return (day_1_q1(input_file, 1, 1)*day_1_q1(input_file, 3, 1)*day_1_q1(input_file, 5, 1)
    *day_1_q1(input_file, 7, 1)*day_1_q1("day_3.txt", 1, 2))

print(day_2_q2("day_3.txt"))