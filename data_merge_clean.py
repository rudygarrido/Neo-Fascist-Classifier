import pandas as pd


df_posts_iron = pd.read_csv('iron_march/forums_posts_edited_english.csv', header=0)
df_posts_iron = df_posts_iron.reindex(["post","post_date"], axis=1)
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'\n> ', '', regex=True )
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'On (([A-Za-z0-9]+(/[A-Za-z0-9]+)+)|([0-9]+(\.[0-9]+)+)|([0-9]+(\-[0-9]+)+)|([0-9]+(\.\s[0-9]+)+))(.)?(\sг\.)? at (\d)?\d:\d\d (PM|AM),(.*?)said:', 'Another user said:', regex=True )
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'Just now,\s(.*?)said:', 'Another user said:', regex=True )
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'[0-9]+\s[A-Za-z]+\sago,(.*?)said:', 'Another user said:', regex=True )
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'On\s[0-9]+\s[A-Za-z]+\s[0-9]+\sat\s(\d)?\d:\d\d\s(PM|AM),\s(.*?)said:', 'Another user said:', regex=True )
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'On\s[A-Za-z]+\s[0-9]+,\s[0-9]+\sat\s(\d)?\d:\d\d\s(PM|AM),\s(.*?)said:', 'Another user said:', regex=True )
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'On\s[A-Za-z]+,\s[A-Za-z]+\s[0-9]+,\s[0-9]+\sat\s(\d)?\d:\d\d\s(PM|AM),\s(.*?)said:', 'Another user said:', regex=True )
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'On(.*?)[0-9]+\sat\s(\d)?\d:\d\d\s(PM|AM),(.*?)said:', 'Another user said:', regex=True )
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'On\s(.*?)(\sг\.)\sat\s(\d)?\d:\d\d\s(PM|AM),\s(.*?)\ssaid:', 'Another user said:', regex=True )
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'!\[[^\]]*\]\([^)]*\)', '', regex=True)
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'<(.*?)>', '', regex=True)
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'\S*https?:\S*', '', regex=True)
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'>', '', regex=True )
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'\n', ' ', regex=True )
df_posts_iron['post'] = df_posts_iron['post'].str.replace(r'[\w-]+\.html', ' ', regex=True )
df_posts_iron["post"] = df_posts_iron["post"].apply(lambda x: x.strip())
df_posts_iron.post.replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
df_posts_iron = df_posts_iron.loc[(df_posts_iron["post"].str.len() > 120) & (df_posts_iron["post"].str.len() < 5000 ) ]
df_posts_iron['source'] = 'Iron March Posts'
df_posts_iron = df_posts_iron.rename(columns={'post':'text', 'post_date':'date'})

df_storm = pd.read_csv('stormfront/cleanposts_after_iron_english.csv', header=0)
df_storm = df_storm.reindex(["cleanmessage", "posteddate"], axis=1)
df_storm["posteddate"] = df_storm["posteddate"].apply(lambda x: pd.to_datetime(x, utc=True))
df_storm['cleanmessage'] = df_storm['cleanmessage'].str.replace(r'\n', ' ', regex=True )
df_storm['cleanmessage'] = df_storm['cleanmessage'].str.replace(r'\r', '', regex=True )
df_storm['cleanmessage'] = df_storm['cleanmessage'].str.replace(r'\[ame="(.*?)"\](.*?)\[\/ame\]', '', regex=True )
df_storm['cleanmessage'] = df_storm['cleanmessage'].str.replace(r'\S*https?:\S*', '', regex=True )
df_storm['cleanmessage'] = df_storm['cleanmessage'].str.replace(r"\[QUOTE=(.*?);[0-9]+\]", '', regex=True )
df_storm["cleanmessage"] = df_storm["cleanmessage"].apply(lambda x: x.strip())
df_storm.cleanmessage.replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
df_storm = df_storm.loc[(df_storm["cleanmessage"].str.len() > 120) & (df_storm["cleanmessage"].str.len() < 5000 ) ]
df_storm['source'] = 'Stormfront.org'
df_storm = df_storm.rename(columns={'cleanmessage':'text', 'posteddate':'date'})

df_message_iron = pd.read_csv('iron_march/message_posts_edited_english.csv', header=0)
df_message_iron = df_message_iron.reindex(["msg_post", "msg_date"], axis=1)
df_message_iron['msg_post'] = df_message_iron['msg_post'].str.replace(r'\n> ', '', regex=True )
df_message_iron['msg_post'] = df_message_iron['msg_post'].str.replace(r'!\[[^\]]*\]\([^)]*\)', '', regex=True)
df_message_iron['msg_post'] = df_message_iron['msg_post'].str.replace(r'<(.*?)>', '', regex=True)
df_message_iron['msg_post'] = df_message_iron['msg_post'].str.replace(r'\S*https?:\S*', '', regex=True)
df_message_iron['msg_post'] = df_message_iron['msg_post'].str.replace(r'>', '', regex=True )
df_message_iron['msg_post'] = df_message_iron['msg_post'].str.replace(r'\n', ' ', regex=True )
df_message_iron['msg_post'] = df_message_iron['msg_post'].str.replace(r'[\w-]+\.html', ' ', regex=True )
df_message_iron["msg_post"] = df_message_iron["msg_post"].apply(lambda x: x.strip())
df_message_iron.msg_post.replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
df_message_iron = df_message_iron.loc[(df_message_iron["msg_post"].str.len() > 120) & (df_message_iron["msg_post"].str.len() < 5000 ) ]
df_message_iron['source'] = 'Iron March Messages'
df_message_iron = df_message_iron.rename(columns={'msg_post':'text', 'msg_date':'date'})

resulting_df = pd.concat([df_posts_iron, df_message_iron, df_storm], ignore_index=True)
resulting_df['is_facist'] = 0
resulting_df.to_csv('dataset_v1.01.csv', sep='\t', index=False)
resulting_df.to_excel('dataset_v1.01.xlsx', index=False)