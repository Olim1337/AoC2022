#part 1
with open ("4/4.txt") as f:
    total = 0
    rows = f.read().split("\n")[:-1]
    for row in rows:
        range1 = row.split(',')[0].split('-')
        range2 = row.split(',')[1].split('-')
        range1, range2 = [*range(int(range1[0]), int(range1[1])+1)], [*range(int(range2[0]), int(range2[1])+1)]
        if range1 and range2 and (all(i in range1 for i in range2) or all(i in range2 for i in range1)):
            total +=1
    print(total)

#part 2
with open ("4/4.txt") as f:
    total = 0
    rows = f.read().split("\n")[:-1]
    for row in rows:
        range1 = row.split(',')[0].split('-')
        range2 = row.split(',')[1].split('-')
        range1, range2 = [*range(int(range1[0]), int(range1[1])+1)], [*range(int(range2[0]), int(range2[1])+1)]
        if range1 and range2 and (any(i in range1 for i in range2)):
            total +=1
    print(total)
