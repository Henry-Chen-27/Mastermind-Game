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


# TODO: Implement user solution input


# TODO: OPTIONAL, Implement settings
# TODO: Play game
