import re

def get_largest_operand(op1, op2):
    if len(op1) > len(op2):
        return op1
    return op2

def is_valid(re_rule, problem):
    return bool(re.fullmatch(re_rule, problem))

def is_valid_size(problems, MAX_SIZE=5):
    return len(problems) <= MAX_SIZE

def arithmetic_arranger(problems, show_answers=False):
    top_row = []
    bottom_row = []
    dash_row = []
    FOUR_SPACES = '    '
    answers = None
    ans_count = None

    # For validation
    rules = {
        'is_valid_operator': '[-+]',
        'is_valid_digit': '\d+',
        'is_valid_digit_size': '\d{1,4}'
    }

    if show_answers:
        answers = []
        ans_count = 0

    if not is_valid_size(problems):
        return "Error: Too many problems."

    for problem in problems:
        top_operand, operator, bottom_operand = problem.split()

        if not is_valid(rules['is_valid_digit'], top_operand) \
                or not is_valid(rules['is_valid_digit'], bottom_operand):
            return "Error: Numbers must only contain digits."
        elif not is_valid(rules['is_valid_digit_size'], top_operand) \
                or not is_valid(rules['is_valid_digit_size'], bottom_operand):
            return "Error: Numbers cannot be more than four digits."
        elif not is_valid(rules['is_valid_operator'], operator):
            return "Error: Operator must be '+' or '-'."

        largest_operand = get_largest_operand(top_operand, bottom_operand)
        dash_size = len(largest_operand) + 2  # Two accounts for whitespace and operator

        if show_answers:
            if operator == '-':
                answers.append(int(top_operand) - int(bottom_operand))
            else:
                answers.append(int(top_operand) + int(bottom_operand))
            answers[ans_count] = str(answers[ans_count]).rjust(dash_size)
            ans_count += 1

        top_row.append(top_operand.rjust(dash_size))
        bottom_row.append(operator + bottom_operand.rjust(dash_size - 1))  # account for whitespace
        dash_row.append('-' * dash_size)

    # Add four spaces to each string and create new formatted string
    top_result = FOUR_SPACES.join(top_row)
    bottom_result = FOUR_SPACES.join(bottom_row)
    dash_result = FOUR_SPACES.join(dash_row)

    if show_answers:
        answers_result = FOUR_SPACES.join(answers)
        return '\n'.join([top_result, bottom_result, dash_result, answers_result])

    return '\n'.join([top_result, bottom_result, dash_result])