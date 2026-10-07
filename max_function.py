def find_max(my_list):
    max_value = my_list[0]
    for item in my_list:
        if item > max_value:
            max_value = item
    return max_value

my_list = [1, 20, 3, 6, 4, 5, 7, 15, 8, 9]
max_value = find_max(my_list)
print("The maximum value is:", max_value)