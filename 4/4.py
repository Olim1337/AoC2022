with open ("4/4.txt") as f:
    part1 = part2 = 0
    for row in f.read().split("\n")[:-1]:
        range1, range2 = [i.split('-') for i in row.split(',')] 
        range1, range2 = range(int(range1[0]), int(range1[1])+1), range(int(range2[0]), int(range2[1])+1)
        if (all(i in range1 for i in range2) or all(i in range2 for i in range1)):
            part1 +=1
        if (any(i in range1 for i in range2)):
            part2 +=1

print(f'Part 1: {part1}, Part 2: {part2}')
