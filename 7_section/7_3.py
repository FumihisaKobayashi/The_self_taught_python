#tvを繰り返す代わりに、TVをenumerte関数で繰り返し

tv = ["GOT", "Narcos", "Vice"]
#インデックス血を受け取るiを追加。
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)
