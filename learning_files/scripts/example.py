"""It's example doctest using."""

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]  # filter out all odd numbers
final_list = list(filter(lambda ite: (ite % 2 != 0), li))
print(final_list)

# filter out all odd numbers
