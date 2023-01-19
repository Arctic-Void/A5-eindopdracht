import pandas as pd
from datetime import datetime
import lib_bamboo as bamboo
from datetime import timedelta
import os

eregalerijFile = open("python/eregalerij.txt", "w")

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
data["datum"] = pd.to_datetime(data["datum"], format="%d/%m/%Y")
filter = (data["datum"] > datetime.now())
filter2 = ((data["overtredingen"] <= 1))
data_filtered = data[filter]
data_filtered = data_filtered[filter2]
data_sorted2 = data_filtered.sort_values("datum", ascending=False)
last21 = data_sorted2.head(21)

blankIndex = [''] * len(last21)
last21.index=blankIndex

print(last21)
open("python/eregalerij.txt", 'w')
eregalerijFile.write(bamboo.prettify(last21, type="eregalerij"))


print("Done!")

eregalerijFile.close()
