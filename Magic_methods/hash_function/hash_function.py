def hash_function(obj):
    obj_str = str(obj)
    temp1 = 0
    for i in range(len(obj_str)//2):
        temp1 += ord(obj_str[i]) * ord(obj_str[::-1][i])
    if len(obj_str)%2 != 0:
        temp1 += ord(obj_str[len(obj_str)//2])

    temp2 = 0
    for index, character in enumerate(obj_str, start=1):
        if index % 2 != 0:
            temp2 += ord(character) * index
        else:
            temp2 -= ord(character) * index
    return (temp1 * temp2) % 123456791

print(hash_function(12345))
print(hash_function("python"))
