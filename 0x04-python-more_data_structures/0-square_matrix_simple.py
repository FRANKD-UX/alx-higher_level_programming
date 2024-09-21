#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    # Create a new matrix with the same size as the input matrix
    new_matrix = []

    # Iterate through each row in the matrix
    for row in matrix:
        # Create a new row to store the squared values
        new_row = []
        # Iterate through each element in the row
        for element in row:
            # Append the square of the element to the new row
            new_row.append(element ** 2)
        # Append the new row to the new matrix
        new_matrix.append(new_row)

    return new_matrix
