

pop = []  #洋楽を保存するリスト
jpop = [] #Jpopを保存するリスト

#関数の作成
def collect_songs():
    song = "曲名を入れてください:"
    ask = "p か j のどちらかを入力して下さい。qで終わります:"

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "p":
            p = input(song)
            pop.append(p)

        elif genre == "j":
            j = input(song)
            jpop.append(j)

        else:
            print("不正な数値です")
        
        print("pop songs: ", pop)
        print("jpop songs: ", jpop)


collect_songs()

#.append()リスト追加！！忘れない