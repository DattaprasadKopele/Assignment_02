" count number which appears more than once in list "


## method1 using counter() function from collection module

# from collections import Counter
#
# l = [1, 2, 3, 4,1, 2, 1, 3, 5, 6, 7, 8, 8, 8, 8, 9, 10]
#
# d = Counter(l)
#
# print(d)
#
# new_list = list([item for item in d if d[item]>1])
# print(new_list)


## method 2 using the brute force approach

# l = [1, 2, 3, 4,1, 2, 1, 3, 5, 6, 7, 8, 8, 8, 8, 9, 10]
#
# def Repeat(x):
#     _size = len(x)
#     repeated = []
#
#     for i in range(_size):
#         k = i+1
#
#         for j in range(k, _size):
#             if x[i] == x[j] and x[i] not in repeated:
#                 repeated.append(x[i])
#
#     return repeated
# print(Repeat(l))


