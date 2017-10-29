
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
import numpy as np

#importo los datos y posteriomente me creo un dataframe  por cada variable que voy a analizar
df = pd.read_csv('Datostfg.csv')


#Creo una data series para la variable a estudiar que seran la siguiente·
ContratosIndefinidos=df.pop('Contratosindefinidos')

#Creo una data series para las variables regresoras que seran las siguiente:
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


#Desarrollo el primer modelo de regresión.para los contratos Indefinidos.
Regresiondecontratosindefinidos=smf.ols('ContratosIndefinidos~TasadeParo+IncrementoSalarial+Exportaciones', data=df)
results=Regresiondecontratosindefinidos.fit()
print(results.summary())



#Analisis de la correlacion del modelo.
correlacion=np.ma.corrcoef([TasadeParo,IncrementoSalarial,Exportaciones], rowvar=1)
matrizcorrelacion=pd.DataFrame(correlacion, columns=['TasadeParo','IncrementoSalarial','Exportaciones'])
matrizcorrelacion.to_excel('Correlacioncontratosindefinidos.xls')
print(matrizcorrelacion)


# #Analisis del factor de inflacion de varianza para la TasadeParo

modelodeTasadeparo=smf.OLS('TasadeParo~IncrementoSalarial+Exportaciones', data=df)
a=modelodeTasadeparo.fit()
a1=results.rsquared
r=1/(1-a1)
print('FIV incremento TasadeParo: ',r)

# #Analisis del factor de inflacion de varianza para el IncrementoSalarial
IncrementoSalarial=sm.add_constant(IncrementoSalarial)
modelodeincrementosalarial=sm.OLS(ContratosIndefinidos,IncrementoSalarial).fit()
a=modelodeincrementosalarial.rsquared
r=1/(1-a)
print('FIV Incremento Salarial: ',r)

# #Analisis del factor de inflacion de varianza para la productividad
Productividad=sm.add_constant(TasadeParo)
modeloproductividad=sm.OLS(ContratosIndefinidos,Productividad).fit()
a=modeloproductividad.rsquared
r=1/(1-a)
print('FIV Tasa de Paro: ', r)

# #Analisis del factor de inflacion de varianza para las Exportaciones
Exportaciones=sm.add_constant(Exportaciones)
modelodeexportaciones=sm.OLS(ContratosIndefinidos,Exportaciones, missing='drop').fit()
a=modelodeexportaciones.rsquared
r=1/(1-a)
print('FIV Exportaciones: ',r)

# #Analisis del factor de inflacion de varianza para la ProduccionIndustrial
ProduccionIndustrial=sm.add_constant(ProduccionIndustrial)
modelodeproducionindustrial=sm.OLS(ContratosIndefinidos,ProduccionIndustrial).fit()
a=modelodeproducionindustrial.rsquared
r=1/(1-a)
print('FIV ProduccionIndustrial: ',r)

# Estudio de la homocedasticidad
name = ['Lagrange multiplier statistic', 'p-value',
        'f-value', 'f p-value']
test = sms.het_breushpagan(results.resid, results.model.exog)
print(test)
