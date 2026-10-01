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
print(df.head(5));
print(df.tail(5));
#print(df[len()])
print(df["Instagram_Minutes"])
print(df["Instagram_Minutes"].sum())
print(df["Study_Minutes"].mean())
print(df["YouTube_Minutes"].max())
print(df[df["Instagram_Minutes"]>100])
print(df[df["Study_Minutes"]>180])
df= df.sort_values("Instagram_Minutes", ascending=False)
print(df)
print(df[df["Study_Minutes"]>df["Study_Minutes"].mean()])
df['Total_screen_time']=df["Instagram_Minutes"]+df["YouTube_Minutes"]+df["WhatsApp_Minutes"]+df["LinkedIn_Minutes"]
df['Screen_hours']=df['Total_screen_time']/60
df['Digital_balance']=df['Study_Minutes']/df['Total_screen_time']
Day_Type=df["Total_screen_time"]
#loc[which rows,which cols]=value
#print(df[rows,cols])
total_min=df["Instagram_Minutes"].sum(),df["YouTube_Minutes"].sum(),df["WhatsApp_Minutes"].sum(),df["LinkedIn_Minutes"].sum()
print(total_min)
print(max(total_min))
print(df[df["Study_Minutes"]>df["Study_Minutes"].mean()])
print(df["Digital_balance"].mean())



#print(df[df["Instagram_Minutes"]>100])
#Date,Instagram_Minutes,YouTube_Minutes,WhatsApp_Minutes,LinkedIn_Minutes,Reels_Watched,Videos_Watched,Messages_Sent,Posts_Liked,Study_Minutes
