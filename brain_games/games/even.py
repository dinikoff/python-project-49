import random


def get_welcome_message():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    question = random.randint(1, 99)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
