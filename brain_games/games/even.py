from brain_games.generator import get_numbers


def get_welcome_message():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    question = get_numbers()[0]
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
