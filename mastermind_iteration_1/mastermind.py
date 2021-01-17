import random


def run_game():
    """
    TODO: implement Mastermind code here
    """
    #STEP 1
    random_digits = [] 
    for _ in range(4):
        x = random.randint(1,8)
        while x in random_digits:
            x = random.randint(1,8)
        random_digits.append(x)
    
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    #STEP 2
    
    user_input = input("Input 4 digit code: ")
    code = ""
    turns = 12
   
    while turns > 0:
        
        count = 0
        count_wrongs = 0
        if not user_input.isnumeric() or len(user_input) != 4:
            print("Please enter exactly 4 digits.")
            user_input = input("Input 4 digit code: ")
            continue
        else:
            user_inpu = list(map(int,list(user_input)))
            for i in user_inpu:
                if i > 8 or i <= 0:
                    print("Out of range")
                    user_input = input("Input 4 digit code: ")
                    continue
    #STEP 3
            user_input = list(map(int,list(user_input)))
            
            
            if random_digits == user_input:
                print("Number of correct digits in correct place:     4")
                print("Number of correct digits not in correct place: 0")
                print("Congratulations! You are a codebreaker!")
                print("The code was: {}".format(code.join(list(map(str,random_digits)))))
                break
            else:
                for i in range(4):
                    if random_digits[i] == user_input[i]:
                        count += 1    
                    elif user_input[i] in random_digits:
                        count_wrongs += 1
                print("Number of correct digits in correct place:     {}".format(count))
                print("Number of correct digits not in correct place: {}".format(count_wrongs))
    #STEP 4
                turns -= 1
                print("Turns left: {}".format(turns))
                if turns == 0:
                    print("The code was: {}".format(code.join(list(map(str,random_digits)))))
                    break
                user_input = input("Input 4 digit code: ")
                continue
    return


if __name__ == "__main__":
    run_game()
