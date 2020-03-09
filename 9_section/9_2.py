#モード
# "r"はファイル読み取り専用
# "w"はファイル書き出し専用
# "w+"は、読み書き両方できるようにファイルを開く


#open関数使ってファイル開いた後、open関数の戻り値をstに代入して書き込み。最後にcloseでファイル閉じる。

#writeメソッドを使ってファイル書き込み
st = open("st.txt", "w")
st.write("HI from Python!")
st.close()