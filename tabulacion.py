import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

datosOrginales = [98,
 101,
 108,
 108,
 110,
 112,
 115,
 115,
 116,
 118,
 118,
 120,
 120,
 120,
 128,
 129,
 132,
 135,
 137,
 142,
 143,
 145,
 148,
 150,
 154,
 154,
 155,
 157,
 158,
 161,
 162,
 162,
 165,
 167,
 168,
 170,
 170,
 176,
 176,
 177,
 183,
 184,
 186,
 188,
 190,
 191,
 195,
 195,
 205,
 215]

fig, ax =plt.subplots(1,1)
fig2, ax2 =plt.subplots()

hombres = 30
mujeres = 20
total = 50

# Tabla 1.

data=[[hombres, hombres/total, (hombres/total) * 100],
      [mujeres, mujeres/total, (mujeres/total) * 100],
      [total, hombres/total + mujeres/total, 100.0]]

# Tabla 2 datos (Hombres).
rowData = ["[98-115)", 
           "[115-132)",
           "[132-149)",
           "[149-166)",
           "[166-183)",
           "[183-200)",
           "[200-217)"] 

dataAc = 0
dataFi = [6,10,7,10,7,8,2]
dataFr = []
dataFa = []
dataPor = []

# loop function fill table based in Fi.
for nFa in range(0, len(dataFi), 1):
     dataAc += dataFi[nFa]
     dataFa.append(dataAc)
     dataAc = dataFa[nFa]
     
     # list for Fr
     dataFr.append("%d/50" % dataFi[nFa])
     
     # list for %
     dataPor.append(int((dataFi[nFa] / total)*100))
     
dataPrueba = {'labels_row': rowData,
              'Mc': [106.5, 123.5, 140.5, 157.5, 174.5, 191.5, 208.5],
              'Fi': dataFi,
              'Fr': dataFr,
              'Fa': dataFa,
              '%': dataPor}

# Tabla 1
column_labels = ["Fi", "Fr", "Fr%"]
rowsLabels = ["Hombres","Mujeres", "Total"]


# pandas DataFrames for data.
df=pd.DataFrame(data,columns=column_labels)
df2=pd.DataFrame(dataPrueba)

sumXiFi = df2.iloc[:, 1:]['Mc'] * df2.iloc[:, 1:]['Fi']

# add new column dataFrame Pandas
df2['Mc * Fi'] = sumXiFi

# Tabla final para plot de pesos.
rowTot = pd.Series({'labels_row':None, 'Mc': 'Total', 'Fi': sum(df2["Fi"]),'Fr': 1, 'Fa':None, '%': sum(df2["%"]), "Mc * Fi": sum(df2["Mc * Fi"])})
dfTot = pd.DataFrame([rowTot])
df3 = pd.concat([df2, dfTot], ignore_index=True) 

# Details Tables
ax.axis('tight')
ax.axis('off')
#ax.text(0.1, 0.1, '*Media igual a --> {media}'.format(media = media_tb1), horizontalalignment='center', verticalalignment='center', transform=ax2.transAxes)

ax2.axis("tight") 
ax2.axis("off")

copyData = rowData.copy()
copyData.append(None)

tablaEdad = ax.table(cellText=df.values,colLabels=df.columns,rowLabels=rowsLabels,loc="center")
tablaPesos = ax2.table(cellText=df3.values[:, 1:], colLabels=df3.columns[1:], rowLabels=copyData,loc="center")

# Pastel tabla 1
fig5, ax5 =plt.subplots(1,1)
plt.pie([data[x][0] for x in range(0,2,1)] , labels=rowsLabels[0:2], autopct="%0.1f %%")
plt.title("Genero")

# Pastel tabla 2
fig4, ax4 =plt.subplots(1,1)
plt.pie(np.array(df2.iloc[:,:]['Fi']), labels=rowData[0:7], autopct="%0.1f %%")
plt.title("Peso")

# Histogram tabla 2
fig5, ax5 =plt.subplots()
plt.hist(x=datosOrginales, bins=(98, 115, 132,149, 166, 183, 200, 217), )

# bar-Paretto tabla 1
fig6, ax6 =plt.subplots(figsize=(16,12))
ax6.bar(rowsLabels[0:2], [30,20])

axx6 = ax6.twinx()
axx6.plot(rowsLabels[0:2], [30,50], color="red", marker="D", ms=7)
axx6.axhline(80, color="orange", linestyle="dashed")
axx6.set_ylabel("Frecuencia Acumulada");

# Paretto

figP, axP =plt.subplots(figsize=(22,10))

axP.bar(df2['labels_row'], df2["Fi"])
axP.set_title("Pareto Chart")
axP.set_xlabel("Pesos")
axP.set_ylabel("Frequencia Indivdual");

ax2 = axP.twinx()
ax2.plot(df2['labels_row'], df2["Fa"], color="red", marker="D", ms=7)
ax2.axhline(80, color="orange", linestyle="dashed")
ax2.set_ylabel("Frecuencia Acumulada");

plt.show()




    