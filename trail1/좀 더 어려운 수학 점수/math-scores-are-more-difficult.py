A_math, A_eng = list(map(int, input().split()))
B_math, B_eng = list(map(int, input().split()))

if A_math > B_math: print('A')
if B_math > A_math: print('B')
elif A_math == B_math: 
    if A_eng > B_eng: print('A')
    elif A_eng < B_eng: print('B')