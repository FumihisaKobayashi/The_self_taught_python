

tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Develpment", "friends", "Always sunny"]
all_shows = []

#３つのリストの要素を順番に.upper()で大文字にしてからリスト(all_shows)に追加
for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

#出力に対して、all_showsを指定して、全て大文字から格納。
print(all_shows)