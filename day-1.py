import re

def get_input():
    with open('day-1.txt') as f:
        return f.read().splitlines()

def fetch_numbers(s):
    return re.findall(r'\d', s)

def fetch_spelled_out_numbers(s):
    # fetch spelled out numbers and numbers both
    return re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))', s)

def part_1():
    res = 0
    data = get_input()
    for line in data:
        nums = fetch_numbers(line)
        # add first and last number
        two_digit = nums[0] + nums[-1]
        res += int(two_digit)
    return res

def part_2():
    str_num = {
        'zero': "0",
        'one': "1",
        'two': "2",
        'three': "3",
        'four': "4",
        'five': "5",
        'six': "6",
        'seven': "7",
        'eight': "8",
        'nine': "9"
    }
    data = get_input()
    res = 0
    for line in data:
        nums = fetch_spelled_out_numbers(line)
        if nums[0] in str_num:
            nums[0] = str_num[nums[0]]
        if nums[-1] in str_num:
            nums[-1] = str_num[nums[-1]]
        two_digit = nums[0] + nums[-1]
        print(f'{line} -> {two_digit}')
        res += int(two_digit)
    return res

print(part_2())