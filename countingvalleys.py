# HackerRank practice Counting Valleys

def countingValleys(n,s):
    
    sea_level = 0
    valleys = 0

    for steps in s:
        if steps == "U":
            sea_level += 1
            if sea_level == 0:
                valleys += 1
        else:
            sea_level -= 1
        return valleys