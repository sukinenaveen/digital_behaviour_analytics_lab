import pandas as pd
df=pd.read_csv('digital_behaviour.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df[["Instagram_Minutes","Study_Minutes"]])
print(df["Instagram_Minutes"].sum())
print(df["Study_Minutes"].mean())
print(df["YouTube_Minutes"].max())
print(round(df["Instagram_Minutes"].mean(),2))
print(df[df["Instagram_Minutes"]>100])
print(df[df["Study_Minutes"]>180])


#print(df[df["Instagram_Minutes"]>100])
#Date,Instagram_Minutes,YouTube_Minutes,WhatsApp_Minutes,LinkedIn_Minutes,Reels_Watched,Videos_Watched,Messages_Sent,Posts_Liked,Study_Minutes
