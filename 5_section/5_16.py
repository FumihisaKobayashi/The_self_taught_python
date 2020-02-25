#リストだからこれ[]
lists = []


rap = ["カニエ・ウェスト", "ジェイ・Z", "エミネム", "ナス"]
rocks = ["ボブ・ディラン", "ビートルズ", "レッド・ツェッペリン"]
djs = ["ゼッズ・デッド", "テイエスト"]


lists.append(rap)
lists.append(rocks)
lists.append(djs)


#新しい要素を追加すると、リストも更新される。
rap = lists[0]
rap.append("ケンドリック・ラマー")
print(rap)
print(lists)
