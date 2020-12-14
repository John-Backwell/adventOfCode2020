direction_dict = {0:"N",90:"E",180:"S",270:"W"}

def load_file(input_file:str):
    with open(input_file) as data_file:
        return data_file.read().splitlines()

def get_key(val):
    for key, value in direction_dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def move_ship(current_direction,instruction, value, NS_pos, EW_pos):
    if instruction == "N":
        NS_pos += value
    elif instruction == "S":
        NS_pos -= value
    elif instruction == "E":
        EW_pos += value
    elif instruction == "W":
        EW_pos -= value
    elif instruction == "L":
        angle = get_key(current_direction)
        angle -= value
        current_direction = direction_dict[angle % 360]
    elif instruction == "R":
        angle = get_key(current_direction)
        angle += value
        current_direction = direction_dict[angle % 360]
    return (current_direction,NS_pos, EW_pos)

def parse_line(current_direction,line, NS_pos,EW_pos):
    instruction = line[0]
    value = int(line[1:])
    if instruction == "F":
        coords = move_ship(current_direction, current_direction, value,NS_pos,EW_pos)
    else:
        coords = move_ship(current_direction, instruction, value,NS_pos,EW_pos)
    return coords

def day_12_q1(input_file):
    instructions = load_file(input_file)
    current_direction = "E"
    NS_pos = 0
    EW_pos = 0
    for line in instructions:
        current_direction, NS_pos, EW_pos = parse_line(current_direction,line,NS_pos,EW_pos)
    return abs(NS_pos)+ abs(EW_pos)

def waypoint_move(instruction, value,wpx,wpy):
    if instruction == "N":
        wpy += value
    elif instruction == "S":
        wpy -= value
    elif instruction == "E":
        wpx += value
    elif instruction == "W":
        wpx -= value
    elif instruction == "L":
        new_coords = anticlockwise_rotation(wpx,wpy,value)
        wpx = new_coords[0]
        wpy = new_coords[1]
    elif instruction == "R":
        new_coords = clockwise_rotation(wpx,wpy,value)
        wpx = new_coords[0]
        wpy = new_coords[1]
    return wpx, wpy

def clockwise_rotation(wpx,wpy,angle):
    if angle %360 == 0:
        return wpx,wpy
    if angle %360 == 90:
        return wpy,-wpx
    if angle %360 == 180:
        return -wpx, -wpy
    if angle %360 == 270:
        return -wpy, wpx


def anticlockwise_rotation(wpx,wpy,angle):
    return clockwise_rotation(wpx, wpy, 360 - angle)

def parse_q2(line,wpx,wpy,ship_x,ship_y):
    instruction = line[0]
    value = int(line[1:])
    if instruction == "F":
        ship_x += wpx*value
        ship_y += wpy*value
    else:
        wpx, wpy = waypoint_move(instruction, value, wpx,wpy)
    return wpx,wpy,ship_x,ship_y

def day_12_q2(input_file):
    instructions = load_file(input_file)
    wpx = 10
    wpy = 1
    ship_x = 0
    ship_y = 0
    for line in instructions:
        wpx,wpy,ship_x,ship_y = parse_q2(line,wpx,wpy,ship_x,ship_y)
    return abs(ship_x) + abs(ship_y)

