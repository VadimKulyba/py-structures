"""wg forge task-B"""
#!/usr/bin/python2
import difflib
import math
import re
import sys

def compute_size_for_devide(line):
    """Round half size list for will devide and return zero, if < 1"""
    dicimal_value = len(line) / 2.0
    if dicimal_value < 1:
        return 0
    return int(math.ceil(dicimal_value))

def split_string_on_half(line, size):
    """Split line on half with condition size"""
    return line[:size], line[-size:]

def comparator(first_line, second_line, state=dict(coincidences=[])):
    """Function compatate parts of list or return exit code"""
    devide_number = None
    if first_line[0] == second_line[0]:
        state['coincidences'].append(True)
        devide_number = -1
    elif first_line[-1] == second_line[-1]:
        state['coincidences'].append(True)
        devide_number = 0

    if not state['coincidences']:
        if len(differ_indexer(differ_wrapper())) != 1:
            print(0)
            sys.exit(0)
        else:
            find_limits()
    else:
        del state['coincidences'][:]
        devide_strings_on_parts(first_line, second_line, devide_number)

def devide_strings_on_parts(first_line, second_line, devide_number):
    """Function divide string on half or not divide and find limits repeat letters"""
    half_number = compute_size_for_devide(first_line[devide_number])
    if half_number == 0:
        find_limits()
    first_line = split_string_on_half(first_line[devide_number], half_number)
    second_line = split_string_on_half(second_line[devide_number], half_number)
    comparator(first_line, second_line)

def differ_wrapper():
    """differ wrapper for string"""
    differ = difflib.Differ()
    return list(differ.compare(STRING_WITH_MISTAKE, STRING_RIGHT))

def differ_indexer(result):
    """indexer differentions with string"""
    return [i for i, word in enumerate(result) if re.search('-', word)]

def find_limits():
    """find limits in repeat symbols and return indexes"""
    result = differ_wrapper()
    index = differ_indexer(result)[0]
    result[index] = result[index].replace('-', ' ')
    left = limit(result, index, -1, None)
    if left is None:
        left = index
    right = limit(result, index, 1, None)
    if right is None:
        right = index
    if left == right:
        print(1)
        print(str(index + 1))
        exit(0)
    else:
        result_list = range(left + 1, right + 2)
        print(len(result_list))
        print(' '.join(map(str, result_list)))
        exit(0)

def limit(line, index, offset, state):
    """Return last repeat letter index"""
    next_index = index + offset
    if next_index < 0 or (len(line) - 1) < next_index:
        return state

    if line[index] == line[next_index]:
        state = next_index
        state = limit(line, next_index, offset, state)

    return state

def main():
    """Launch function (input value and make first devide)"""
    half_len_mistake_sting = compute_size_for_devide(STRING_WITH_MISTAKE)

    mistake = split_string_on_half(STRING_WITH_MISTAKE, half_len_mistake_sting)
    right = split_string_on_half(STRING_RIGHT, half_len_mistake_sting)
    comparator(mistake, right)

if __name__ == "__main__":
    FIRST_STRING = raw_input()
    SECOND_STRING = raw_input()

    if len(FIRST_STRING) > len(SECOND_STRING):
        STRING_WITH_MISTAKE = FIRST_STRING
        STRING_RIGHT = SECOND_STRING
    else:
        STRING_WITH_MISTAKE = SECOND_STRING
        STRING_RIGHT = FIRST_STRING

    main()
