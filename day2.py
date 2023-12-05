import re

def day2data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read().strip().split("\n")
        input_list = list(map(str, input_list))
        return input_list

day2puzzle = day2data("day2input")

def firststar(puzzle_input: list) -> int:
    class impossible_line(Exception): pass
    max_score = 5050 
    RGB = [re.compile(r"\d+\sred"), re.compile(r"\d+\sgreen"), re.compile(r"\d+\sblue")]
    max_RGB = [12, 13, 14]
    for line in puzzle_input:
        game_id = line[line.find('Game ')+5 : line.find(':')]
        sets_reveal = list((line[line.find(': ')+2:]).split(';'))
        try:
            for set in sets_reveal:
                for i,j in zip(RGB, max_RGB):
                    colour_result = re.search(i, set)
                    if not colour_result == None:
                        colour_result = colour_result.group()
                        colour_value = colour_result[:colour_result.find(' ')]
                        if int(colour_value) > j:
                            max_score -= int(game_id)
                            raise impossible_line
        except impossible_line:
            pass                  
    return max_score

firststar(day2puzzle)