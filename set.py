set1 = {1,2,3,4,5}
set2 = {"apple","banna","cherry"}
set3 = set([1,2,2,3,4]) # duplicate removed
print("set3:",set3)

# Adding & Removing

set1.add(6)
print("After add:",set1)
set1.remove(3)  # removes element ,error if not present
print("After remove:",set1)
set1.discard(10)  # no error if element not present

# set operations
a={1,2,3,4}
b={3,4,5,6}
print("Union:",a|b) #{1,2,3,4,5,6}
print("Intersection:",a & b) #{3,4}
print("Difference:",a-b) #{1,2}
print("Symmetric Diff:",a ^ b) # {1,2,5,6}