print("line1\nline2\nline3")
#\nで改行して表記。

#インデックス値リストでスライス。(切り抜き)
fict = ["トイ", "ストーリー", "マニア",
        "ランキング"]
print(fict[0:3])

#0から始める時は：で簡略。終了までのインデックスは最後に[：]
iva = "死の代わりにひとつの光があった。"
print(iva[:6])
print(iva[6:])

#前後を簡略化すると、全文コピー。
print(iva[:])