import datetime

import pandas as pd
from langdetect import detect

def is_english (text:str) :
    try:
        return detect(text) == 'en'
    except:
        return False


df_message = pd.read_csv('iron_march/message_posts_edited_english.csv', header=0)
'''
df_message.msg_post.replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
df_message["msg_date"] = df_message["msg_date"].apply(lambda x: pd.to_datetime(int(x), utc=True, unit='s'))
df_message = df_message[(df_message['msg_date'] > "2015-06-16")]
df_message = df_message.loc[(df_message["msg_post"].str.len() > 120) & (df_message["msg_post"].str.len() < 5000 ) ]
df_message = df_message[df_message["msg_post"].apply(is_english)]
df_message.to_csv('iron_march/message_posts_edited_english.csv')

print(df_message[df_message.columns[0]].count())
print(df_message['msg_date'].max())
print(df_message['msg_date'].min())

'''

df_posts = pd.read_csv('iron_march/forums_posts_edited_english.csv', header=0)
#df_posts.post.replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
'''
df_posts["post_date"] = df_posts["post_date"].apply(lambda x: pd.to_datetime(int(x), utc=True, unit='s'))
df_posts = df_posts[(df_posts['post_date'] > "2015-06-16")]
df_posts = df_posts.loc[(df_posts["post"].str.len() > 120) & (df_posts["post"].str.len() < 5000 ) ]
df_posts = df_posts[df_posts["post"].apply(is_english)]
df_posts.to_csv('iron_march/forums_posts_edited_english.csv')

#print(df_posts[df_posts.columns[0]].count())
df_posts["Indexes"] = df_posts['post'].str.find('boycot')
print(df_posts.loc[:,["post_date","post"]])
#print(df_posts['post_date'].max())
#print(df_posts['post_date'].min())
#print(df_posts.loc[:,["post_date","post"]])
'''