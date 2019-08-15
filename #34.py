# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible
# anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the
# lexicographically earliest one (the first one alphabetically). For example, given the string "race", you should
# return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There
# are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first
# alphabetically. As another example, given the string "google", you should return "elgoogle".


# Again, no idea if it is correct -- gives satisfactory results, tho.


in_str = 'laptop'
new_str = in_str
rev_str = in_str[::-1]

if in_str[-1:] < in_str[:1]:
    # append in the beg
    count = 0
    while new_str != new_str[::-1]:
        new_str = rev_str[:count] + in_str
        count += 1
else:
    # append at the end
    count = 0
    new_str = in_str
    while new_str != new_str[::-1]:
        new_str = in_str + rev_str[1:count]
        count += 1
        pass

print(f'\n{in_str} <--> {new_str}')
