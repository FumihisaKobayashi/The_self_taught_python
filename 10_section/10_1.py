

#ハングマンの関数作成し、wordの引数受け取り
def hangman(word):
    wrong = 0
    stages = ["",
              "______     ",
              "|          ",
              "|     |    ",
              "|     O    ",
              "|    /|\   ",
              "|    / \   ",
              "|          "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")

#wrong　何回間違えたかを数える
#stages 文字列のりすと
#変数rlettersはwordの文字を一文字ずつ要素に分解してリストにしたもの

#変数board ヒントの記録  ["_"] * len(word)は、wordの中の文字の数に"_"入れる
