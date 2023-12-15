import pandas as pd
from langdetect import detect

def is_english (text:str) :
    try:
        return detect(text) == 'en'
    except:
        return False

df = pd.read_csv('stormfront/cleanposts_after_iron_english.csv', header=0)
#df = df[(df['posteddate'] > "2017-11-21")]
#df = df[df["cleanmessage"].apply(is_english)]
#df = df.loc[(df["cleanmessage"].str.len() > 120) & (df["cleanmessage"].str.len() < 5000 ) ]

#df.to_csv('stormfront/cleanposts_after_iron_english.csv')
# 400283
print(df[df.columns[0]].count())
print(df.loc[:,["posteddate","cleanmessage"]])