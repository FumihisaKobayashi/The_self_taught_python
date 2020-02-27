
#.index() インデックス値表示
a = "animals".index("m")
print(a)

#わからない時は、例外が発生する前提で例外処理しておく
try:
    "animals".index("z")
except:
    print("Not found")
