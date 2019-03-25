from combination import combination_finder
import numpy as np

def combination_finder_test():
    a1, a2 = combination_finder(np.array([1]), 1)
    assert a1 == set([1])
    assert a2 == set()
    
    a1, a2 = combination_finder(np.array([1,2]), 3)
    assert a1 == set([1,2])
    assert a2 == set()
    
    a1, a2 = combination_finder(np.array([1,2,4]), 5)
    assert a1 == set([1,4])
    assert a2 == set([2])
    
    a1, a2 = combination_finder(np.array([1,2,3]), 3)
    assert a1 == set()
    assert a2 == set()
    
    a1, a2 = combination_finder(np.array([1,1,1]), 3)
    assert a1 == set([1])
    assert a2 == set()

    a1, a2 = combination_finder(np.array([1,1,2,4]), 8)
    assert a1 == set([1,2,4])
    assert a2 == set()
    
    a1, a2 = combination_finder(np.array([2,2,4,3]), 8)
    assert a1 == set([2,4])
    assert a2 == set([3])
    
    a1, a2 = combination_finder(np.array([1,1,2]), 3)
    assert a1 == set([2])
    assert a2 == set()

    print("All Combination Finder Tests Passed")

if __name__ == "__main__":
    combination_finder_test()

