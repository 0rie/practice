# csvモジュールを使ってCSVファイルから1行ずつ読み込む
import csv

filename = 'messages2.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)
# 出力結果：
#['年', '地域コード', '地域', '総人口']
#['1920年', '00000', '全国', '55963053']
# …… 省略 ……
#['2010年', '00000', '全国', '128057352']
#['2020年', '00000', '全国', '126226568']

'''
# タブ区切りの文字を読み込む
filename = 'tabdelimiteddata.tsv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f, delimiter='\t')
    for row in csvreader:
        print(row)  # 出力結果は省略

# CSVファイルの内容を1つのリストにまとめる
filename = 'populationdata.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader]  # 各年のデータを要素とするリスト
    #content = []
    #for row in csvreader:
    #    content.append(row)

print(content)
# 出力結果：
#[['年', '地域コード', '地域', '総人口'], ['1920年', '00000', '全国',
# '55963053'], …… , ['2010年', '00000', '全国', '128057352'], ['2020年',
# '00000', '全国', '126226568']]

# 特定の列のデータ型を変換する
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)  # 見出し行は別扱い
    content = [[row[0], row[1], row[2], int(row[3])] for row in csvreader]

content.insert(0, header)  # 最後にリストの先頭に見出し行を挿入
print(content)
# 出力結果：
#[['年', '地域コード', '地域', '総人口'], ['1920年', '00000', '全国',
# 55963053], …… , ['2010年', '00000', '全国', 128057352], ['2020年',
# '00000', '全国', 126226568]]

# 数値フィールド以外はシングルクオートで囲まれていることを指示して
# 数値フィールドの値を全て浮動小数点数値に自動的に変換
filename = 'sample.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f, quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
    for row in csvreader:
        print(row) 
# 出力結果
# ['年', '地域コード', '地域', '総人口']
# ['1920年', '00000', '全国', 55963053.0]
# …… 省略 ……
# ['2010年', '00000', '全国', 128057352.0]
# ['2020年', '00000', '全国', 126226568.0]

# CSVファイルの内容から辞書形式のデータを作成
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.DictReader(f)
    content = [row for row in csvreader]

print(content[0])
# 出力結果：
#{'年': '1920年', '地域コード': '00000', '地域': '全国', '総人口': '55963053'}
'''