import re
from operator import mul # type: ignore

puzzle: str = open("./0302.txt").read()

enabled: str = re.sub(r"don't\(\).*?do\(\)", "", puzzle, flags=re.S)
instructions: list[str] = re.findall(r"mul\(\d+,\d+\)", enabled)

print(sum([eval(i) for i in instructions]))