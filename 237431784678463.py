N = int(input())
S = k = 0
S = N // 10 + N % 10
if S % 2 == 1:
    k = 1
else:
    k = 0
print(k)