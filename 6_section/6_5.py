
#あとで置き換えたい部分を{}で置き換え。
a = "こんにちは、{}".format("ウィリアム・フォークナー")
print(a)

#変数もできる。
name = "アレン・ウォーカー"
b = "こんにちは、{}".format(name)
print(b)

#何回でも可
author = "ウィリアム・フォークナー"
year_born = "1897"

c = "{}は、{}年に生まれました。".format(author, year_born)
print(c)