stacks = [[]]*9
with open("5/5.txt") as f:
    for i in f.read().split("\n")[:8]:
        print([j for j in i])

print(stacks)
