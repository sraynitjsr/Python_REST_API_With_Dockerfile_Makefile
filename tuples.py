def start():
    print('Inside Tuples')
    tuple1 = ('ABCD', 100 , 35.46, 'XYZ')
    tuple2 = (123, 'MSD')
    print ('Full Tuple', tuple1)
    print ('First Element in Tuple', tuple1[0])
    print ('Last Element in Tuple', tuple1[-1])
    print ('Tuple Elements From Index 1 to 3', tuple1[1:3])
    print ('Tuple Elements From Index 2 to Last', tuple1[2:])
    print ('Print Tuple Twice', tuple2 * 2)
    print ('Tuple Concatenation', tuple1 + tuple2)
   