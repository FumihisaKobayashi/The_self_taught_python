
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


#スタックの一番上の要素を覗き見（peek）を確認してサイズの確認。
stack = Stack()

for i in range(0, 6):
    stack.push(i)

print(stack.peek())
print(stack.size())

