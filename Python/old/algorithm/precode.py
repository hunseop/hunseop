N, X = map(int, input().split())
result = []

A = list(map(int, input().split()))

for i in A:
    if ( i < X ):
        result.append(i)

