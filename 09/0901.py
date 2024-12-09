puzzle_string: str = open("0901.txt").read()
puzzle_string = puzzle_string.ljust(len(puzzle_string)+((len(puzzle_string)+1)%2==0), "0")

blocks: list[tuple[int, int]] = [(int(puzzle_string[i]), int(puzzle_string[i+1])) for i in range(0, len(puzzle_string)-1, 2)]

re_ordered: list[str] = []
for i, block in enumerate(blocks):
	re_ordered.extend([str(i) for _ in range(block[0])])
	re_ordered.extend(["." for _ in range(block[1])])

pl: int = 0
pr: int = len(re_ordered)-1

while pl < pr:
	if re_ordered[pl] != ".":
		pl+=1
	if re_ordered[pr] == ".":
		pr-=1
	if re_ordered[pl] == "." and re_ordered[pr] != ".":
		re_ordered[pl] = re_ordered[pr]
		re_ordered[pr] = "."

checksum = 0
for i in range(len(re_ordered)):
	if re_ordered[i] == ".":
		break
	checksum+=i*int(re_ordered[i])

print(checksum)