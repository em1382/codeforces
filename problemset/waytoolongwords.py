# Solves http://codeforces.com/problemset/problem/71/A
words = int(input())
for i in range(words):
    word = str(input())
    if len(word) > 10:
        word = word[0] + str(len(word) - 2) + word[-1]
    print(word)
