class Ord:
    def __getattr__(self, item):
        position = ord(item)
        return position

obj = Ord()

print(obj.a)
print(obj.b)

obj = Ord()

print(obj.в)
print(obj.г)

