from collections import OrderedDict

def day1data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read().strip().split("\n")
        input_list = list(map(str, input_list))
        return input_list


day1puzzle = day1data("day1input")

def firststar(calibration_doc: list) -> int:
    digits_list = []
    for line in calibration_doc:
        digits_in_line = [char for char in line if char in '0123456789']
        digits_list.append(''.join(digits_in_line[0] + digits_in_line[len(digits_in_line) - 1]))
    digits_list = [int(i) for i in digits_list]
    return sum(digits_list)

firststar(day1puzzle)

def secondstar(calibration_doc: list) -> int:
    digit_list = []
    for line in calibration_doc:
        corrections = OrderedDict([('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')])
        for x,y in corrections.items():
            line = line.replace(x,y)
        digits_in_line = [char for char in line if char in '0123456789']
        digit_list.append(''.join(digits_in_line[0] + digits_in_line[len(digits_in_line) - 1]))
    print(digit_list)
    digit_list = [int(i) for i in digit_list]
    return sum(digit_list)

print(secondstar(day1puzzle))