class Warden:
	def __init__(self, x: int, y: int, puzzle: list[list[str]]) -> None:
		self.rotation: int = 0
		self.x: int = x
		self.y: int = y
		self.puzzle: list[list[str]] = puzzle
	
	def move(self) -> None:
		self.x, self.y = self.get_next_tile()
	
	def turn(self) -> None:
		self.rotation = (self.rotation+90)%360

	def get_next_tile(self) -> tuple[int, int]:
		match self.rotation:
			case 0:
				return (self.x, self.y-1)
			case 90:
				return (self.x+1, self.y)
			case 180:
				return (self.x, self.y+1)
			case 270:
				return (self.x-1, self.y)
			case _:
				raise ValueError("Ain't no rotation then ig.")

	def can_move(self) -> bool:
		facing_tile: tuple[int, int] = self.get_next_tile()
		return not (self.puzzle[facing_tile[1]][facing_tile[0]] in ["#"])
	
	def patrol(self) -> list[tuple[int, int]]:
		path: list[tuple[int, int]] = list()
		segments: list[list[tuple[int, int]]] = []
		segment: list[tuple[int, int]] = []
		while True:
			facing: tuple[int, int] = self.get_next_tile()
			if not (0 <= facing[1] < len(self.puzzle) and (0 <= facing[0] < len(self.puzzle[2]))):
				path.extend(sum(segments, segment))
				return path
			if self.can_move():
				self.move()
				# path.append(facing)
				segment.append(facing)
			else:
				if len(segment) > 0 and segment in segments:
					return [(-1, -1)]
				segments.append(segment)
				segment = []
				self.turn()

	def trap(self) -> set[tuple[int, int]]:
		starting_pos: tuple[int, int] = self.x, self.y
		full_path: list[tuple[int, int]] = self.patrol()		
		possible_spots: set[tuple[int, int]] = set(full_path)
		traps: set[tuple[int, int]] = set()
		
		for spot in possible_spots:
			self.x, self.y = starting_pos
			self.rotation = 0
			self.puzzle[spot[1]][spot[0]] = "#"
			if self.patrol() == [(-1, -1)]:
				traps.add(spot)
			self.puzzle[spot[1]][spot[0]] = "."
		return traps


def find_warden(puzzle: list[list[str]]) -> Warden:
	for i, l in enumerate(puzzle):
		if not "^" in l:
			continue
		return Warden(l.index("^"), i, puzzle)
	raise BaseException("No warden? :(")