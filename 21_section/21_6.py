#スタックには、入れた順番と逆順で取り出される性質がある。

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.tems) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


#文字列’HELLO’を１文字ずつループpush()に入れていく
stack = Stack()
for c in "Hello":
    stack.push(c)
#スタックの要素がある間ループして1文字ずつ取り出してreverse変数に書き足し
reverse = ""

#繰り返し処理終わると、順番が逆になり、OLLEHになる。
while stack.size():
    reverse += stack.pop()


print(reverse)
