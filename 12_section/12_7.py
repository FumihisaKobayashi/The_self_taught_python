#インスタンス変数の値を変更する。


class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

#[オブジェクト名].[インスタンス変数] = [新しい値]
or1 = Orange(10, "dark orange")
or1.weight = 100
or1.color = "light orange"


print(or1.weight)
print(or1.color)