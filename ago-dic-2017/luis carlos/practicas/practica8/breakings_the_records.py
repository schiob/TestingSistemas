import sys

def getRecord(s):
    maxs = s[0]
    mins = s[0]
    max_count = 0
    min_count = 0
    if len(s) > 1:
        for val in s[1:]:
            if val > maxs:
                max_count += 1
                maxs = val
            if val < mins:
                min_count += 1
                mins = val
    return (max_count, min_count)

if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().strip().split(' ')))
    result = getRecord(s)
    print (" ".join(map(str, result)))
