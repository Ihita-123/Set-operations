A={1,3,5,7,9,11,13}
B={1,2,3,4,5,6,7,8}

print(A.union(B))
print(A|B)

print(A.intersection(B))
print(A&B)

print(A.difference(B))
print(B.difference(A))
print(A-B)
print(B-A)

print(A.symmetric_difference(B))
print(A^B)

D={"apple","grape","blueberry","melon","strawberry"}
F={"watermelon","grape","blackberry","apple","lemon"}

print(D.union(F))
print(D.difference(F))
print(D.intersection(F))
print(F.symmetric_difference(D))

list=[2,4,6,8,3,9,1]

print(type(list))
p=set(list)
print(type(p))

J={3,7,9,4,6,0}

print(J)
J.add(8)
print(J)
J.remove(0)
print(J)
J.discard(6)
print(J)
J.discard(0)
J.clear()
print(J)

A={1,3,5,7,9,11,13}
B={1,2,3,4,5,6,7,8}
C={7,9,11}
sub_set=A>=C
print(sub_set)
print(B<=C)