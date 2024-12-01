puzzle = open("0101.txt", "r")
l1, l2 = [], []
for l in puzzle:
    l = l.replace("\n", "")
    if not l: continue
    v1, v2 = l.split("   ")
    l1.append(int(v1))
    l2.append(int(v2))

deltas = []
gm = max(max(l1), max(l2))
while(len(deltas) < len(l1)):
    m1 = min(l1)
    i1 = l1.index(m1)
    m2 = min(l2)
    i2 = l2.index(m2)
    l1[i1] = gm+1
    l2[i2] = gm+1
    deltas.append(max(m1, m2)-min(m1,m2))
print(sum(deltas))
