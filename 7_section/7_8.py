
#ループの中でリストqsの質問の繰り返し。
qs  = ["What is your name?",
       "What is your fav. color?",
       "What is your quest?"]

#ループの中で(n + 1) % 3の評価をnに当てている。
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3

#次のループは、(0+1) % 3で１の結果に。
#その次は(1+1)%3で２が出る。左の値が小さいから肥大の値で表記される。
#３つ目は0になるので戻る。