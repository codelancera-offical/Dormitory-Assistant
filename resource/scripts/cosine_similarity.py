#code to identify soundprint using cosine similarity#
import numpy as np

def sumofsquare(a):
    sum = 0.0
    for x in a:
        sum += x ** 2  
    return sum ** 0.5  

def unit_vector(a):
    norm = sumofsquare(a)  
    if norm == 0:
        return a  
    return [x / norm for x in a]  

def cosine_similarity(a, b):
    a_unit = unit_vector(a)
    b_unit = unit_vector(b)
    
    t = sum(x * y for x, y in zip(a_unit, b_unit))
    
    return abs(t)  # make sure the result is positive

if __name__ == "__main__":
    vec1 = np.random.rand(128).tolist()  # generate two random vector
    vec2 = np.random.rand(128).tolist()

    similarity = cosine_similarity(vec1, vec2)
    print("Cosine Similarity:", similarity)