num = [1, 2, 3, 5, 7, 11]

while True:
    a = input("数字を入力するか、'q'で終了します")
    if a == "q":
        break
    #ここの三行は答えから、（例外処理）
    try:
        a = int(a)
    except ValueError:
        print("please type a number or q to quit.")
    if a in num:
        print("素数です")
    else:
        print("素数(小さい値)ではないです。")

    