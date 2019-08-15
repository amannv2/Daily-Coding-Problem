# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs
# come first, the Gs come second, and the Bs come last. You can only swap elements of the array. Do this in linear
# time and in-place. For example,
# given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

gbr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
length = len(gbr)

print(gbr)

index = 0
for elm in gbr:
    if elm == 'R':
        del gbr[index]
        gbr.insert(0, 'R')
        print(f'{length} - {index} - {elm} - {gbr}')

    elif elm == 'B':
        del gbr[index]
        gbr.append('B')
        print(f'{length} - {index} - {elm} - {gbr}')

    else:
        pass
    index += 1

# TODO:
# #35 not done
