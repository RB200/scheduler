import csv
import pandas as pd
import random
rows=[]
with open("./schedule.csv","r") as f:
  reader=csv.reader(f)
  for row in reader: 
    rows.append(row)

headers = rows[0]

print(headers)

df = pd.read_csv('./schedule.csv')

list_of_divisions = []
data = df[1:]

div = df['Division']

for i in div:
    if str(i) not in list_of_divisions:
        list_of_divisions.append(i)

list_of_teams = df['Home Team']
total_teams = len(df['Away Club'])

print(df[df['Pitch'].str.contains('-7')])




homeTeams = []
awayTeams = []
class SchedulePhase1:
    def __init__(self):
        self.amount_of_matchups = int(total_teams) / 2
        self.u09 = df.loc[df['Age'] == 'U09']
        self.u10 = df.loc[df['Age'] == 'U10']
        self.u11 = df.loc[df['Age'] == 'U11']
        self.u12 = df.loc[df['Age'] == 'U12']
        self.u13 = df.loc[df['Age'] == 'U13']
        self.u14 = df.loc[df['Age'] == 'U14']
        self.u15 = df.loc[df['Age'] == 'U15']
        self.u16 = df.loc[df['Age'] == 'U16']
    def makeMatchup(self):
        r1 = random.randint(0,int(len(list_of_teams) -1))
        r2 = random.randint(0,int(len(list_of_teams) -1))
        t1 = list_of_teams[r1]
        list(list_of_teams).remove(list_of_teams[r1])

        t2 = list_of_teams[r2]
        list(list_of_teams).remove(list_of_teams[r2])
    
        return (t1,t2)
schedule = SchedulePhase1()

for i in range(int(schedule.amount_of_matchups)):
    print(schedule.makeMatchup())

print(schedule.u09['Home Team'])