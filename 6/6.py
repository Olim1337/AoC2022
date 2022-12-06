def day6(n):
    with open("6/6.txt") as f:
        puzzle = [i for i in f.read()]
        for i, j in enumerate(puzzle):
            code = set(puzzle[i:i+n])
            if len(code) == n:
                return i+n

print(f"Part 1: {day6(4)}")
print(f"Part 2: {day6(14)}")
