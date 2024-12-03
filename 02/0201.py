f = open("./0201.txt")
safe: int = 0
for line in f:
    lvls: list[int] = [int(i) for i in line.split(" ")]
    if (len(lvls) == 0): continue
    asc: bool = (lvls[0] - lvls[1]) <= 0
    this_safe = True
    for i in range(len(lvls) - 1):
        if asc == (lvls[i] - lvls[i+1] >= 0):
            this_safe = False
            break
        if not 1<=abs(lvls[i] - lvls[i+1])<=3:
            this_safe=False
            break
    safe += this_safe
print(safe)
