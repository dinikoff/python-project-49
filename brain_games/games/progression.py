import random
import re

MAX_LENGTH = 10
MAX_NUMBER = 99
MIN_NUMBER = 1
MAX_STEP = 3
MIN_STEP = 1


def get_welcome_message():
    return 'What number is missing in the progression?'


def get_game_data():
    first = random.randint(MIN_NUMBER, MAX_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    prog = list(range(first, first + (MAX_LENGTH * step), step))
    hidden_position = random.randint(0, MAX_LENGTH - 1)
    answer = prog[hidden_position]
    prog[hidden_position] = '..'
    question = re.sub(r'[\[\],\']', '', str(prog))
    return question, str(answer)
