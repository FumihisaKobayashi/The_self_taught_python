#スタック　出したものを後ろから入れる。
#pop スタックから要素を削除すること。
#push スタックに要素を追加

class Stack:
    def __init__(self):
        self.items = []
    #スタックが空のときTRUEを返す中に要素がある時ファlsえを返す。
    def is_empty(self):
        return self.items == []
    #要素を削除して返す。
    def push(self, item):
        self.items.append(item)
    #スタックの一番上を返すが削除しない。
    def pop(self):
        return self.items.pop()
    #スタックの中の要素数を整数で返す。
    def peek(self):
        last = len(self.tems) - 1
        return self.items[last]

    def size(self):
        return len(self.items)
