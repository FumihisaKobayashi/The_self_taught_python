#オブジェクト作成後は、インスタンス変数の値を取得。
#オブジェクト名.[インスタンス定数]
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")


or1 = Orange(10, "dark orange")
print(or1.weight)
print(or1.color)