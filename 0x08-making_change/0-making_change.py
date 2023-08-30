#!/usr/bin/python3
"""
change comes from within
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    zoo = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            zoo[i] = min(zoo[i], zoo[i - coin] + 1)
    return zoo[-1] if zoo[-1] != float("inf") else -1