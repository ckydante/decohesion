import matplotlib.pyplot as ppt
import pandas as pandas
import csv as csv

pd = pandas.read_csv ('Specimen_RawData_T2.csv',encoding='utf-8', skiprows=9)





fig, ax = ppt.subplots()

pd.plot(y='(N)', x='(mm)', ax=ax)
fig.suptitle = ('Wykres sily od przemieszczenia')
fig.savefig('sila.png')




