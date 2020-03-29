#スタック　出したものを後ろから入れる。
#pop スタックから要素を削除すること。
#push スタックに要素を追加

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

#LIFO(ラストイン・ファーストアウト)