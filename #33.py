# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of
# the list so far on each new element. Recall that the median of an even-numbered list is the average of the two
# middle numbers. For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

numbers = [2, 1, 5, 7, 2, 0, 5]
temp = []


# not efficient? ofc.

def cal_median(num):
    temp.append(num)
    temp.sort()

    length = len(temp)

    if length % 2 != 0:
        median = temp[int(length / 2)]
    else:
        median = (temp[int(length/2)] + temp[(int(length/2)) - 1])/2

    print(f'{temp} --- {median}')
    pass


for i in range(len(numbers)):
    cal_median(numbers[i])
