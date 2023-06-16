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
    my_dict["X"] = 4040
    my_dict["Y"] = 5050
    my_dict["Z"] = 6060
    for k, v in my_dict.items():
        if k == "Y":
            print ('Found Y with Value', v)
            break
