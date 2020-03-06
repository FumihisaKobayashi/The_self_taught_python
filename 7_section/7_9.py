for i in range(1,6):
    if i == 3:
        continue
    print(i)

#１〜５の数字を入力したいが３を省きたい。


#iが３の時continueで続きは表記されないwhileループとの組み合わせ。
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1