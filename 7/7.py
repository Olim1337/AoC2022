from collections import defaultdict

with open("7/7.txt") as f:
    sizes = defaultdict(int)
    path = []
    for row in f.read().split("\n"):
        commands = row.split(" ")
        if commands[0] == "$" and commands[1] == "cd":
            dir = commands[2]
            if dir == "/":
                path.append("/")
            elif dir == "..":
                path.pop()
            else:
                path.append(f"{path[-1]}{'/'}{dir}")
        if commands[0].isnumeric():
            for p in path:
                sizes[p] += int(commands[0])

# Part 1
print(sum(i for i in sizes.values() if i <= 100000))

# Part 2
spaceRemaining = 70000000 - sizes['/']
print(min(i for i in sizes.values() if i >= (30000000 - spaceRemaining)))