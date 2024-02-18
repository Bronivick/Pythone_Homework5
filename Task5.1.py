list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, 10, 2, 0, -9, 8, 10, -9, 0, 5, 5]
max_number = 10
min_number = 0
list_2 = []
for i in range(len(list_1)):
    if list_1[i] >= min_number and list_1[i] <=max_number:
        list_2.append(i)
print(list_2)