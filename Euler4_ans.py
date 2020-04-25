# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

A = 0
B = 0
palindroms = []
for A in range(999,900,-1):
	for B in range(999,900,-1):
		L = A*B
		X = str(A*B)
		Z = X[::-1]
		print("Число А: {}".format(A))
		print("Число B: {}".format(B))
		print("Число L: {}".format(L))
		print("Число X: {}".format(X))
		print("Число Z: {}".format(Z))
		if X == Z:
			palindroms.append(X)
print(max(palindroms))
