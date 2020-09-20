# TASK 3
# There are a few huge text files (>1TB each). You need to write an eternal generator, which outputs those files in
# a multiplexed file-by-file line-by-line order. The next line after the last one is the first one.
# The next file after the last one is, again, the first one.
#

# if we work with small files

F1 = open('1.txt', 'r')
list_of_strings1 = F1.readlines()
F2 = open('2.txt', 'r')
list_of_strings2 = F2.readlines()
F3 = open('3.txt', 'r')
list_of_strings3 = F3.readlines()
F_total = open('total.txt', 'w')

i = 0
j = 0
c = 0

while i >= 0 or j >= 0 or c >= 0:
    if i <= (len(list_of_strings1) - 1) and j <= (len(list_of_strings2) - 1) and c <= (len(list_of_strings3) - 1):
        F_total.write(list_of_strings1[i])
        F_total.write(list_of_strings2[j])
        F_total.write(list_of_strings3[c])
        i += 1
        j += 1
        c += 1

    if i <= (len(list_of_strings1) - 1) and j <= (len(list_of_strings2) - 1) and c == (len(list_of_strings3)):
        c = 0

    if i == (len(list_of_strings1)) and j <= (len(list_of_strings2) - 1) and c <= (len(list_of_strings3)):
        i = 0

    if i <= (len(list_of_strings1)) and j == (len(list_of_strings2)) and c <= (len(list_of_strings3)):
        j = 0

F1.close()
F2.close()
F3.close()
F_total.close()


# if we work with big data files

from itertools import chain

# F1 = open('1.txt', 'r')
# count_s1 = F1.readlines()
# c1 = len(count_s1)
# F1.close()
#
# F2 = open('2.txt', 'r')
# count_s2 = F2.readlines()
# c2 = len(count_s2)
# F2.close()
#
# F3 = open('3.txt', 'r')
# count_s3 = F3.readlines()
# c3 = len(count_s3)
# F1.close()
#
# #
# def read_by_string_1(f1, line):
#     """
#     Lazy function to read a string by string
#     """
#     while True:
#         data = f1.read(line)
#         if not data:
#             break
#         yield data
# #
# # def read_by_string_2(f2, j):
# #     while True:
# #         data = f2.read(j)
# #         if not data:
# #             break
# #         yield data
# #
# # def read_by_string_3(f3, z):
# #     while True:
# #         data = f3.read(z)
# #         if not data:
# #             break
# #         yield data
# #
# F_total = open('total.txt', 'w')
#
# i = 0
# j = 0
# z = 0
#
# c1 = len(count_s1)
#
# t1 = 0
# t2 = 0
# t3 = 0
#
# while i<=(c1-1) or j<= (c2-1) or j<= (c3-1):
#     while t1 <= c1 or t2 <= c2 or t2 <= c3:
#         with open('1.txt') as f1:
#             for line in f1:
#                 if t1 == i:
#                     F_total.write(line)
#                     break
#                 f1.close()
#                 i+=1
#                 t1+=1
#             with open('2.txt') as f2:
#                 for line in f2:
#                     if t2 == j:
#                         F_total.write(line)
#                         break
#                     f2.close()
#                     j+=1
#                     t2+=1
#
#                 with open('3.txt') as f3:
#                     for line in f3:
#                         if t3 == z:
#                             F_total.write(line)
#                             break
#                         f3.close()
#                         z += 1
#                         t3 += 1
#
#
#
#
#
#
#
#             # for line in read_by_string_1(f1, line):
#             #         F_total.write(line)
#             #         i+=1
# #             for linej in read_by_string_2(f2, j):
# #                     F_total.write(linej)
# #                     j+=1
# #             for linez in read_by_string_3(f3, z):
# #                     F_total.write(linez)
# #                     z+=1
# #
# #             f3.close()
# #             f2.close()
# #             f1.close()
# #             F_total.close()
#
#
# # spent time is about 12 h
#
#
# # F_total.write('\n')