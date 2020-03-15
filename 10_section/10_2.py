
#stagesを１マイナスはstagesは０からだが、wrongは１からのため
while wrong < len(stages) - 1:
    print("\n")
    msg = "一文字を予想してね"
    #input使って変数charに割り当て
    char = input(msg)
    #input使って入力された数値をcharに割り当て
    if char in rletters:
        cind = rletters.index(char)
        board[cind] = char
        rletters[cind] = '$'
        #複数同じ文字あると正しく動作しないので、正解したものを＄に書き換え
    else:
        wrong += 1

    print(" ".join(stages[0:e]))
    if "_" not in board:
        print("あなたの勝ち！")
        print(" ".join(board))
        win = True
        break

