
#re = regular expression:定規表現
import re
l = "Beautiful is better than ungly."
matches = re.findall("Beautiful", l)
#検索対象のテキストを渡すと一致したすべてを返す。
print(matches)