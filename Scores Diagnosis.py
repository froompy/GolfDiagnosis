import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.options.display.float_format = '{:,.3f}'.format

#Function for hole result
def applyresult(score):
    if score == -2:
        return 'Ace'
    elif score == -1:
        return "Birdie"
    elif score == 0:
        return "Par"
    elif score == 1:
        return "Bogey"
    elif score == 2:
        return "Double Bogey"
    elif score == 3:
        return "Triple Bogey"
    else:
        return "Other"

df = pd.read_csv(r'''C:\Users\froom\OneDrive\Documents\Docs\Coding\Python\Web Scrape\Garmin scrape\scorecards.csv''')
df.drop(['Unnamed: 0'],axis=1,inplace=True)

##Calculate strokes to par and create a new column
df['Result'] = df['Strokes'] - df['Par']
##Create new column that has hole result (Eagle, Ace (Layton has an Ace), Birdie, etc...)..and run it through 'applyresult' function
df['To_Par'] = df['Result'].apply(applyresult)
##Print off unique courses played

print(f"List of courses played:")
for i in df['Course'].unique():
    print(f"   {i}")

##Remove '0' score holes from dataframe.
df = df[~(df[df.columns[3:3]]==0).any(axis=1)]
df['Date'] = pd.to_datetime(df['Date'])



####Complete rounds for golf course taken from the "courselist" below.
##Just change the course name (matching courselit) and year needed.
# courselist = ['Holiday Park Golf Course' 'York Lake Golf & Country Club'
#  'Silverwood Golf Course' 'Wildwood Golf Course'
#  'Moonlake Golf & Country Club' 'Deer Park Municipal Golf Course'
#  'Valleyview Delisle Golf & Country Club'
#  'The Willows Golf & Country Club' 'Pipestone Hills' 'Shields Golf Course'
#  'Dakota Dunes Golf Links' 'The Legends Golf Club']

# df = df[(df['Course']=="Holiday Park Golf Course") & (df['Type']=='Championship') & (df['Date'].dt.year==2023)]
df = df[(df['Course']=="Deer Park Municipal Golf Course") & (df['Date'].dt.year==2022)]
# df = df[(df['Course']=="Wildwood Golf Course") & (df['Date'].dt.year==2023)]
# df = df[(df['Course']=="Holiday Park Golf Course") & (df['Type']=='Championship') & (df['Date'].dt.year==2021)]
# df = df[(df['Course']=="Moonlake Golf & Country Club") & (df['Date'].dt.year==2024)]
#Print off above result
#Number of holes played at course/year
print(f"Number of holes played: {len(df)}")
#Total numbers of results
print(f"Hole Results: ")
print(f"{df['To_Par'].value_counts()}")


# print(df.loc[((df['Date'].dt.month_name()=='October') & (df['Date'].dt.year==2022))])
coursename = pd.unique(df[['Course','Type']].values.ravel('K'))
dfHPGC = df.groupby('Hole').mean().reset_index()
dfHPGC['Over Par'] = dfHPGC['Strokes'] - dfHPGC['Par']
print(f"{coursename[0]} {coursename[1]}")

print(dfHPGC[['Hole','Over Par','Putts']].to_string(index=False))

