import numpy as np
from combination import combination_finder 

def input(puzzle_name):
    file = open("test-cases/" + puzzle_name + ".txt", "r")
    row_size, col_size = get_array(file.readline())
    row_targets = np.array(get_array(file.readline()))
    col_targets = np.array(get_array(file.readline()))
    nums = []
    for _ in range(row_size):
        nums.append(get_array(file.readline()))
    nums = np.array(nums)
    return row_size, col_size, row_targets, col_targets, nums

def get_array(str_nums):
    return [int(i) for i in str_nums.split(',')]

def solver(row_size, col_size, row_targets, col_targets, nums, verbose = False):
    solution = np.array([[1 for _ in range(col_size)] for _ in range(row_size)])
    guaranteed = np.array([[0 for _ in range(col_size)] for _ in range(row_size)])
    return solver_helper(row_size, col_size, row_targets, col_targets, nums, solution, guaranteed, verbose)

def solver_helper(row_size, col_size, row_targets, col_targets, nums, solution, guaranteed, verbose):
    has_changed = True 

    while has_changed:
        has_changed = False
        if verbose:
            print("Iteration --------")
            print(nums)
            print("\n")
            print(solution)
            print("\n")
            print(guaranteed)
            print("\n")
            print("\n")

        curr_row_sums = np.sum(np.multiply(nums, solution), axis=1)
        for r in range(row_size):
            if curr_row_sums[r] != row_targets[r]:
                curr_row = nums[r,:] * (1 - guaranteed[r,:]) * solution[r,:]
                curr_guaranteed = nums[r,:] * guaranteed[r,:]

                guaranteed_set, not_used_set = combination_finder(curr_row[curr_row > 0], row_targets[r] - np.sum(curr_guaranteed))
                for i in range(col_size):
                    if nums[r,i] in guaranteed_set and solution[r,i] != 0:
                        guaranteed[r,i] = 1
                        has_changed = True
                
                for i in range(col_size):
                    if nums[r,i] in not_used_set and guaranteed[r,i] == 0:
                        solution[r,i] = 0
                        has_changed = True
            else:
                guaranteed[r,:] = solution[r,:]

        curr_col_sums = np.sum(np.multiply(nums, solution), axis=0)
        for c in range(col_size):
            if curr_col_sums[c] != col_targets[c]:
                curr_col = nums[:,c] * (1 - guaranteed[:,c]) * solution[:,c]
                curr_guaranteed = nums[:,c] * guaranteed[:,c]
                
                guaranteed_set, not_used_set = combination_finder(curr_col[curr_col > 0], col_targets[c] - np.sum(curr_guaranteed))
                for i in range(row_size):
                    if nums[i,c] in guaranteed_set and solution[i,c] != 0:
                        guaranteed[i,c] = 1
                        has_changed = True

                for i in range(row_size):
                    if nums[i,c] in not_used_set and guaranteed[i,c] == 0:
                        solution[i,c] = 0
                        has_changed = True
            else:
                guaranteed[:,c] = solution[:,c]
    
    if check_solution(row_targets, col_targets, solution, nums):
        return solution
    else:
        for r in range(row_size):
            for c in range(col_size):
                if solution[r,c] == 1 and guaranteed[r,c] != 1:
                    solution_copy = solution.copy()
                    guaranteed_copy = guaranteed.copy()
                    solution_copy[r,c] = 0
                    if check_valid(row_targets, col_targets, solution_copy, nums):
                        return solver_helper(row_size, col_size, row_targets, col_targets, nums, solution_copy, guaranteed_copy, verbose)

def check_valid(row_targets, col_targets, solution, nums):
    vals = nums * solution
    row = np.sum(vals, axis=1) - row_targets
    col = np.sum(vals, axis=0) - col_targets
    b1 = (len(row[row < 0]) == 0)
    b2 = (len(col[col < 0]) == 0)
    return b1 and b2

def check_solution(row_targets, col_targets, solution, nums):
    vals = nums * solution
    row_sums = np.sum(vals, axis=1)
    col_sums = np.sum(vals, axis=0)
    b1 = np.array_equal(row_sums, row_targets)
    b2 = np.array_equal(col_sums, col_targets)
    return b1 and b2

if __name__ == "__main__":
    row_size, col_size, row_targets, col_targets, nums = input("10-rectangle")
    solved = solver(row_size, col_size, row_targets, col_targets, nums)
    
    print("Finished Solving")
    print(row_targets)
    print(col_targets)
    print(nums)
    print(solved)
    print(check_solution(row_targets, col_targets, solved, nums))
