def f(str):
    try:
        return float(str)
    
    except ValueError:
        print("Not")

f = (12.56)
print(f)
#正解下

def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c)