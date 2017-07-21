# Solves http://codeforces.com/problemset/problem/158/A
n, k = (int(x) for x in input().split())
scores = [int(s) for s in input().split()]
if scores[0] == 0:
    print(0)
else:
    passing = 0
    last_score = None
    for score in scores:
        if (score > 0 and k > 0) or last_score == score:
            passing += 1
            k -= 1
            last_score = score
        else:
            break
    print(passing)
