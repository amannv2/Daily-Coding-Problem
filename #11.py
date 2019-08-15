# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings
# [dog, deer, deal], return [deer, deal].

# Hint: Try pre-processing the dictionary into a more efficient data structure to speed up queries.


my_list = ['deer', 'beer', 'sheer', 'ball', 'bump', 'dump', 'sheep', 'beep', 'deal', 'meal', 'seal', 'seat']
result = []

match = 's'
max_len = len(match)

for item in my_list:
    if item[:max_len] == match:
        result.append(item)

print(f'{my_list}\n\n{result}')
