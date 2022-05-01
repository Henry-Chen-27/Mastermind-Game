# Mastermind game
import random
from colorama import Fore, Style

def generate_solution(color_list, solution_len = 4):
    """
    Given the solution's length and a list of colours, generate
    a random set to be used as the solution
    """
    solution = []
    for i in range(solution_len):
        solution.append(random.choice(color_list))
    return solution

def check_solution(user_input, solution):
    """
    Compares the user input to the solution set and return the
    appropriate response

    "hit": number of correct guesses
    "in": number of guesses that are in solution, but wrong position
    "miss": number of guesses that are not in solution

    Precondition: len(user_input) == len(solution)
    """
    result = {"hit": 0, "in": 0, "miss": 0}
    # tracks char frequecy to check ins
    user_input_map = {}
    solution_map = {}
    # check number of hits
    for i in range(len(solution)):
        if user_input[i] == solution[i]:
            result["hit"] += 1
        else:
            _increment_item(user_input_map, user_input[i])
            _increment_item(solution_map, solution[i])
    # check number of ins
    for item in user_input_map:
        if item in solution_map:
            result["in"] += min(user_input_map[item], solution_map[item])
    # calculate number of misses
    result["miss"] = len(solution) - result["hit"] - result["in"]
    return result

def _increment_item(dict, item):
    """
    Increments the value of <item> in <dict> by 1
    """
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1

def input_answer(color_list, solution_len = 4):
    """
    Prompts the user to enter their guess for the solution

    Example input for solution length of 4:
    "a b c d"
    """
    print("Enter your guess: ")
    user_input = input().split(" ")
    while not _valid_input(color_list, solution_len, user_input):
        print("Invalid input, enter your guess again: ")
        user_input = input().split(" ")
    return user_input

def _valid_input(color_list, solution_len, solution):
    """
    Checks if the user input is valid
    """
    for i in solution:
        if i not in color_list:
            return False
    return len(solution) == solution_len

# TODO: OPTIONAL, Implement settings
def play_game(num_pegs):
    print("=====================")
    color_list = ['R', 'Y', 'G', 'B', 'C', 'P']
    solution = generate_solution(color_list, num_pegs)
    guess_count = 0
    history = []
    while True:
        user_input = input_answer(color_list, num_pegs)
        guess_count += 1
        result = check_solution(user_input, solution)
        _print_guess(user_input)
        if result["hit"] == num_pegs:
            print("That was the correct answer.")
            print(f"You took {guess_count} guesses.")
            break
        else:
            _print_result(result)

def _print_guess(guess):
    """
    Prints the series of colours represented by <guess>
    """
    colours = {"R": Fore.RED,
               "Y": Fore.YELLOW,
               "G": Fore.GREEN,
               "B": Fore.BLUE,
               "C": Fore.CYAN,
               "P": Fore.MAGENTA}
    result_str = ""
    for ch in guess:
        result_str += colours[ch] + ch + " "
    print(result_str + Style.RESET_ALL)

def _print_result(result):
    """
    Prints the results from the user's guess
    """
    print("hits: " + str(result['hit']) + ", ins: " + str(result["in"]) + \
          ", misses: " + str(result['miss']))

def print_intro():
    print("Possible colours are")
    _print_guess(['R', 'Y', 'G', 'B', 'C', 'P'])

if __name__ == '__main__':
    play_again = "yes"
    print_intro()
    print("Enter the number of pegs to be guessed: ")
    # verifies that the input is valid
    while True:
        num_pegs = input()
        if num_pegs.isdigit():
            break
        else:
            print("Please enter a positive integer: ")
    num_pegs = int(num_pegs)
    while play_again == "yes" or play_again == "YES":
        play_game(num_pegs)
        print("Type 'yes' to play again, anything else to exit game: ")
        play_again = input()
