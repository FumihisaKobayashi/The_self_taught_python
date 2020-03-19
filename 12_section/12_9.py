#Orangeオブジェクトに腐る性質を追加

class Orange:
    def __init__(self, w, c):
        """weight(重さ)はグラム"""
        self.wight = w
        self.color = c
        self.mold = 0
        print("Created!")
    
    def rot(self, days, temp):
        """temp(温度)は摂氏"""
        self.mold = days * temp

orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)

#rot　オレンジを買ってからの日付と、その期間の平均温度の２つを引数にする。
#２つの引数からインスタンス変数（MOLD）を計算して代入する。