def min_heapify(a, n, i):
	"""
	After every iteration root is minimum
	"""
	smallest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and a[l] < a[i]:
		smallest = l

	if r < n and a[r] < a[smallest]:
		smallest = r

	if smallest != i:
		a[i], a[smallest] = a[smallest], a[i]
		min_heapify(a, n, smallest)


def heap_sort(a):
	n = len(a)
	for i in range(n, -1, -1):
		min_heapify(a, n, i)

	#Heapifies from leaf to root
	for i in range(n - 1, 0, -1):
		a[i], a[0] = a[0], a[i]
		min_heapify(a, i, 0)


if __name__ == '__main__':
	a = [int(each) for each in input().split(' ')]
	heap_sort(a)
	print(a)