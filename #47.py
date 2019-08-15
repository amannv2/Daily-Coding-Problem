# Given a array of numbers representing the stock prices of a company in chronological order, write a function that
# calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you
# can sell it.
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5
# dollars and sell it at 10 dollars.


stock = [9, 11, 8, 5, 7, 10]

max_diff = stock[1] - stock[0]
min_val = stock[0]

for i in range(len(stock)):

    if stock[i] - min_val > max_diff:
        max_diff = stock[i] - min_val

    if stock[i] < min_val:
        min_val = stock[i]

print(f'>>{max_diff}')

