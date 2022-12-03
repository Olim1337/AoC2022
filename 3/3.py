alphabet = 'abcdefghijklmnopqrstuvwxyz'
X = {letter: index for index, letter in enumerate(alphabet + alphabet.upper(), start=1)}

# part 1
with open("3/3.txt") as f:
    total = 0
    for item in f.read().split("\n"):
        item1, item2 = [i for i in item[:len(item)//2]], [i for i in item[len(item)//2:]]
        letter = set(item1).intersection(item2).pop()
        prio = X.get(letter)
        total += prio
print(total)

# part 2
with open("3/3.txt") as f:
    total = 0
    itemList = f.read().split("\n")
    for i in range(0, 300, 3):
        items = itemList[i:i+3]
        letter = set(items[0]).intersection(items[1]).intersection(items[2]).pop()
        prio = X.get(letter)
        total += prio
print(total)