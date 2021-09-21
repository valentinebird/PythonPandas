import pandas as pd
import re
#load data
df = pd.read_csv('pokemon_data.csv')
print(df.head(3))
print(df.tail(3))

#read headers
print(df.columns)

#read each column
print(df['Name']) # df.Name

#Print specific row
print(df.iloc[1:4])

# Print Specific Location R,C
print(df.iloc[2:1])

#iteate

#for index, row in df.iterrows():
  #print(index, row['Name'])

#Find specific data and rows
df.loc[df['Type 1']=="Fire"]
df.loc[df['Legendary']=="TRUE"]

#Sort data
df.describe()


df.sort_values('Name', ascending=False)

print("Change Data")
#Total stats
df['Total'] = df['HP'] + df['Attack'] +  df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))

#Drop columns
#df.drop(columns=['Total'])

#Add a  column in a differennt way
df['Total2'] = df.iloc[:,4:9].sum(axis=1)

#Reorder columns
#df = df[['Total','HP','Defense']]

#Save data
#remove indexes

df.to_csv('modified.csv', index=False)

#To excel
df.to_excel('m.xlsx',index=False)

#filtering 
new_df =  df.loc[(['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]

new_df.to_csv('filtered.csv',index=False)

#Loc name

#df.loc[df['Name']str.contains('Mega')]

#filter data
df.loc[df['Name'].str.contains('pi[a-z]*', flags = re.I,regex=True)]

#change frame based on contidions

#df.loc[df['Type 1']] == 'Fire',

df.loc[df['Total'] > 500, ['Generation','Legendary']] = 'TEST VALUE'

#Aggregate groupby

print("group by")
#df.groupby(['Type 1']).mean()


print("group by2")
df.groupby(['Type 1']).mean().sort_values('HP',ascending=False)


df.groupby(['Type 1']).sum()


#df.groupby(['Type 1','Type 2']).count()['count']

