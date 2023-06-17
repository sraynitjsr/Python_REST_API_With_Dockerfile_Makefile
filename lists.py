def start():
    print('Inside Lists')
    list1 = ['ABCD', 100 , 35.46, 'XYZ']
    list2 = [123, 'MSD']
    print ('Full List', list1)
    print ('First Element in List', list1[0])
    print ('Last Element in List', list1[-1])
    print ('List Elements From Index 1 to 3', list1[1:3])
    print ('List Elements From Index 2 to Last', list1[2:])
    print ('Print List Twice', list2 * 2)
    print ('List Concatenation', list1 + list2)

    myList = [100, 300, 200, 500, 400]
    print ('Unsorted List =>', myList)
    myList.sort(reverse=True)
    print ('Sorted List =>', myList)
