def log_for(logfile, date_str):
    with (
        open(logfile, mode="r", encoding="utf-8") as logfile,
        open(f"log_for_{date_str}.txt", mode="w", encoding="utf-8") as output
    ):
        for line in logfile.readlines():
            if date_str in line:
                output.write(" ".join(line.split(" ")[1:]))


with open('log.txt', 'w', encoding='utf-8') as file:
    print('2022-01-01 INFO: User logged in', file=file)
    print('2022-01-01 ERROR: Invalid input data', file=file)
    print('2022-01-02 INFO: User logged out', file=file)
    print('2022-01-03 INFO: User registered', file=file)

log_for('log.txt', '2022-01-01')

with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
    print(file.read())

# Valid output
# INFO: User logged in
# ERROR: Invalid input data
#
