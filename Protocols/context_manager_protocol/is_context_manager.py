def is_context_manager(obj):
    try:
        with obj:
            return True
    except AttributeError:
        return False


print(is_context_manager(open('output.txt', mode='w')))
# Valid output
# True

from tempfile import TemporaryFile

with TemporaryFile(mode='r+') as file:
    print(is_context_manager(file))

# Valid output
# True

from threading import Lock

print(is_context_manager(Lock()))

# Valid output
# True


print(is_context_manager(1992))
print(is_context_manager('beegeek'))
print(is_context_manager([1, 2, 3]))
print(is_context_manager({'one': 1, 'two': 2}))
print(is_context_manager(None))
#
# Valid output
# False
# False
# False
# False
# False
