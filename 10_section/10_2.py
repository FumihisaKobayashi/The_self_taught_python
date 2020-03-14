

while wrong < len(stages) - 1:
    print("\n")
    msg = "一文字を予想してね"
    #input使って変数charに割り当て
    char = input(msg)
    if char in rletters:
        cind = rletters.index(char)
        board[cind] = char
        rletters[cind] = '$'
    else:
        wrong += 1

    print(" ".join(stages[0:e]))
    if "_" not in board:
        print("あなたの勝ち！")
        print(" ".join(board))
        win = True
        break

