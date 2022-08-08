# if __name__ == '__main__':
#     arr = [['alpha', 20], ['chi', 40], ['omega', 100], ['beta', 40]]
#
#
#     list_of_grades = [x[1] for x in arr]
#
#     list_of_grades = list(set(list_of_grades))
#     list_of_grades.sort()
#
#     second_grade = list_of_grades[1]
#
#     students_with_second_grade = [x[0] for x in arr if x[1] == second_grade]
#
#     students_with_second_grade.sort()
#
#     print(students_with_second_grade)

# arr = [20, 32, 12]
# # print(arr.mean())
# # print(f'{(sum(arr) / len(arr)).2f}')
#
# # print('{:.4f}'.format(21.33352251))
# # print('21.33352251'.format(:.2f))
# # print("Floating point {:.2f}".format(345.7916732))
#
# name = "Greg"
# age = 40
#
# print('My name is {0} and I am {1} years old'.format(name, age))

# def staircase(n):
#     for i in range(1, n + 1):
#         print((n - i) * ' ', end='')
#         print(i * '#')
#
#
# if __name__ == '__main__':
#     # n = int(input().strip())
#
#     staircase(6)
#
# print('tst')
def migratoryBirds(arr):
    dic = {}

    unique_value = set(arr)

    for value in unique_value:
        freq_value = arr.count(value)
        dic[value] = freq_value

    max_value = max(dic.values())

    result = []

    for key, value in dic.items():
        if value == max_value:
            result.append(key)

    return min(result)

migratoryBirds([1, 1, 1, 12, 12, 12, 3, 4, 5, 4, 3])
