x = int(input())
for _ in range(0,x):
    n,m = map(int,(input().split()))
    if n>m:
        print(n-m)
    else:
        print(0)
