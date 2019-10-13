CARDS = [1, 3, 1, 7, 8, 9, 4]
LEN_CARDS = len(CARDS)
CALL_NUMBER = 0

def getScores(i, j, sisterFirst):
    global CALL_NUMBER
    CALL_NUMBER += 1
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
    
    return (firstScore, secondScore)

def main():
    scoresOpt = getScores(0, LEN_CARDS - 1, False)
    print("Scores for list : " + str(CARDS) + ":\n")
    print("Brother : {} - Sister : {}".format(scoresOpt[0], scoresOpt[1]))
    print("Number of calls : {}".format(CALL_NUMBER))

main()