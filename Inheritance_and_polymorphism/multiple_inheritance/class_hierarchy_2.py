class H:
    pass

class D(H):
    pass

class E(H):
    pass

class F(H):
    pass

class G(H):
    pass

class B(D, E):
    pass

class C(F, G):
    pass

class A(B, C):
    pass


 # Sample Input 1:

print(issubclass(D, H))
print(issubclass(E, H))
print(issubclass(F, H))
print(issubclass(G, H))

# Sample Output 1:
#
# True
# True
# True
# True
#
# Sample Input 2:

print(issubclass(B, D))
print(issubclass(B, E))
print(issubclass(B, F))
print(issubclass(B, G))

# Sample Output 2:
#
# True
# True
# False
# False
#
# Sample Input 3:

print(issubclass(C, D))
print(issubclass(C, E))
print(issubclass(C, F))
print(issubclass(C, G))
#
# Sample Output 3:
#
# False
# False
# True
# True
#
