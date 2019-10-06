#!/usr/bin/env python3
from random import randint
from collections import deque

def pile_of_cards(n):
    """
    Returns a deque with a pile of n cards
    Cards are represented by their value (ranging from 2 to 14)
    """
    liste = [randint(2,14) for k in range(n)]
    return deque(liste)


def play_greedy(isSisterFirst, cards):
    """
    Returns who won by comparing sister's sum and mine
    Both of us plays greedy
    """
    sum_sister, my_sum = 0, 0
    if isSisterFirst:
        while cards != deque([]):
            # Sister's turn
            if cards[0] > cards[-1]:
                sum_sister += cards[0]
                cards.popleft()
            else:
                sum_sister += cards[-1]
                cards.pop()
            # Brother's turn
            if cards[0] > cards[-1]:
                my_sum += cards[0]
                cards.popleft()
            else:
                my_sum += cards[-1]
                cards.pop()
    else:
        while cards != deque([]):
            # Brother's turn
            if cards[0] > cards[-1]:
                my_sum += cards[0]
                cards.popleft()
            else:
                my_sum += cards[-1]
                cards.pop()

            # Sister's turn
            if cards[0] > cards[-1]:
                sum_sister += cards[0]
                cards.popleft()
            else:
                sum_sister += cards[-1]
                cards.pop()

    if sum_sister > my_sum:
        # print("Little sister won !")
        return(0)
    elif sum_sister == my_sum:
        # print("It's a draw !")
        return(0)
    else:
        # print("I won !")
        return(1)

succes = 0
for k in range(100):
    tas = pile_of_cards(8)
    if play_greedy(False, tas):
        succes += 1
print(succes/100)

def play_complete(isSisterFirst, cards):
    """
    Checks all possible ways of winning then making a choice
    Complete solution space method is in O(2^n) so we can't implement it
    """
    cards_copie = cards
    sum_sister, my_sum, DontChangeStrategy = 0, 0, True
    if isSisterFirst:
        while DontChangeStrategy:
            cards = cards_copie
            while cards != deque([]):
                # Sister's turn
                if cards[0] > cards[-1]:
                    sum_sister += cards[0]
                    cards.popleft()
                else:
                    sum_sister += cards[-1]
                    cards.pop()
                # Brother's turn
                choice = randint(0,1)
                if choice:
                    my_sum += cards[-1]
                    cards.pop()
                else:
                    my_sum += cards[0]
                    cards.popleft()
            if my_sum > sum_sister:
                return(1)


succes = 0
for k in range(10):
    tas = pile_of_cards(8)
    if play_complete(True, tas):
        succes += 1
print(succes/10)
