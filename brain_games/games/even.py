import random

MAX_NUMBER = 99
MIN_NUMBER = 1


def get_welcome_message():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
