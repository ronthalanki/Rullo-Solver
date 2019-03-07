import numpy as np

def input(puzzle_name):
    file = open("test-cases/" + puzzle_name + ".txt", "r")
    size = int(file.readline())
    row_targets = np.array(get_array(file.readline()))
    col_targets = np.array(get_array(file.readline()))
    nums = []
    for _ in range(size):
        nums.append(get_array(file.readline()))
    nums = np.array(nums)
    return size, row_targets, col_targets, nums

def get_array(str_nums):
    return [int(i) for i in str_nums.split(',')]

def combination_finder(lst, target):
    all_nums_lst = lst.copy()
    combination_lst = []
    subset_sum(lst, target, combination_lst)
    
    nums_set = set() 
    for lst in combination_lst:
        nums_set.update(lst)    

    not_used_set = set()
    for num in all_nums_lst:
        if not num in nums_set:      
            not_used_set.add(num)
    
    guaranteed_set = set()
    exclusions_set = set()
    for num in all_nums_lst:
        count = 0
        for lst in combination_lst:
            if num in lst:
                count += 1
        if count == len(combination_lst):
            if num in guaranteed_set: 
                exclusions_set.add(num)
                guaranteed_set.remove(num)
            elif not num in exclusions_set:
                guaranteed_set.add(num)

    return not_used_set, guaranteed_set

def subset_sum(lst, target, combination_lst, partial_lst=[]):
    s = sum(partial_lst)

    if s == target:
        combination_lst.append(partial_lst)
    
    if s > target:
        return 
    
    for i in range(len(lst)):
        n = lst[i]
        remaining = lst[i+1:]
        subset_sum(remaining, target, combination_lst, partial_lst + [n])

def solver(size, row_targets, col_targets, nums):
    solution = np.array([[1 for _ in range(size)] for _ in range(size)])
    guaranteed = np.array([[0 for _ in range(size)] for _ in range(size)])

    for _ in range(100):
        print("Iteration --------")
        print(nums)
        print("\n")
        print(solution)
        print("\n")
        print(guaranteed)
        print("\n")
        print("\n")
        
        curr_row_sums = np.sum(np.multiply(nums, solution), axis=1)
        for r in range(size):
            if curr_row_sums[r] != row_targets[r]:
                curr_row = list(nums[r,:])
                del_indices_lst = []
                guaranteed_sum = 0
                for i in range(size):
                    if solution[r,i] == 0: 
                        del_indices_lst.append(i)
                    elif guaranteed[r,i] == 1:
                        guaranteed_sum += nums[r,i]
                        del_indices_lst.append(i)
                
                for i in reversed(range(len(del_indices_lst))):
                    del curr_row[del_indices_lst[i]]

                not_used_set, guaranteed_set = combination_finder(curr_row, row_targets[r] - guaranteed_sum)
                for i in range(size):
                    if nums[r,i] in guaranteed_set:
                        guaranteed[r,i] = 1
                
                for i in range(size):
                    if nums[r,i] in not_used_set and guaranteed[r,i] == 0:
                        solution[r,i] = 0

        curr_col_sums = np.sum(np.multiply(nums, solution), axis=0)
        for c in range(size):
            if curr_col_sums[c] != col_targets[c]:
                curr_col = list(nums[:,c])
                del_indices_lst = []
                guaranteed_sum = 0
                for i in range(size):
                    if solution[i,c] == 0:
                        del_indices_lst.append(i)
                    elif guaranteed[i,c] == 1:
                        guaranteed_sum += nums[i,c]
                        del_indices_lst.append(i)

                for i in reversed(range(len(del_indices_lst))):
                    del curr_col[del_indices_lst[i]]
                
                not_used_set, guaranteed_set = combination_finder(curr_col, col_targets[c] - guaranteed_sum)
                for i in range(size):
                    if nums[i,c] in guaranteed_set:
                        guaranteed[i,c] = 1

                for i in range(size):
                    if nums[i,c] in not_used_set and guaranteed[i,c] == 0:
                        solution[i,c] = 0
    return solution

if __name__ == "__main__":
    size, row_targets, col_targets, nums = input("3-large-easy")
    print(size)
    print(row_targets)
    print(col_targets)
    print(nums)
    
    solved = solver(size, row_targets, col_targets, nums)
    print(solved)
