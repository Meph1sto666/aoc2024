import re
from operator import mul # type: ignore

puzzle: str = open("./0301.txt").read()
instructions: list[str] = re.findall(r"mul\(\d+,\d+\)", puzzle)

print(sum([eval(i) for i in instructions]))