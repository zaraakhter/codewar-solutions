from collections import Counter

def stray(arr):
    counter = Counter(arr)
    return min(counter, key=counter.get)