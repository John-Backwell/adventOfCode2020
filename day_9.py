def load_file(input_file: str)-> [str]:
    with open(input_file) as data_file:
        return data_file.read().splitlines()

def day_9_q1(input_file: str) -> int:
    