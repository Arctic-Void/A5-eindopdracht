import pandas as pd
from datetime import datetime
import lib_bamboo as bamboo
from datetime import timedelta
import os

os.system("cls") #Deze regel nog invullen! Hoe maak je het scherm leeg?
print("Working...")

data = pd.read_excel("python/Voetbal_Amstel League_tussenstand.xlsx")
data["datum"] = pd.to_datetime(data["datum"], format="%d/%m/%Y")
data = data.sort_values("datum")

#Informatievraag 1
#Het totaal aantal overtredingen in de competitie tot nu toe

overtredingen = data["overtredingen"].sum()
overtredingen = int(overtredingen)

print(overtredingen)



#Informatievraag 2
#Het gemiddeld aantal overtredingen per wedstrijd
averageOvertredingen = data["overtredingen"].mean()
print(averageOvertredingen)



#Informatievraag 3
zwartBoek = data_sorted = data.sort_values("divisie",ascending=False)
top5 = data_sorted.head(5)
print(top5)  #Deze regel nog invullen! Hoe maak je een top 5?

file3 = open("files/zwartboek.txt", "w", encoding="UTF-8")
file3.write(bamboo.prettify(zwartBoek, type="zwartboek"))
file3.close() #Deze regel nog invullen! Hoe sluit je file3?


#Informatievraag 4
#Een “eregalerij”, ofwel alle wedstrijden van de laatste 21dagen waarin maximaal één overtreding is geweest
data["datum"] = pd.to_datetime(data["datum"], format = "%d/%m/%Y")
today = datetime.now()
check_date = today - timedelta(days=21)

filter1 = (data["datum"] > check_date and data["datum"] < today)
ereGalerij = data[filter1]
filter2 = (data["overtredingen"] <= 1)
ereGalerij = ereGalerij[filter2]
print(ereGalerij)




print("Done!")



#if data["datum"] > check_date and data["datum"] < today:
    #print(f"{data['team1']} - {data['team2']}")
#filter1 = (data["datum"] > datetime.now())
#ereGalerij = data[filter1]