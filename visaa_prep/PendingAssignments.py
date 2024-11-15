O, P, Q = map(int, input().split())
total_minutes = 2 * 24 * 60
required_minutes = O * P
if required_minutes <= total_minutes:
    print("YES")
else:
    print("NO")
