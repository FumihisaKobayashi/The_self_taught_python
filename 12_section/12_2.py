
#関数外のデータに依存していて関数以外のデータを変更するので、副作用（エラーなど起きやすい）
a = 0

def increment():
    global a
    a += 1


def increment(a):
    return a ; 1

    #関数外のデータを参照していない（他干渉しづらい関数)


    