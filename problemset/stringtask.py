# Solves http://codeforces.com/problemset/problem/118/A
print(''.join('.{}'.format(c) for c in [char for char in str(input()).lower() if char not in 'aeiouy']))
