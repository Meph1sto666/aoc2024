puzzle: list[list[int]] = [[int(i) for i in l.split(" ")] for l in list(open("./0202.txt"))]

def asc_or_dec(l: list[int]) -> bool:
	return sorted(l) == l or sorted(l, reverse=True) == l

def min_max_diff(l: list[int]) -> bool:
	faulty: list[bool] = [1<=abs(l[i]-l[i+1])<=3 for i in range(len(l)-1)]
	print(faulty, l)
	return all(faulty)

safe = 0
for l in puzzle:
	for i in range(len(l)+1):
		cpy: list[int] = l.copy()
		if i != len(l):
			cpy.pop(i)
		if min_max_diff(cpy) and asc_or_dec(cpy):
			safe +=1
			break

print(safe)