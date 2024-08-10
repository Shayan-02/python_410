mylist = [1, 1, 2, 3, 4, 5, 5, 5, 6, 6]
print(set(mylist))
# {1, 2, 3, 4, 5, 6}

# And since a string can be treated like a
# list of letters, you can also get the
# unique letters from a string this way:
print(set("aaabbbcccdddeeefff"))
# {'a', 'b', 'c', 'd', 'e', 'f'}
