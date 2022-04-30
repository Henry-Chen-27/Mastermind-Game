# Mastermind game
import random

# TODO: Generate Solution
def generate_solution(color_list, solution_len = 4):
    """
    Given the solution's length and a list of colours, generate
    a random set to be used as the solution
    """
    solution = []
    for i in range(solution_len):
        solution.append(random.choice(color_list))
    return solution

# TODO: Implement checking methods
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
    user_input_map = {}
    solution_map = {}
    for i in range(len(solution)):
        if user_input[i] == solution[i]:
            result["hit"] += 1
        else:
            _increment_item(user_input_map, user_input[i])
            _increment_item(solution_map, solution[i])
    for item in user_input_map:
        if item in solution_map:
            result["in"] += min(user_input_map[item], solution_map[item])
    result["miss"] = len(solution) - result["hit"] - result["in"]
    return result

def _increment_item(dict, item):
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1

# TODO: Implement user solution input


# TODO: OPTIONAL, Implement settings
# TODO: Play game
