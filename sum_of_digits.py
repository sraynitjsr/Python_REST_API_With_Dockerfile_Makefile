def start():
    print('\nInside Sum of Digits File')
    n = 345
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n/10)
    print ('Sum of Digits of 345 =>', sum)
