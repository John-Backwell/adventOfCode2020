

def load_file(input_file: str)-> [str]:
    with open(input_file) as text_file:
        nums = [int(i) for i in text_file]
        return nums

def day_10_q1(input_file: str)->int:
    nums = load_file(input_file)
    nums.append(0)
    nums.sort()
    num_1_jump = 0
    num_3_jump = 0
    for x in range(len(nums)-1):
        if nums[x+1] - nums[x] == 3:
            num_3_jump += 1
        elif nums[x+1] - nums[x] == 1:
            num_1_jump += 1
    num_3_jump +=1
    return num_1_jump * num_3_jump

def day_10_q2(input_file: str):
    nums = load_file(input_file)
    nums.append(0)
    nums.append(max(nums)+3)
    nums.sort()
    permutations = [1]+[0]*nums[-1]
    for i in nums[1:]:
            permutations[i] = permutations[i-1] + permutations[i-2] + permutations[i-3]
    return permutations[-1]
        
