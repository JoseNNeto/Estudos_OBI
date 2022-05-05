c1, c2, c3, c4, c5 = input().split(' ')
c1 = int(c1)
c2 = int(c2)
c3 = int(c3)
c4 = int(c4)
c5 = int(c5)
if c1 < c2 < c3 < c4 < c5:
    print('C')
elif c1 > c2 > c3 > c4 > c5:
    print('D')
else:
    print('N')
