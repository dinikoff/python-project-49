import random

MAX_NUMBER = 99
MIN_NUMBER = 1
OPERATION_NUMBER = 3


def get_welcome_message():
    return 'What is the result of the expression?'


def get_game_data():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = ('+', '-', '*')[random.randint(0, OPERATION_NUMBER - 1)]
    question = f'{first_number} {operation} {second_number}'
    if operation == '+':
        answer = first_number + second_number
    elif operation == '-':
        answer = first_number - second_number
    else:
        answer = first_number * second_number
    return question, str(answer)
