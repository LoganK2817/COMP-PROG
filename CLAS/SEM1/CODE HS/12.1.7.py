my_tuple = (0, 1, 2, "hi", 4, 5)

# Your code here...

slice_one = my_tuple[:3]
slice_two = my_tuple[4:6]

my_tuple = slice_one + (3,) + slice_two



print(my_tuple)
