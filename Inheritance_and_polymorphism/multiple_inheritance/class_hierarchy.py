class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(A):
    pass

class E(B, D):
    pass




# Sample Input 1:

print(issubclass(E, B))
print(issubclass(E, C))
print(issubclass(E, D))

# Sample Output 1:
#
# True
# False
# True

# Sample Input 2:

print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(D, A))

# Sample Output 2:
#
# True
# True
# True

