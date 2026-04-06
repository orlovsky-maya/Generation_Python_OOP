class MROHelper:
    @staticmethod
    def len(cl):
        return len(cl.mro())

    @staticmethod
    def class_by_index(cl, n=0):
        return cl.mro()[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.mro().index(parent)


# Sample Input 1:


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(MROHelper.len(D))

# Sample Output 1:
#
# 5
#
# Sample Input 2:


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(MROHelper.class_by_index(D, 2))
print(MROHelper.class_by_index(B))

# Sample Output 2:
#
# <class '__main__.C'>

# <class '__main__.B'>
#
#
# Sample Input 3:


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(MROHelper.index_by_class(D, A))

# Sample Output 3:
#
# 3

