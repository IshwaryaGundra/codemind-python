def isPalindrome(n: int) -> bool:

	rev = 0
	i = n
	while i > 0:
		rev = rev * 10 + i % 10
		i //= 10
	return (n == rev)

# prints palindrome between min and max
def countPal(minn: int, maxx: int) -> None:
	for i in range(minn, maxx + 1):
		if isPalindrome(i):
			print(i, end = " ")

# Driver Code
n=int(input())
m=int(input())
if __name__ == "__main__":
	countPal(n, m)

# This code is contributed by
# sanjeev2552
