def determinant(matrix):
    '''
    This function recursively calculates the determiinant of an n x n matrix,
    stored as a list of lists.
    '''
    # Make sure that the user actually passed in a list of lists
    try:
        len(matrix[0])
    except:
        raise TypeError('Matrix must be a list of lists')
    # Ensure that we have a square matrix
    if len(matrix) != len(matrix[0]):
        raise ValueError('Matrix must be square')
    # If we got a 1x1 matrix, just return that number
    elif len(matrix) == 1:
        return matrix[0]
    # If we have a 2x2, its determinant can be calculated directly
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    # Otherwise, apply the determinant formula recursively
    else:
        signs = [(-1)**i for i in range(len(matrix[0]))]
        recursive_det = 0
        # For each item in the first row, match it to its proper sub-determinant
        for i in range(len(matrix[0])):
            # Copy the full matrix except for the first row
            sub_matrix = [[] for n in range(len(matrix[1:]))]
            for n in range(len(sub_matrix)):
                for m in range(len(matrix[0])):
                    sub_matrix[n].append(matrix[n+1][m])
            # Remove the ith item from each row to finish creating our sub-matrix
            for j in range(len(sub_matrix)):
                sub_matrix[j].pop(i)
            # Calculate the determinant of the entire matrix recursively, one sub-matrix at a time
            recursive_det += signs[i] * matrix[0][i] * determinant(sub_matrix)
        return recursive_det
