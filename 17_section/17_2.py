import re

l = "Beautiful is better than ungly."
matches = re.findall("Beautiful", l, re.IGNORECASE)

#大文字小文字の違いを無視して検索したい場合はfindall関数めの３つ目にre.IGNORECASEフラグ
print(matches)