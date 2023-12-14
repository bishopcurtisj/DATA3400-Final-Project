import pandas as pd
import numpy as np



def fiveYearAvg():
    fiveYearAvg = list()
    teams = nbaDraft.team.unique().tolist()
    for year in range(2006, 2022):

        for team in teams:
            picks = list()
            for i in range(1, 6):
                pick = nbaDraft[(nbaDraft.year == (year - i)) & (nbaDraft.team == team)].overall_pick
                if len(pick) > 0:
                    picks.append(min(pick))
            avg = sum(picks) / len(picks)
            fiveYearAvg.append(avg)
            print(f'{year}\t{team}\t{avg}')
    return fiveYearAvg


#print(len(fiveYearAvg))

if __name__ == '__main__':
    nbaDraft = pd.read_csv("C:\\Users\\bisho\\Documents\\DATA3400\\Final Project\\nbaplayersdraft.csv")
    teamWins = pd.read_csv("C:\\Users\\bisho\\Documents\\DATA3400\\Final Project\\TeamWins.csv")

    fiveYear=fiveYearAvg()
    while len(fiveYear) != 990:
        fiveYear.insert(0,0)