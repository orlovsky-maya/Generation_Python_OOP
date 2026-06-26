def add_attr_to_class(**attrs):
    def decorator(cls):
        attr = {**attrs}
        for key, value in attr.items():
            setattr(cls, key, value)
        return cls

    return decorator

# Входные данные1
@add_attr_to_class(first_attr=1, second_attr=2)
class MyClass:
    pass

print(MyClass.first_attr)
print(MyClass.second_attr)


# Выходные данные1
# 1
# 2