import numpy as np

#Input: np.array, int
#Output: set, set
def combination_finder(lst, target):
    combined_lst = merge_lst(lst)
    
    combination_lst = []
    subset_sum(combined_lst, target, combination_lst)
    return combination_lst
    #return set([1,2]), set()

#Input: np.array
#Output: np.array
def merge_lst(lst):
    while len(lst) != len(set(lst)):
        lst = merge_lst_helper(lst)
    return lst

#Input: np.array
#Output: np.array
def merge_lst_helper(lst):
    unique_lst, counts = np.unique(lst, return_counts=True)
    count_dict = dict(zip(unique_lst, counts))
    merged_lst = np.array([num * count_dict[num] for num in count_dict])
    return merged_lst

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

