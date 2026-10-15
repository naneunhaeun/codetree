f_age, f_gender = input().split()
s_age, s_gender = input().split()

f_age = int(f_age)
s_age = int(s_age)

if (f_age >= 19 and f_gender == 'M') or (s_age >= 19 and s_gender == 'M'):
    print(1)
else:
    print(0)