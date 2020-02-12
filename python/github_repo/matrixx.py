A = []
n = int(input("Enter N for N * N matrix:"))
print("Enter the element :")
for i in range(n):
	row = []
	for j in range (n):
		row.append(int(input()))
		A.append(row)
print (A)
print ("Display in Matrix")	
for i in range(n):
	row = []
	for j in range (n):
		print(A[i][j])
	print()	

B = []
n = int(input("Enter N for N * N matrix:"))
print("Enter the element :")
for i in range(n):
	row = []
	for j in range (n):
		row.append(int(input()))
		B.append(row)
print (B)
print ("Display in Matrix")	
for i in range(n):
	row = []
	for j in range (n):
		print(B[i][j])
	print()
result = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(len(A)):
	for j in range(len(B[0])):
		for k in range(len(B)):
			result[i][j] += A[i][k] * B[k][j]
print ("the final matrix :")
for r in result :
	print (r)			
