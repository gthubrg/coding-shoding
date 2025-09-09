def BubbleSort(Array):
	Length = len(Array)

	for i in range(0,Length):
		for j in range(0, Length - i - 1):
			if Array[j] > Array[j + 1] :
				Array[j], Array[j + 1] = Array[j + 1], Array[j]
A = [74, 3, 34, 57, 82, 1, 10, 22]

BubbleSort(A)

print ("SORTED ARRAY : ")
for i in range(len(A)):
	print (A[i], end = " ")