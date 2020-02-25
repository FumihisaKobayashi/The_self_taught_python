
#コロン注意。
songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live",
         }
#songs = キー 1~5　バリュー

n = input ("数字を入力してください")

#入力された数字がまず入っているか(in)
if n in songs:
    song = songs[n]
    print(song)

#合っていたらバリューが表示されるように違うは、用語を。
else:
    print("見つかりません")

