from ctypes import Union

#Trying sets to understand that sets take only unique value and work with union and intersection
def trysets():
    example_set1 = set([1, 3.14, 'suchitra', 789, 'this is a simple text'])
    example_set2 = set([3.14, 789, 'suchi', 'suchi', 'suchi'])
    print(example_set1.union(example_set2))
    print(example_set1.intersection(example_set2))

trysets()