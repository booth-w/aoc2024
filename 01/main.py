import collections


def part1(input: list) -> int:
	left, right = zip(*[line.split() for line in input])
	return sum(abs(int(l) - int(r)) for l, r in zip(sorted(left), sorted(right)))

def part2(input: list) -> int:
	left, right = zip(*[line.split() for line in input])
	rightCounter = collections.Counter(right)
	return sum([rightCounter[l]*int(l) for l in left])


if __name__ == "__main__":
	with open("input.txt") as f:
		print(part2(f.readlines()))
