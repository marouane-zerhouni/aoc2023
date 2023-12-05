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
        digits_in_line = [char for char in line if char.isnumeric()]
        digits_list.append(''.join(digits_in_line[0] + digits_in_line[-1]))
    digits_list = [int(i) for i in digits_list]
    return sum(digits_list)

firststar(day1puzzle)

def secondstar(calibration_doc: list) -> int:
    digit_list = []
    corrections = {('one', 'o1e'), ('two', 't2o'), ('three', 't3e'), ('four', 'f4r'), ('five', 'f5e'), ('six', 's6x'), ('seven', 's7n'), ('eight', 'e8t'), ('nine', 'n9e')}
    for line in calibration_doc:
            for written_no, garbage_attempt in corrections:
                line = line.replace(written_no, garbage_attempt)
            digits_in_line = [char for char in line if char.isnumeric()]
            digit_list.append(''.join(digits_in_line[0] + digits_in_line[-1]))
    digit_list = [int(i) for i in digit_list]
    return sum(digit_list)

            
print(secondstar(day1puzzle))