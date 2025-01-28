# H, W = map(int, input().split())

# A = [list(map(int, input().split())) for _ in range(H)]

# A_transposed = list(zip(*A))


# sum_row = [sum(row) for row in A]
# sum_col = [sum(col) for col in A_transposed]

# B = [[sum_row[i] + sum_col[j] - A[i][j] for j in range(W)] for i in range(H)]

# for row in B:
#     print(*row)


import numpy as np

H, W = map(int, input().split())

A = np.array([list(map(int, input().split())) for _ in range(H)])

sum_row = A.sum(axis=1) 
sum_col = A.sum(axis=0)

B = sum_row[:, np.newaxis] + sum_col - A

for row in B:
    print(*row.astype(int))
