import math
a, b, v = map(int, input().split())
x = math.ceil((v-b)/(a-b))
print(x)