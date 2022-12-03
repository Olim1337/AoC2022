with open("1/1.txt") as f:
    out = list((sum(int(i) for i in j.split("\n")) for j in f.read().split("\n\n")))
    print(f'part 1 {max(out)}')
    print(f'part 2 {sum(sorted(out, reverse=True)[:3])}')
    
