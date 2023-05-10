import pandas as pd
df=pd.read_csv('most_subscribed_youtube_channels.csv',
    dtype={'rank': 'int64',
        'Youtuber': 'str',
        'subscribers': 'int64',
        'video views':'int64',
        'video count':'int64',
        'category':'category',
        'started':'int64'},
        thousands=',')

print(df.head())
print(df.info())

column_names=list(df.columns.values)
print(column_names)

for item in column_names:
    print(item, 'nulls:', df[item].isna().sum())
    print(item, 'zeroes:', df[item].isin([0]).sum())

#10 zeroes in video views
#10 zeroes in video count
#27 nulls in category

dropping=(df['category'].isna()) | (df['video views'] == 0) | (df['video count'] == 0)
print(df[dropping])

df=df.drop(df[dropping].index)

for item in column_names:
    print(item, 'nulls:', df[item].isna().sum())
    print(item, 'zeroes:', df[item].isin([0]).sum())
print(df.shape)

#EDA
numdata=df[['subscribers','video views', 'video count', 'started']]
pd.set_option('display.float_format', lambda x: '%.3f' % x)
print(numdata.describe())

#look at outliers
import matplotlib.pyplot as plt
import seaborn as sns

for column in numdata:
    plt.figure(figsize =(10, 5))
    plt.title(column + ' outliers')
    sns.boxplot(x=df[column], palette="rocket")
    plt.show()

#impossible for channel to start in 1970, change to  2005
df['started']=df['started'].replace(1970, 2005)

print(df.describe())

categorydf = df.groupby('category').size().sort_values(ascending=False)
print(categorydf)


myexplode = [0.2, 0, 0.4,  0.1]

palette_color = sns.color_palette('rocket')
#plt.pie(categorydf, labels=categorydf['category'], colors=palette_color,
        explode=myexplode, autopct='%.0f%%')
#plt.show()