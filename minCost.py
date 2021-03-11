from itertools import permutations


def minCost(matrix):
	list = []
	for x in range(len(matrix)):
		list.append(x)
		
	list.pop(0)

	mincost = 99999999999999999

	perm = permutations(list)
	origin = []
	path = []
	for combo in perm:
		for num in combo:
			origin.append(combo[num-1])
		destination = origin.copy()
		origin.insert(0,0)
		destination.append(0)
		cost = 0
		for i in range(len(origin)):
			x = origin[i]
			y = destination[i]
			cost += int(matrix[x][y])
		if (cost < mincost):
			mincost = cost
			path = origin.copy()
		origin = []
	return (path, mincost)
		

