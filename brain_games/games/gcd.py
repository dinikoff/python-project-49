import random

MAX_NUMBER = 99
MIN_NUMBER = 1


def get_welcome_message():
    return 'Find the greatest common divisor of given numbers.'


def get_game_data():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = get_gcd(first_number, second_number)
    question = f'{first_number} {second_number}'
    return question, str(answer)


def get_gcd(first_number, second_number):
    remain = first_number % second_number
    if remain == 0:
        return second_number
    return get_gcd(second_number, remain)
