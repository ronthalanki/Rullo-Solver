import numpy as np

#Input: np.array, int
#Output: set, set
def combination_finder(lst, target, verbose = False):
    combination_lst = []
    subset_sum(lst.copy(), target, combination_lst)
     
    unique, counts = np.unique(lst, return_counts = True)
    dict_lst_count = dict(zip(unique, counts))
    
    dict_total_count = dict(zip(unique, [0 for _ in range(len(unique))]))
    
    for lst in combination_lst:
        for item in lst:
            dict_total_count[item] = dict_total_count[item] + 1

    guaranteed_set = set()
    not_used_set = set()
    
    for num in dict_total_count:
        if dict_total_count[num] == dict_lst_count[num] * len(combination_lst):
            guaranteed_set.add(num)
        elif dict_total_count[num] == 0:
            not_used_set.add(num)

    if verbose:
        print(combination_lst)
        print(dict_lst_count)
        print(dict_total_count)
        print(guaranteed_set)
        print(not_used_set)
    return guaranteed_set, not_used_set 

#Input: np.array, int, ndarray, np.array
#Output: None, ndarray is modified
def subset_sum(lst, target, combination_lst, partial_lst=[]):
    s = np.sum(partial_lst)

    if s == target:
        combination_lst.append(partial_lst)
    
    if s > target:
        return 
    
    for i in range(len(lst)):
        n = lst[i]
        remaining = lst[i+1:]
        subset_sum(remaining, target, combination_lst, partial_lst + [n])

