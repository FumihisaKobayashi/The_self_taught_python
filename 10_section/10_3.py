if not win:
    print("\n".join(stages[0:wrong+1]))
    print("あなたの負け！正解は{}.".format(word))

#ループ終了時にwin がFALSEの場合は、全て表記