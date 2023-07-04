def printPairs(arr, n, sum):
	for i in range(0, n):
		for j in range(i + 1, n):
			if (arr[i] + arr[j] == sum):
				print(arr[i], " ", arr[j], sep="")

def start():
    print('Inside Pair Sum Problem')
    arr = [10, -50, 90, 150, 25, -75, 75]
    n = len(arr)
    sum = 100
    print('Pairs Summing Upto', sum, "Are")
    printPairs(arr, n, sum)
