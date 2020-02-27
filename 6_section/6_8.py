
#.join() 全ての文字列の間に新しい文字列
first_three = "abc"
result = "+".join(first_three)

print(result)

#空白文字で隙間作成。
words = ["The", "Fox", "Jamped",
    "over", "the", "fence", "."]
one = " ".join(words)

print(one)

#空白除去.strip()
s = "    The    "
s = s.strip()

print(s)
