
# coding: utf-8

# In[126]:


import MeCab
import sys
import re
from collections import Counter


# In[127]:


import glob
import numpy as np
import csv
import pprint


# In[128]:


tagger= MeCab.Tagger()


# In[129]:


file_text = [] #テキストファイル名を格納するリスト型変数
#muliti files
for file in glob.glob('./input/*.txt'): #Pythonソースと同じディレクトリの「test」フォルダにあるテキストファイルが対象
    #file_name.append(os.path.basename(file)) #ファイルパスからファイル名のみ抽出
    file_data = open(file,'r',encoding='utf-8-sig') 
    bindata = file_data.read()
    parse_data = tagger.parse(bindata)
    lines = parse_data.split('\n')
    items = (re.split('[\t,]', line) for line in lines)
    # 名詞をリストに格納
    words = [item[0]
             for item in items
             if (item[0] not in ('EOS', '', 't', 'ー') and
                 item[1] == '名詞' and item[2] == '一般')]
    file_text.extend(words) 


# In[130]:


# 抽出テキスト
#print(file_text)


# In[131]:


# 頻度順に出力
# Ref: https://note.nkmk.me/python-collections-counter/
counter = Counter(file_text)
count_file = []
for word, count in counter.most_common(100):
    count_file.append(word)
    print(f"{word}: {count}")


# In[132]:


# CSVファイルを作成
with open('./output/word_count.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(count_file)


# In[133]:


with open('./output/word_count.csv') as f:
    print(f.read())

