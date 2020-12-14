import copy

def load_file(input_file:str)-> [str]:
    with open(input_file) as data_file:
        data = data_file.readlines()
        copy = []
        for line in data:
            line = line.rstrip("\n")
            line = list(line)
            copy.append(line)
    return copy

def count_occupied(seating_arrangement):
    total_seats_occupied = 0
    for row in seating_arrangement:
        for seat in row:
            if seat == "#":
                total_seats_occupied +=1
    return total_seats_occupied

def swap_all_seats(seating_arrangement):
    seating_arrangement_copy = copy.deepcopy(seating_arrangement)
    for y in range(len(seating_arrangement)):
        for x in range(len(seating_arrangement[y])):
            seat_status = seating_arrangement[y][x]
            total_occupied = checK_num_adjacent_seats(x, y, seating_arrangement,"#")
            seating_arrangement_copy[y][x] = change_seat_status(seat_status,total_occupied)
    return seating_arrangement_copy

def test(input_file):
    seating_arrangement = load_file(input_file)
    test = swap_all_seats(seating_arrangement)
    print(test)

def day_11_q1(input_file):
    seating_arrangement = load_file(input_file)
    seats_changing = True
    while seats_changing:
        old_seating_arrangement = copy.deepcopy(seating_arrangement)
        seating_arrangement = swap_all_seats(seating_arrangement)
        seats_changing = old_seating_arrangement != seating_arrangement
    return count_occupied(seating_arrangement)

def checK_num_adjacent_seats(seat_index_x, seat_index_y, seating_arrangement, target_char)-> int:
    total_occupied = 0
    def check_seat(offset_x, offset_y):
        try:
            nonlocal total_occupied
            if seating_arrangement[seat_index_y - offset_y][seat_index_x - offset_x] == target_char:
                total_occupied +=1
        except IndexError:
            pass
    check_seat(1,-1)#top left
    check_seat(0,-1)#above
    check_seat(-1,-1)#top right
    check_seat(1,0)#left
    check_seat(-1,0)#right
    check_seat(1,1)#bottom left
    check_seat(0,1)#below
    check_seat(-1,1)#bottom right
    return total_occupied

def change_seat_status(seat_status, total_occupied):
    if seat_status == "L" and total_occupied == 0:
        seat_status = "#"
    if seat_status == "#" and total_occupied >= 4:
        seat_status = "L"
    return seat_status

