#importo librerias
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
import numpy as np


#importo los datos y posteriomente me creo un dataframe  por cada variable que voy a analizar
df = pd.read_csv('Datostfg.csv')


#Creo una data frame para la variable a estudiar que sera la siguiente:
ContratosTemporales=df.pop('Contratostemporales')

#Creo una data frame para las variables regresoras que seran las siguiente:
IncrementoSalarial=df.pop('Incremento.Salarial')
TasadeParo=df.pop('Paro registrado.TVI')
TasadeParoIndustria=df.pop('Parados sector industria.TVI')
TasadeParoConstruccion=df.pop('Parados sector construccion.TVI')
TasadeParoServicios=df.pop('Parados sector servicios.TVI')
Competitividad=df.pop('Competitividad de Espana. Costes totales. Frente a ue28')
Temporalidad=df.pop('Tasadetemporalidad')
Exportaciones=df.pop('Exportaciones')
CostelaboralUnitario=df.pop('CostelaboralUnitario.Base2010')
Productividad=df.pop('Productividad.Laboral')
ProduccionIndustrial=df.pop('Indice de Produccion Industrial')
Matriculacionesdecoches=df.pop('Matriculaciones de vehiculos')
Viajeros=df.pop('Viajeros alojados en hoteles tasa de variacion interanual')

#Desarrollo el primer modelo de regresión.para los contratos temporales
Regresiondecontratostemporales=smf.ols('ContratosTemporales~Viajeros+ProduccionIndustrial+IncrementoSalarial+TasadeParo', data=df)
results=Regresiondecontratostemporales.fit()
print(results.summary())


#Analisis de la multicolinealidad del modelo.
correlacion=np.ma.corrcoef([TasadeParo,IncrementoSalarial,ProduccionIndustrial,Viajeros], rowvar=1)
matrizcorrelacion=pd.DataFrame(correlacion, columns=['TasadeParo','IncrementoSalarial','ProduccionIndustrial','Viajeros'])
print(matrizcorrelacion)
matrizcorrelacion.to_excel('Correlacioncontratostemporales.xls')


# #Analisis del factor de inflacion de varianza para la TasadeParo

RegresiondeTasadeParo=smf.ols('TasadeParo~Viajeros+ProduccionIndustrial+IncrementoSalarial', data=df)
results2=RegresiondeTasadeParo.fit()
r=results2.rsquared()
r=1/(1-a)
print('FIV TasadeParo: ',r)


# #Analisis del factor de inflacion de varianza para el IncrementoSalarial
IncrementoSalarial=sm.add_constant(IncrementoSalarial)
modelodeincrementosalarial=sm.OLS(ContratosTemporales,IncrementoSalarial).fit()
a=modelodeincrementosalarial.rsquared
r=1/(1-a)
print('FIV Incremento salarial: ',r)

# #Analisis del factor de inflacion de varianza para las Exportaciones
Exportaciones=sm.add_constant(Exportaciones)
modelodeproducionindustrial=sm.OLS(ContratosTemporales,ProduccionIndustrial).fit()
a=modelodeproducionindustrial.rsquared
r=1/(1-a)
print('FIV ProduccionIndustrial: ',r)

# #Analisis del factor de inflacion de varianza para el numero de viajeros
Exportaciones=sm.add_constant(Exportaciones)
modelodeproducionindustrial=sm.OLS(ContratosTemporales,Viajeros).fit()
a=modelodeproducionindustrial.rsquared
r=1/(1-a)
print('FIV Viajeros: ',r)

#Breusch-Pagan
name = ['Lagrange multiplier statistic', 'p-value',
        'f-value', 'f p-value']
test = sms.het_breushpagan(results.resid, results.model.exog)
zip(name,test)
print(list(zip(name,test)))

