from combination import combination_finder, merge_lst, subset_sum
import numpy as np

def merge_lst_test():
    a = set(merge_lst(np.array([1,1,1,1])))
    assert a == set([4])
    print("Test 1 Passed")

    a = set(merge_lst(np.array([1,1,2])))
    assert a == set([4])
    print("Test 2 Passed")
    
    a = set(merge_lst(np.array([1,1,1,2])))
    assert a == set([3,2])
    print("Test 3 Passed")

    a = set(merge_lst(np.array([1,2,3,4])))
    assert a == set([1,2,3,4])
    print("Test 4 Passed")

    a = set(merge_lst(np.array([1,1,1,1,2,2,4])))
    assert a == set([12])
    print("Test 5 Passed")
    
    a = set(merge_lst(np.array([2,4,6])))
    assert a == set([2,4,6])
    print("Test 6 Passed")
    
    print("All Merge List Tests Passed")

def subset_sum_test():
    combination_lst = []
    a1, a2 = subset_sum()

def combination_finder_test():
    a1, a2 = combination_finder(np.array([1,2]), 3)
    assert a1 == set([1,2])
    assert a2 == set()
    print("Test 1 Passed")
    
    a1, a2 = combination_finder(np.array([1,1,1]), 3)
    assert a1 == set([1])
    assert a2 == set()
    print("Test 2 Passed")

    a1, a2 = combination_finder(np.array([1,1,2]), 3)
    assert a1 == set([2])
    assert a2 == set()
    print("Test 3 Passed")

    a1, a2 = combination_finder(np.array([2,2,3]), 4)
    assert a1 == set([2])
    assert a2 == set([3])
    print("Test 4 Passed")

    print("All Combination Finder Tests Passed")

if __name__ == "__main__":
    merge_lst_test()
