import re

def get_input():
    with open('day-2.txt') as f:
        return f.read().splitlines()
    
def get_color_and_count(s):
    color_cnt = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    pattern = r'(\d+) (red|green|blue)'
    # fetch groups and count them
    # group 1: count and group 2: color
    games = s.split('; ')

    # for each game, fetch the color and count separately
    for i,game in enumerate(games):
        for count, color in re.findall(pattern, game):
            # update dictionary with max count of each color
            color_cnt[color] = max(color_cnt[color], int(count))
    return color_cnt


def part_1():
    data = get_input()
    res = 0
    for game in data:
        color_cnt = get_color_and_count(game)

        # power = product of all values
        power = 1
        for color in color_cnt:
            power *= color_cnt[color]
        res += power
    print(res)

part_1()