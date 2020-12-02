
def day_1_question_1(input_file, sum):
    with open(input_file) as text_file:
        nums = [int(i) for i in text_file]
        dict_nums = {}
        for x in range(len(nums)):
            dict_nums.setdefault(x, nums[x])      
    if len(dict_nums) == 0 or len(dict_nums) == 1:
        return False
    for x in range (len(dict_nums)):
        if (sum - dict_nums[x]) in dict_nums.values():

            return dict_nums[x] * (sum-dict_nums[x])



def day_1_question_2(input_file, sum):
    with open(input_file) as text_file:
        nums = [int(i) for i in text_file]
        dict_nums = {}
        for x in range(len(nums)):
            dict_nums.setdefault(x, nums[x])      
    if len(dict_nums) == 0 or len(dict_nums) == 1 or len(dict_nums) == 2:
        return False
    for x in range (len(dict_nums)):
        for y in range(1,len(dict_nums)):
            if sum - dict_nums[x] - dict_nums[y] in dict_nums.values():
                return dict_nums[x] * dict_nums[y] * (sum - dict_nums[x] - dict_nums[y])

if __name__ == "__main__":
    print(day_1_question_1("day_1_q1.txt", 2020))
    print(day_1_question_2("day_1_q1.txt", 2020))