a1, b1 = input().split()
b1 = int(b1)
a2, b2 = input().split()
b2 = int(b2)
a3, b3 = input().split()
b3 = int(b3)

if a1 == 'Y' and b1 >= 37:
    if (a2 == 'Y' and b2 >= 37) or (a3 == 'Y' and b3 >= 37):
        print('E')
    else: print('N')

else: 
    if (a2 == 'Y' and b2 >= 37) and (a3 == 'Y' and b3 >= 37):
        print('E')
    else: print('N')