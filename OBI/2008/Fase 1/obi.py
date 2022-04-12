n, p = input().split(' ')
n = int(n)
p = int(p)
cont = 0
for c in range(0, n):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    if x + y >= p:
        cont += 1

print(cont)