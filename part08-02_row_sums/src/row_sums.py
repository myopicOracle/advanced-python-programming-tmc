# Write your solution here

def row_sums(my_matrix: list) -> None:

    for row in my_matrix:
        row_sum = 0

        for item in row:
            row_sum += item

        row.append(row_sum)

# my_matrix = [[1, 2], [3, 4]]
# row_sums(my_matrix)
# print(my_matrix)