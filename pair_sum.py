def printPairs(arr, n, sum):
	mydict = dict()
	for i in range(n):
		temp = sum - arr[i]
		if temp in mydict:
			count = mydict[temp]
			for j in range(count):
				print(temp, " ", arr[i], sep="")
		if arr[i] in mydict:
			mydict[arr[i]] += 1
		else:
			mydict[arr[i]] = 1

def start():
    print('Inside Pair Sum Problem')
    arr = [10, -50, 90, 150, 25, -75, 75]
    n = len(arr)
    sum = 100
    print('Pairs Summing Upto', sum, "Are")
    printPairs(arr, n, sum)
