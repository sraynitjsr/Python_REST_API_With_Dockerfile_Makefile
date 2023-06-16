def start():
    print('Inside Dictionaries in Python')
    my_dict = {"A": 100, "B": 500}
    print(my_dict)
    my_dict["C"] = 1000
    print('After Adding C', my_dict)
    my_dict["B"] = 2020
    print('After Updating Value for B', my_dict)
    del my_dict["C"]
    print('After Deleting Key C, Full Dictionary =>', my_dict)
