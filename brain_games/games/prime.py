import math
import random

MAX_NUMBER = 99
MIN_NUMBER = 1


def get_welcome_message():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game_data():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(question) else 'no'
    return question, str(answer)


def is_prime(num):
    if num <= 1:
        return False
    return iter_prime(num, math.ceil(num / 2))


def iter_prime(num, div):
    if div == 1:
        return True
    if num % div == 0:
        return False
    return True and iter_prime(num, div - 1)
