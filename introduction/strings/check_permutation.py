from collections import Counter


'''
A counter is a container that keeps track of HOW MANY TIMES equivalent values are added.
It can be used to implement the same algorithm for which bag or multiset data structures are 
commonly used.
'''
def check(a,b):
    if len(a) != len(b):
        return False
    print("counter(a): "+str(Counter(a)))
    print("counter(b): "+str(Counter(b)))
    
    return Counter(a) == Counter(b)

bool = check("abcb", "abca")
print(str(bool))