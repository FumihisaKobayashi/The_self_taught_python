st = open("st.txt", "w", encoding="utf-8")
st.write("Pythonからこんにちは")
st.close()


#encoding引数はファイルの文字コードを指定。
#日本語などの非アスキー文字はそのまま✖︎　utf-8は、変換方式の一つ。