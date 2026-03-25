my_list = []
for x in range(1, 10):
    my_list.append(x)
    print("Original list:",my_list)
    print("Length of list:", len(my_list))
    unique_list = []
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
            print("\nThe list with unique elements only.")
            print(unique_list)
