
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np

#importo los datos y posteriomente me creo un dataframe  por cada variable que voy a analizar
df = pd.read_csv('Datostfg.csv')
# print('Hola')

#Creo una data frame para la variable a estudiar que sera la siguiente:
ContratosTotales=df.pop('Contratos registrados. Total. Tasa de variacion interanual')



#Creo una data frame para las variables regresoras que seran las siguiente:
IncrementoSalarial=df.pop('Incremento.Salarial')
TasadeParo=df.pop('Paro registrado. Tasa de variación interanual')
TasadeParoIndustria=df.pop('Parados sector industria. Tasa de variación interanual')
TasadeParoConstruccion=df.pop('Parados sector construcción. Tasa de variación interanual.')
TasadeParoServicios=df.pop('Parados sector servicios. Tasa de variación interanual.')
Competitividad=df.pop('Competitividad de España. Costes totales. Frente a ue28')
Temporalidad=df.pop('Tasadetemporalidad')
Exportaciones=df.pop('Valor unitario exportaciones  Tasa de variación interanual. ')
CostelaboralUnitario=df.pop('CostelaboralUnitario.Base2010')
Productividad=df.pop('Productividad.Laboral')
ProduccionIndustrial=df.pop('Indice de Producción Industrial')
Matriculacionesdecoches=df.pop('Matriculaciones de vehiculos')


#Desarrollo el primer modelo de regresión.para los contratos totales.
Regresiondecontratosindefinidos=smf.ols('ContratosTotales~TasadeParo+ProduccionIndustrial', data=df)
results=Regresiondecontratosindefinidos.fit()
print(results.summary())

#Analisis de la correlacion del modelo.
correlacion=np.ma.corrcoef([TasadeParo,IncrementoSalarial,Productividad,Exportaciones,ProduccionIndustrial], rowvar=1)
matrizcorrelacion=pd.DataFrame(correlacion, columns=['TasadeParo','IncrementoSalarial','Productividad','Exportaciones','ProduccionIndustrial'])
matrizcorrelacion.to_excel('Correlacioncontratosindefinidos.xls')


# #Analisis del factor de inflacion de varianza para la TasadeParo
TasadeParo=sm.add_constant(TasadeParo)
modelodeTasadeparo=sm.OLS(ContratosTotales,TasadeParo).fit()
a=modelodeTasadeparo.rsquared
r=1/(1-a)
print('FIV incremento TasadeParo: ',r)

# #Analisis del factor de inflacion de varianza para el IncrementoSalarial
IncrementoSalarial=sm.add_constant(IncrementoSalarial)
modelodeincrementosalarial=sm.OLS(ContratosTotales,IncrementoSalarial).fit()
a=modelodeincrementosalarial.rsquared
r=1/(1-a)
print('FIV incremento salarial: ',r)

# #Analisis del factor de inflacion de varianza para la productividad
Productividad=sm.add_constant(Productividad)
modeloproductividad=sm.OLS(ContratosTotales,Productividad).fit()
a=modeloproductividad.rsquared
r=1/(1-a)
print('FIV productividad: ', r)

# #Analisis del factor de inflacion de varianza para las Exportaciones
Exportaciones=sm.add_constant(Exportaciones)
modelodeexportaciones=sm.OLS(ContratosTotales,Exportaciones, missing='drop').fit()
a=modelodeexportaciones.rsquared
r=1/(1-a)
print('FIV Exportaciones: ',r)

# #Analisis del factor de inflacion de varianza para la ProduccionIndustrial
ProduccionIndustrial=sm.add_constant(ProduccionIndustrial)
modelodeproducionindustrial=sm.OLS(ContratosTotales,ProduccionIndustrial).fit()
a=modelodeproducionindustrial.rsquared
r=1/(1-a)
print('FIV ProduccionIndustrial: ',r)
