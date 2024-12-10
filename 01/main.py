def part1(input: list) -> int:
	left, right = zip(*[line.split() for line in input])
	return sum(abs(int(l) - int(r)) for l, r in zip(sorted(left), sorted(right)))


if __name__ == "__main__":
	with open("input.txt") as f:
		print(part1(f.readlines()))
