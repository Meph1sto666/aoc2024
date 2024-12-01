puzzle = open("0102.txt", "r")
l1, l2 = [], []
for l in puzzle:
    l = l.replace("\n", "")
    if not l: continue
    v1, v2 = l.split("   ")
    l1.append(int(v1))
    l2.append(int(v2))

deltas = []
for i in range(len(l1)):
    deltas.append(l1[i]*l2.count(l1[i]))
print(sum(deltas))
