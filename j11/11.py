def upper(s):
    return s.upper()
    
mylist = list(map(upper, ['sentence', 'fragment']))
print(mylist)
# ['SENTENCE', 'FRAGMENT']

# Convert a string representation of
# a number into a list of ints.
list_of_ints = list(map(int, "1234567"))
print(list_of_ints)
# [1, 2, 3, 4, 5, 6, 7]
