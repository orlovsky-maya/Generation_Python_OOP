class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

print('start')

with SuppressAll():
    print('Python generation!')
    raise ValueError

print('end')

# Valid output
# start
# Python generation!
# end

print('start')

with SuppressAll():
    print('Python generation!')

print('end')

# Valid output
# start
# Python generation!
# end