def start():
    print("Inside Loops in Python")

    print("For Loop =>", end=" ")
    for i in range(1, 6):
        print(i, end=" ")

    print("\nWhile Loop =>", end=" ")
    temp = 1
    while temp <= 10:
        print(temp, end=" ")
        temp = temp + 1

    print("\nBreak and Continue Clause in Loops")
    var = 100
    while var > 0:
        print("Hi", end=" ")
        var = var - 10
        if var < 25:
            print("\nBreaking Loop")
            break
        else:
            continue
