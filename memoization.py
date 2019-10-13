import numpy as np

CARDS = [1, 3, 1, 7, 8, 9, 4]
LEN_CARDS = len(CARDS)
SIS_FIRST = False
cache = [[0]*LEN_CARDS for _ in range(LEN_CARDS)]

def getScores(i, j, sisterFirst):
    if (cache[i][j] != 0): return cache[i][j]
    if (i==j): return (CARDS[i], 0)

    if (sisterFirst):
        # Sister takes the local optimum
        if (CARDS[i] > CARDS[j]):
            scoreTuple = getScores(i+1, j, not sisterFirst)
            firstScore  = CARDS[i] + scoreTuple[1]
            secondScore = scoreTuple[0]
        else:
            scoreTuple = getScores(i, j-1, not sisterFirst)
            firstScore  = CARDS[j] + scoreTuple[1]
            secondScore = scoreTuple[0]
    else:
        leftCutScore = getScores(i+1, j, not sisterFirst)
        rightCutScore = getScores(i, j-1, not sisterFirst)

        # Strategist takes the global optimum
        if (CARDS[i] + leftCutScore[1] > CARDS[j] + rightCutScore[1]):
            firstScore = CARDS[i] + leftCutScore[1]
            secondScore = leftCutScore[0]
        else:
            firstScore = CARDS[j] + rightCutScore[1]
            secondScore = rightCutScore[0]
    
    cache[i][j] = (firstScore, secondScore)
    return cache[i][j]

def pad(obj):
    print(str(obj).ljust(10, ' '), end="&")

def main():
    scoresOpt = getScores(0, LEN_CARDS - 1, SIS_FIRST)
    print("Scores for list : " + str(CARDS) + ":\n")
    if (SIS_FIRST):
        print("Brother : {} - Sister : {}".format(scoresOpt[1], scoresOpt[0]))
    else:
        print("Brother : {} - Sister : {}".format(scoresOpt[0], scoresOpt[1]))

    print("Resulting table :\n")

    for row in cache:
        [pad(node) if node != 0 else pad("0") for node in row]
        print("\\\\")

main()