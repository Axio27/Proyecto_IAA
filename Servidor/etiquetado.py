import pandas as pd
import numpy as np
import os

df = pd.read_csv("D:\Python_workplace\IAA\Servidor\Data_sensores.csv")
aux = df

#Seleccionar solo los campos con los que se trabajara
aux = aux[['Fecha','Hora','Temperatura','Humedad_relativa','Humedad_Suelo']]
aux[['Temperatura','Humedad_relativa','Humedad_Suelo']] = aux[['Temperatura','Humedad_relativa','Humedad_Suelo']].apply(pd.to_numeric)
#Se crea el campo ADT y se calcula a partir de Humedad_relativa y Humedad_Suelo
aux.loc[aux['Temperatura'] == 14,'ADT'] = aux['Humedad_relativa']*12.07/100 + aux['Humedad_Suelo']*2000/100
aux.loc[aux['Temperatura'] == 15,'ADT'] = aux['Humedad_relativa']*12.83/100 + aux['Humedad_Suelo']*2000/100
aux.loc[aux['Temperatura'] == 16,'ADT'] = aux['Humedad_relativa']*13.53/100 + aux['Humedad_Suelo']*2000/100
aux.loc[aux['Temperatura'] == 17,'ADT'] = aux['Humedad_relativa']*14.4/100 + aux['Humedad_Suelo']*2000/100
aux.loc[aux['Temperatura'] == 18,'ADT'] = aux['Humedad_relativa']*15.33/100 + aux['Humedad_Suelo']*2000/100
aux.loc[aux['Temperatura'] == 19,'ADT'] = aux['Humedad_relativa']*16.31/100 + aux['Humedad_Suelo']*2000/100
aux.loc[aux['Temperatura'] == 20,'ADT'] = aux['Humedad_relativa']*17.3/100 + aux['Humedad_Suelo']*2000/100
aux.loc[aux['Temperatura'] == 21,'ADT'] = aux['Humedad_relativa']*18.48/100 + aux['Humedad_Suelo']*2000/100
aux.loc[aux['Temperatura'] == 22,'ADT'] = aux['Humedad_relativa']*19.66/100 + aux['Humedad_Suelo']*2000/100
aux.loc[aux['Temperatura'] == 23,'ADT'] = aux['Humedad_relativa']*20.93/100 + aux['Humedad_Suelo']*2000/100
aux.loc[aux['Temperatura'] == 24,'ADT'] = aux['Humedad_relativa']*22.27/100 + aux['Humedad_Suelo']*2000/100
aux.loc[aux['Temperatura'] == 25,'ADT'] = aux['Humedad_relativa']*23/100 + aux['Humedad_Suelo']*2000/100
#Se asigna el valor Ks aproximado para el tipo de suelo
aux.loc[:,'Ks']=(aux['ADT']*0.48)/((aux['ADT']-45)*0.64)

#Se calcula el campo ETr con los valores para el primer mes
aux.loc[:,'ETr']=aux['Ks']*22*0.14

#Se crea el campo Etiqueta
aux.loc[aux['ETr'] < 3 ,'Etiqueta']="Si"
aux.loc[aux['ETr'] > 3 ,'Etiqueta']="No"


aux.to_csv('D:\Python_workplace\IAA\Servidor\BBDD\Data_sensores_et.csv', index=False)
#print(aux.loc[aux['Etiqueta']=="Si"])
#print(aux["Etiqueta"].value_counts())

#print(aux)