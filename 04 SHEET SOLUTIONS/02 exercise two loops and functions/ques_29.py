list_num = [14,56,45,123,45,78,156,55]
# list_final = []
# for i in list_num:
#     if i < max(list_num):
#         list_final.append(i)
# print(max(list_final))
first = second = float("-inf")
for i in list_num:
    if i > first:
        second = first
        first = i
    elif i > second and i!= first:
        second = i
print(second)

