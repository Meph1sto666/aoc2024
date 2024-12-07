import typing
class Op:
	def __init__(self, n1: typing.Any, n2: typing.Any, sym: typing.Literal["+", "*"]) -> None:
		self.n1: Op | int = n1
		self.n2: Op | int = n2
		self.sym: typing.Literal["+", "*"] = sym

	def eval(self) -> int:
		n1: int = self.n1.eval() if isinstance(self.n1, Op) else self.n1
		n2: int = self.n2.eval() if isinstance(self.n2, Op) else self.n2
		return n1+n2 if self.sym == "+" else n1*n2

	def __str__(self) -> str:
		return f"{self.n1}{self.sym}{self.n2}"

	def __hash__(self) -> int:
		return self.__str__().__hash__()

def create_both_ops(i1: Op | int, i2: Op | int) -> tuple[Op, Op]:
	return (Op(i1, i2, "+"), Op(i1, i2, "*"))

def generate_combinations(ops: typing.Iterable[Op], ints: list[int]) -> typing.Iterable[Op]:
	all_cmbs: list[Op] = []
	if len(ints) == 0:
		return ops
	for o in ops:
		all_cmbs.extend(generate_combinations(create_both_ops(o, ints[0]), ints[1:]))
	return all_cmbs