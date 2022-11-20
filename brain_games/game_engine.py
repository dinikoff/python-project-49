import prompt

NUM_OF_TRYING = 3


def game_engine(game):
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.get_welcome_message())
    count = 0
    while count < NUM_OF_TRYING:
        question, correct_answer = game.get_game_data()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
