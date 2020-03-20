
#class Dataは整数のリストをnumsに持っている
class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
    
    def change_data(self, index, n):
        self.nums[index] = n
#Dataのインスタンス（中身）numを変更する。

#change_dataを使う方法
data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

#インスタンス変数をそのまま変更する方法。
data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)
