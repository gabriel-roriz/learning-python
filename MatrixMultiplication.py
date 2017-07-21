matrix_1 = []
matrix_2 = []

ij_1 = [x for x in input('1: [i,j]').split(',')]
ij_2 = [x for x in input('2: [i,j]').split(',')]

for i in range(int(ij_1[0])):
    row = []
    for j in range(int(ij_1[1])):
        row.append(input('[{i},{j}]'.format(j = j, i = i)))

    matrix_1.append(row)

for i in range(int(ij_2[0])):
    row = []
    for j in range(int(ij_2[1])):
        row.append(input('[{i},{j}]'.format(j=j, i=i)))

    matrix_2.append(row)


print(matrix_1)
print(matrix_2)



