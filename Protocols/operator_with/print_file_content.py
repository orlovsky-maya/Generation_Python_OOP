def print_file_content(filename):
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            print(file.read())
    except Exception as error:
        print("Файл не найден")


with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
    file.write('Сражения и путешествия берут своё')

print_file_content('Precepts_of_Zote.txt')

# Valid output
# "Сражения и путешествия берут своё"

print_file_content('Precepts_of_Zote2.txt')

# Valid output
# Файл не найден