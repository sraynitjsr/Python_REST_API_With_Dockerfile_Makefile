from collections import OrderedDict

def start():
    print('Inside Dictionaries in Python')
    my_dict = {"A": 100, "C": 500}
    print(my_dict)
    my_dict["B"] = 1000
    print('After Adding C', my_dict)
    my_dict["B"] = 2020
    print('After Updating Value for B', my_dict)
    del my_dict["C"]
    print('After Deleting Key C, Full Dictionary =>', my_dict)
    my_dict["X"] = 4040
    my_dict["Z"] = 5050
    my_dict["Y"] = 6060
    for k, v in my_dict.items():
        if k == "Y":
            print ('Found Y with Value', v)
            break
    print('Unsorted', my_dict)
    sortedDictionary = OrderedDict(sorted(my_dict.items()))    
    print('Sorted by Items =>', sortedDictionary)
