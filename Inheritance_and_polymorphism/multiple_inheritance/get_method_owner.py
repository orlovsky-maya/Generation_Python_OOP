def get_method_owner(cls, method):
    mro_list = list(cls.mro())
    for cl in mro_list:
        if method in cl.__dict__:
            return cl
    return None


# Sample Input 1:


class A:
    def m(self):
        pass


class B(A):
    pass


print(get_method_owner(B, 'm'))
#
# Sample Output 1:
#
# <class '__main__.A'>
#

# Sample Input 2:


class A:
    def m(self):
        pass


class B(A):
    def m(self):
        pass


print(get_method_owner(B, 'm'))
#
# Sample Output 2:
#
# <class '__main__.B'>


# Sample Input 3:


class A:
    pass


class B(A):
    pass


print(get_method_owner(B, 'm'))

# Sample Output 3:
#
# None