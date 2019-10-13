import numpy as np

CARDS = [14, 6, 9, 7, 3, 11, 13, 5, 7, 2]
LEN_CARDS = len(CARDS)
SIS_FIRST = False
cache = [[0]*LEN_CARDS for _ in range(LEN_CARDS)]

# Finding which player is first on diagonal of index
# diag_index
def isSisterFirst(diag_index, sisterFirst):
    if ((diag_index + LEN_CARDS)%2 == 1):
        return sisterFirst
    else:
        return not sisterFirst


def updateCell(coord, sisterFirst):
    i,j = coord
    if (sisterFirst):
        # Sister takes the local optimum
        if (CARDS[i] > CARDS[j]):
            firstScore  = CARDS[i] + cache[i+1][j][1]
            secondScore = cache[i+1][j][0]
        else:
            firstScore  = CARDS[j] + cache[i][j-1][1]
            secondScore = cache[i][j-1][0]
    else:
        # Strategist takes the global optimum
        if (CARDS[i] + cache[i+1][j][1] > CARDS[j] + cache[i][j-1][1]):
            firstScore = CARDS[i] + cache[i+1][j][1]
            secondScore = cache[i+1][j][0]
        else:
            firstScore = CARDS[j] + cache[i][j-1][1]
            secondScore = cache[i][j-1][0]
    
    cache[i][j] = (firstScore, secondScore)


def getScores(i, j, sisterFirst):
    if (i==j): return (CARDS[i], 0)

    # Initializing the diagonal
    for k in range(LEN_CARDS):
        cache[k][k] = (CARDS[k], 0)

    # Computing cache values, starting from the diagonal
    for diag_index in range(1, LEN_CARDS):
        sisterFirstDiag = isSisterFirst(diag_index, sisterFirst)

        # Updating all cells in the diagonal
        it_coord = [0, diag_index]
        for _ in range(LEN_CARDS - diag_index):
            updateCell(it_coord, sisterFirstDiag)
            it_coord = [x+1 for x in it_coord]

    return cache[0][LEN_CARDS-1]

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