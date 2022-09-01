t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    if n%h == 0:
        yy = n
        xx = int(n/h)
    else:
        yy = n%h
        xx = int(n/h) +1 

    if xx < 10:
        xx = "0"+str(xx)

    print(str(yy) + xx)