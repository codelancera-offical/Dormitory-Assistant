"""
Input two np.ndarray with same size, and compute the cosine similarity and return it.

You should inplement it in a function, and test it with following scripts 
"""


import numpy as np

def cosine_similarity(a, b):
    # inplement your code here

    return cosine_similarity


def test_cosine_similarity():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([1, 2, 3])
    arr3 = np.array([4, 5, 6])
    
    # Test case 1: identical arrays
    assert np.isclose(cosine_similarity(arr1, arr2), 1.0), "Test case 1 failed"

    # Test case 2: orthogonal arrays
    orthogonal_arr1 = np.array([1, 0])
    orthogonal_arr2 = np.array([0, 1])
    assert np.isclose(cosine_similarity(orthogonal_arr1, orthogonal_arr2), 0.0), "Test case 2 failed"

    # Test case 3: different arrays
    result = cosine_similarity(arr1, arr3)
    expected = np.dot(arr1, arr3) / (np.linalg.norm(arr1) * np.linalg.norm(arr3))
    assert np.isclose(result, expected), "Test case 3 failed"

if __name__ == "__main__":
    test_cosine_similarity()
    print("All tests passed!")