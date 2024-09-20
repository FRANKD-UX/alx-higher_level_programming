#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Create a new row with squared values
        new_row = [x ** 2 for x in row]
        # Append the new row to the new matrix
        new_matrix.append(new_row)

    return new_matrix

# Example usage:
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

squared_matrix = square_matrix_simple(original_matrix)

print("Original matrix:")
for row in original_matrix:
    print(row)

print("\nSquared matrix:")
for row in squared_matrix:
    print(row)

