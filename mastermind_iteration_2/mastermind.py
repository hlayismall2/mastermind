import random
import code

turns = 0


def generate_four_digits_code():
    '''This function generate 4-digit code and update it to a global variable'''
    global code
    code = [0, 0, 0, 0]
    for i in range(4):
        value = random.randint(1, 8)  # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    # print(code)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return code


def get_user_input(turns):
    '''This function get a 4-digit code to a user in string type'''
    correct = False
    while not correct and turns < 12:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
        else:
            return checking_the_result(answer)
    return


def checking_the_result(answer):
    '''This function checks the user input and validate it and returns the outcome to win_or_not()'''
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    return win_or_not(correct_digits_and_position, correct_digits_only)


def show_result(correct_digits_and_position, correct_digits_only):
    '''This function print outs the outcome of the user input'''
    print('Number of correct digits in correct place:     ' +
          str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    return


def win_or_not(correct_digits_and_position, correct_digits_only):
    '''This function checks if the user guessed the code right or not'''
    global turns
    if correct_digits_and_position == 4:
        show_result(correct_digits_and_position, correct_digits_only)
        print('Congratulations! You are a codebreaker!')
    else:
        turns += 1
        show_result(correct_digits_and_position, correct_digits_only)
        print('Turns left: '+str(12 - turns))
        get_user_input(turns)
    return


# TODO: Decompose into functions
def run_game():
    '''This function runs the game'''
    generate_four_digits_code()
    get_user_input(turns)
    print('The code was: '+str(code))


if __name__ == "__main__":
    run_game()
