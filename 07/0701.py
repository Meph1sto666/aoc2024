import typing
from op import Op, generate_combinations, create_both_ops
puzzle: list[list[int]] = [sum([[int(n) for n in i.split(" ")] for i in l.split(": ")], []) for l in open("./0701.txt")]

equations: list[tuple[int, list[int]]] = []
for i, equation in enumerate(puzzle):
	equations.append((equation[0], equation[1:]))

valid: list[int] = []
for i, equation in enumerate(equations):
	print(i/len(equations))
	cmbs: typing.Iterable[Op] = generate_combinations(create_both_ops(equation[1][0], equation[1][1]), equation[1][2:])
	if len([equation[0] for c in cmbs if c.eval() == equation[0]])>0:
		valid.append(equation[0])
print(sum(valid))