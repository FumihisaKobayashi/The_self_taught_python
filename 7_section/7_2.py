
#forループで辞書のキー要素として繰り返し
people = {"G. Bluth II": "A. Development",
          "Barney": "HIMYM",
          "Denis": "Always Sunny",
          }

for character in people:
    print(character)


#リストインデックス変数持たせる。
tv = ["GOT", "Narcos", "Vice"]

i = 0
#newで代入し、.upper()で代入最後にiと次のループを使う変数揃える。
for show in tv:
    new =tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)
