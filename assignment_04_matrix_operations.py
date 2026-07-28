def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end="\t")
        print()


# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)

    return transposed


# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            sum_val = matrix_a[r][c] + matrix_b[r][c]
            new_row.append(sum_val)
        result.append(new_row)

    return result


# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = []
    for r in range(rows_a):
        new_row = []
        for c in range(cols_b):
            cell_sum = 0
            for k in range(cols_a):
                cell_sum = cell_sum + (matrix_a[r][k] * matrix_b[k][c])
            new_row.append(cell_sum)
        result.append(new_row)

    return result


# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # --- PART A: TRANSPOSE ---
    print("--- PART A: TRANSPOSE MATRIX ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix_a = []
    for i in range(1, rows + 1):
        user_input = input(f"Enter row {i}: ")
        row_str = user_input.split()

        # Convert input text into numbers
        row_num = []
        for item in row_str:
            row_num.append(int(item))
        matrix_a.append(row_num)

    print("\nOriginal Matrix:")
    print_matrix(matrix_a)

    print("\nTransposed Matrix:")
    transposed = transpose_matrix(matrix_a)
    print_matrix(transposed)

    # --- PART B: ADDITION ---
    print("\n--------------------------------------------------")
    print("--- PART B: ADD TWO MATRICES ---")
    print("Enter values for Matrix B (same size):")

    matrix_b = []
    for i in range(1, rows + 1):
        user_input = input(f"Enter row {i}: ")
        row_str = user_input.split()

        row_num = []
        for item in row_str:
            row_num.append(int(item))
        matrix_b.append(row_num)

    print("\nMatrix A + Matrix B:")
    added_matrix = add_matrices(matrix_a, matrix_b)
    print_matrix(added_matrix)

    # --- PART C: MULTIPLICATION ---
    print("\n--------------------------------------------------")
    print("--- PART C: MULTIPLY TWO MATRICES ---")
    cols_c = int(input(f"Enter number of columns for Matrix C ({cols}x?): "))

    matrix_c = []
    for i in range(1, cols + 1):
        user_input = input(f"Enter row {i}: ")
        row_str = user_input.split()

        row_num = []
        for item in row_str:
            row_num.append(int(item))
        matrix_c.append(row_num)

    print("\nMatrix A x Matrix C:")
    multiplied_matrix = multiply_matrices(matrix_a, matrix_c)
    print_matrix(multiplied_matrix)