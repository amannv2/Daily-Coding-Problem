# EDIT DISTANCE BETWEEN TWO STRINGS

str1 = input('Enter first string: ')
str2 = input('Enter second string: ')


row, col = (len(str1) + 1, len(str2) + 1)
ptr1, ptr2 = (row, col)

# matrix
tab = [[0 for i in range(col)] for j in range(row)]

cost = 0

for i in range(row):
    tab[i][0] = i

for j in range(col):
    tab[0][j] = j

# fill up the tab matrix
for i in range(1, row):
    for j in range(1, col):

        if str1[i - 1] == str2[j - 1]:
            cost = 0
        else:
            cost = 1

        tab[i][j] = min(tab[i - 1][j] + 1, tab[i][j - 1] + 1, tab[i - 1][j - 1] + cost)


print(f'Edit Distance: \n\t\t\t{str1} -> {str2} :: {tab[row - 1][col - 1]}\n\n')

# printing the matrix
for row in tab:
    print(row)
