from collections import defaultdict, deque
stacks = defaultdict(deque)

# Part 1
with open("5/5.txt") as f:
    puzzle = f.read().split("\n")
    # parsing stack of crates
    for i in puzzle[:8]:
        row = [i[j] for j in range(1, len(i), 4)]
        for i, j in enumerate(row):
                stacks[i+1].appendleft(j) if j != ' ' else None

    # instructions
    for row in puzzle[10:]:
        n, f, t = [int(row.split(' ')[i]) for i in range(1,6,2)]
        for _ in range(n):
            stacks[t].append(stacks[f].pop())

    part1 = ''.join([v[-1] for k,v in sorted(stacks.items())])
    print(f"Part 1: {part1}")

# Part 2
stacks = defaultdict(deque)
with open("5/5.txt") as f:
    puzzle = f.read().split("\n")
    # parsing stack of crates
    for i in puzzle[:8]:
        row = [i[j] for j in range(1, len(i), 4)]
        for i, j in enumerate(row):
                stacks[i+1].appendleft(j) if j != ' ' else None

    # instructions
    for row in puzzle[10:]:
        n, f, t = [int(row.split(' ')[i]) for i in range(1,6,2)]
        temp = deque()
        for _ in range(n):
            temp.append(stacks[f].pop())
        [stacks[t].append(i) for i in reversed(temp)]

    part2 = ''.join([v[-1] for k,v in sorted(stacks.items())])
    print(f"Part 2: {part2}")