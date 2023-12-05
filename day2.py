import re

def day2data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read().strip().split("\n")
        input_list = list(map(str, input_list))
        return input_list

day2puzzle = day2data("day2input")

def firststar(puzzle_input: list) -> int:

    class impossible_line(Exception): pass
    games_results = {}
    max_score = 5050
    max_red = 12
    max_green = 13
    max_blue = 14
    red = re.compile(r"\d+\sred", re.IGNORECASE)
    green = re.compile(r"\d+\sgreen", re.IGNORECASE)
    blue = re.compile(r"\d+\sblue", re.IGNORECASE)

    for line in puzzle_input:
        game_id = line[line.find('Game ')+5 : line.find(':')]
        sets_reveal = line[line.find(': ')+2:]
        sets_reveal = list(sets_reveal.split(';'))
        try:
            for set in sets_reveal:
                for i,j in zip([red, green, blue], [max_red, max_green, max_blue]):
                    colour_result = re.search(i, set)
                    if not colour_result == None:
                        colour_result = colour_result.group()
                        colour_value = colour_result[:colour_result.find(' ')]
                        if int(colour_value) > j:
                            max_score -= int(game_id)
                            print('Max score is ' + str(max_score))
                            print('Game id is ' + game_id)
                            print('Colour value is ' + colour_value)
                            print('Colour max is ' + str(j))
                            raise impossible_line
        except impossible_line:
            pass                  
    return max_score

firststar(day2puzzle)