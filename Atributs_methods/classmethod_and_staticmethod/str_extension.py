class StrExtension:
    @staticmethod
    def remove_vowels(string):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
        string_list = list(string)
        result = list(filter(lambda l: l not in vowels, string_list))
        return ''.join(result)

    @staticmethod
    def leave_alpha(string):
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        string_list = list(string)
        result = list(filter(lambda l: l in alphabet, string_list))
        return ''.join(result)

    @staticmethod
    def replace_all(string, chars: str, char: str):
        string_list = list(string)
        result = list(map(lambda l: l.replace(l, char) if l in chars else l, string_list))
        return ''.join(result)

print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))


print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))


print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))