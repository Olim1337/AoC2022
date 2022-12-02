# Rock A,X 1 Paper B,Y 2 Scissors C,Z 3
strategy1 = {
    "A Y" : 8,
    "A X" : 4,
    "A Z" : 3,
    "B Y" : 5,
    "B X" : 1,
    "B Z" : 9,
    "C Y" : 2,
    "C X" : 7,
    "C Z" : 6,
    "": 0
}

strategy2 = {
    "A Y" : 4, 
    "A X" : 3,
    "A Z" : 8, 
    "B Y" : 5, 
    "B X" : 1, 
    "B Z" : 9, 
    "C Y" : 6, 
    "C X" : 2, 
    "C Z" : 7,
    "": 0
}

with open ("2/2.txt") as f:
    score1 = score2 = 0
    for i in f.read().split("\n"):
        score1 += strategy1[i]
        score2 += strategy2[i]

print(score1)
print(score2)
        
