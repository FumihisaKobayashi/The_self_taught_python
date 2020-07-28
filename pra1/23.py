def if_test(num):
    if num > 100:
        print('100 < num')
    elif num > 50:
        print('50 < num <= 100')
    elif num > 0:
        print('0 < num <= 50')
    elif num == 0:
        print('num == 0')
    else:
        print('num < 0')

if_test(1000)
# 100 < num

if_test(70)
# 50 < num <= 100

if_test(0)
# num == 0

if_test(-100)
# num < 0