import random


def get_welcome_message():
    return 'What is the result of the expression?'


def get_game_data():
    first_number = random.randint(1, 99)
    second_number = random.randint(1, 99)
    operation = ('+', '-', '*')[random.randint(0, 2)]
    question = f'{first_number} {operation} {second_number}'
    if operation == '+':
        answer = first_number + second_number
    elif operation == '-':
        answer = first_number - second_number
    else:
        answer = first_number * second_number
    return question, str(answer)
