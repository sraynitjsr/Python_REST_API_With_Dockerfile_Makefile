def checkPalindrome(n):
    reverse = 0
    temp = n
    while (temp != 0):
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10
    return (reverse == n)

def start():
    print('Inside Number Palindrome File')
    
    n1 = 23432
    if (checkPalindrome(n1) == 1):
        print(n1, "is palindrome")
    else:
        print(n1, "is not a palindrome")

    n2 = 2020
    if (checkPalindrome(n2) == 1):
        print(n2, "is palindrome")
    else:
        print(n2, "is not a palindrome")
