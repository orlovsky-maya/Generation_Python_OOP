n = int(input())
martrix = [[1] * n for _ in range(n)]
nums = n // 2 + n % 2
for digit in range(2, nums + 1):
    for i in range(digit - 1, n - digit + 1):
        for j in range(digit - 1, n - digit + 1):
            martrix[i][j] = digit
            martrix[j][i] = digit
for i in range(n):
    for j in range(n):
        print(martrix[i][j], end=' ')
    print()

"""
INPUT DATA:

TEST_1:
1

TEST_2:
2

TEST_3:
3

TEST_4:
4

TEST_5:
5 
"""
"""
# OUTPUT DATA:

# TEST_1:
1

# TEST_2:
1 1
1 1

# TEST_3:
1 1 1
1 2 1
1 1 1

# TEST_4:
1 1 1 1
1 2 2 1
1 2 2 1
1 1 1 1

# TEST_5:
1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1
"""