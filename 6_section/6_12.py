
#ダブル(シングル)クォートが重なる時は、\ \(エスケープ文字)で対応。
a = "彼女は、\"そうだね\"と言った。"

b = '彼は、\'そうだね\'と言った。'

#ダブルとシングルがべつであればエスケープ文字は不要。
c = "あの人は、'そうすべきだ'と言った。"


print(a, b, c)
