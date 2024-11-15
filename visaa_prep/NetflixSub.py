X, Y, Z, m = map(int, input().split())

if X + Y >= m or X + Z >= m or Y + Z >= m:
    print("YES")
else:
    print("NO")
