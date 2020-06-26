#新しい要素を追加
fruit = ["Apple", "Orange", "Pear"]
fruit.append("Banana")
fruit.append("Peach")

print(fruit)

#appendで新しい要素追加
random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")

print(random)
#いろんな物ができる。


colors = ["blue", "green", "yellow"]
colors
#何も指定しなかったら、一番後ろが削除される。
item = colors.pop()
#.pop()の中インデックス指定すると、指定番号削除
item
print(colors)
