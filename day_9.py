def load_file(input_file: str)-> [str]:
    with open(input_file) as text_file:
        nums = [int(i) for i in text_file]
        return nums

def day_9_q1(input_file: str) -> int:
    nums = load_file(input_file)
    for x in range(25,len(nums)):
        if not (check_sum(nums[x],nums[x-25:x])):
            return nums[x]

def check_sum(target: int, num_array: [int])-> bool:
    for x in range (len(num_array)-1):
        for y in range(1, len(num_array)):
            if num_array[x] + num_array[y] == target:
                return True
    return False


def contiguous_set(target: int, num_array: [int]):
    for i in range(len(num_array)):
        current_sum = num_array[i]
        j = i+1
        while j <= len(num_array):
            if current_sum == target:
                return num_array[i:j]
            if current_sum > target or j == len(num_array):
                break
            current_sum = current_sum + num_array[j]
            j +=1
    return 0

def day_9_q2(input_file: str) -> int:
    nums = load_file(input_file)
    target = day_9_q1(input_file)
    contiguous_nums = contiguous_set(target, nums)
    return max(contiguous_nums) + min(contiguous_nums)

print(day_9_q2("day_9.txt"))