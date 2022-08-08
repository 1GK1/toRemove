import math
from collections import OrderedDict
from collections import Counter


def flippingMatrix(matrix):
    main_matrix_size = len(matrix)
    sub_matrix_size = int(math.sqrt(main_matrix_size))



    matrix_sums = []
    def count_sum(matrix, sub_matrix_size):
        matrix_sum = 0

        matrix_sums.append(matrix_sum)


    count_sum(matrix, sub_matrix_size)


matrix = [[112, 42, 83, 119],
          [56, 125, 56, 49],
          [15, 78, 101, 43],
          [62, 98, 114, 108]]


max_sum = flippingMatrix(matrix)
print(max_sum)