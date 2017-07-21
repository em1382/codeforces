# Solves http://codeforces.com/problemset/problem/520/A
n = int(input())
word = str(input()).lower()
if set(word) == set(list('abcdefghijklmnopqrstuvwxyz')):
    print('YES')
else:
    print('NO')
