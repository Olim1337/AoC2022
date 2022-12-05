from collections import defaultdict, deque
from copy import deepcopy
stacks = defaultdict(deque)

with open("5/5.txt") as f:
    puzzle = f.read().split("\n")
    # parsing stack of crates
    for i in puzzle[:8]:
        row = [i[j] for j in range(1, len(i), 4)]
        for i, j in enumerate(row):
                stacks[i+1].appendleft(j) if j != ' ' else None

    stacks1, stacks2 = stacks, deepcopy(stacks)

    for row in puzzle[10:]:
        n, f, t = [int(row.split(' ')[i]) for i in range(1,6,2)]
        temp = deque()
        for _ in range(n):
            stacks1[t].append(stacks1[f].pop())
            temp.append(stacks2[f].pop())
        [stacks2[t].append(i) for i in reversed(temp)]

    part1 = ''.join([v[-1] for k,v in sorted(stacks1.items())])
    print(f"Part 1: {part1}")        

    part2 = ''.join([v[-1] for k,v in sorted(stacks2.items())])
    print(f"Part 2: {part2}")