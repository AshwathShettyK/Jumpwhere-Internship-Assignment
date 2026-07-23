# Q17: Sort a matrix by the sum of each row using lambda.

matrix = [
    [3, 5, 1],
    [10, 2, 6],
    [4, 4, 4]
]

print("Original matrix:")
for row in matrix:
    print(row)

sorted_matrix = sorted(matrix, key=lambda row: sum(row))
print("\nSorted matrix by row sum:")
for row in sorted_matrix:
    print(row)
