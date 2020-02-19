
#必須引数とオプション引数
def f(x = 2):
    return x ** x

print(f())
print(f(4))

#必須からOPの方に。,で複数。

def add_it(x, y = 10):
    return x + y

result = add_it(2)
print(result)