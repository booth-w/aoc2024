def checkReport(levels: list) -> bool:
	if not (levels == sorted(levels) or levels == sorted(levels, reverse=True)):
		return False

	for a in range(len(levels)-1):
		difference = abs(levels[a] - levels[a+1])
		if not 1 <= difference <= 3:
			return False

	return True

def main():
	with open("input.txt") as f:
		lines = f.readlines()
		lines = [list(map(int, line.split())) for line in lines]

	safeCount = 0

	for levels in lines:
		safeCount += checkReport(levels)

	print(f"Part 1: {safeCount}")

if __name__ == "__main__":
	main()
