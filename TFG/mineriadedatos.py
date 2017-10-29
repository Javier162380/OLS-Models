#importo librerias.

import pandas as pd

#Comando para evitar error de pandas por posible copia.
pd.options.mode.chained_assignment = None

#limpieza del archivo de Contratos indefinidos y temporales
#Apertura del fichero y selección de los campos a estudiar.
ArchivodeContratostasas= pd.read_csv('ie0404.csv',skiprows =9,
names = ['','','Contratos indefinidos. Variación interanual','',
'Contratos temporales.Variación interanual',
'Tasadetemporalidad'],
na_values = {'Contratos indefinidos. Variación interanual': ['NULL', '_'],
              'Contratos temporales.Variación interanual': ['NULL', '_']},
usecols=range(6))
Contratostasas=ArchivodeContratostasas.drop(['','',''], axis=1)
#Creación de un dataframe de fechas de la misma longuitud que el dataframe abierto
f1=len(ArchivodeContratostasas)
fechacontratostasas=pd.date_range('31/03/2003', periods=f1, freq='3M')
#Fusión de ambos dataframes
Contratostasas['fechas']=fechacontratostasas

#limpieza del archivo de exportaciones.
#Apertura del fichero y selección de los campos a estudiar.
Archivodeexportaciones = pd.read_csv('ie0504.csv',skiprows = 372,
names=['','Valor unitario exportaciones  Tasa de variación interanual. '],
na_values = {'Valor unitario exportaciones  Tasa de variación interanual. ': ['NULL', '_']},
usecols=range(2))
DatosdeExportaciones=Archivodeexportaciones.drop([''], axis=1)
#Creación de un dataframe de fechas de la misma longuitud que el dataframe abierto
f2=len(Archivodeexportaciones)
fechaexportaciones=pd.date_range('31/03/2002',periods=f2, freq='M')
#Fusión de ambos dataframes
DatosdeExportaciones['fechas']=fechaexportaciones


#limipeza del archivo de datos de paro desglosado.
#Apertura del fichero y selección de los campos a estudiar.
Archivodeparodesglosado = pd.read_csv('ie0405.csv',skiprows = 790,
names=['','Paro registrado','',
'Paro registrado. Tasa de variación interanual',
'',
'',
'Parados sector agrícola. Tasa de variación interanual.',
'',
'Parados sector industria. Tasa de variación interanual',
'Parados sector construcción. Tasa de variación interanual.',
'Parados sector servicios. Tasa de variación interanual.',
'Contratos registrados. Total',
'Contratos registrados. Total. Tasa de variación interanual',
'Contratos indefinidos en porcentaje sobre el total',
'Contratos a jornada parcial en porcentaje sobre el total',
'Contratos temporales en porcentaje sobre el total',
'',
''],)
Datosdeparodesglosdo=Archivodeparodesglosado.drop(['','','','','','',''], axis=1)
#Creación de un dataframe de fechas de la misma longuitud que el dataframe abierto
f3=len(Archivodeparodesglosado)
fechaparodesglosado=pd.date_range('01/01/1999',periods=f3, freq='M')
#Union de ambos dataframes
Datosdeparodesglosdo['fechas']=fechaparodesglosado

#limpieza del archivo de costes laborales.
#Apertura del fichero y selección de los campos a estudiar.
Archivodecosteslaborales = pd.read_csv('ie0408.csv',skiprows = 32,
names=['','CostelaboralUnitario.Base2010','','','','','','','Productividad.Laboral'],
na_values = {'CostelaboralUnitario.Base2010': ['NULL', '_'],
              'Productividad.Laboral': ['NULL', '0']},
usecols=range(9))
Datosdecosteslaborales=Archivodecosteslaborales.drop(['','','','','','',''], axis=1)
#Creación de un dataframe de fechas de la misma longuitud que el dataframe abierto
f4=len(Archivodecosteslaborales)
fechacosteslaborales=pd.date_range('31/03/2002', periods=f4, freq='3M')
#Union de ambos dataframes
Datosdecosteslaborales['fechas']=fechacosteslaborales

#limpieza del archivo de indicesdecompetitividad.
#Apertura del fichero y selección de los campos a estudiar.
Archivodeindicesdecompetividad=pd.read_csv('ie0904.csv', skiprows=38,
names=['','','',
'Competitividad de España. Costes totales. Frente a ue28','',
'','',
'Competitividad de España.Costes laborales relativos unitarios totales.ue28',
'','',
'','Competitividad de España. Costes totales.Frente a UM19',
'',
''],
na_values = {'Competitividad de España. Costes totales. Frente a ue28': ['NULL', '_']})
Datosdeindicesdecompetitividad=Archivodeindicesdecompetividad.drop(['','','','','','','','','','',''], axis=1)
#Creación de un dataframe de fechas de la misma longuitud que el dataframe abierto
f5=len(Archivodeindicesdecompetividad)
fechaindicesdecompetitividad=pd.date_range('31/01/1999', periods=f5, freq='M')
#Union de ambos dataframes
Datosdeindicesdecompetitividad['fechas']=fechaindicesdecompetitividad

#Limpieza del archivo de financiación a empresas.
#Apertura del fichero y selección de los campos a estudiar.
Archivodeproducionindustrial = pd.read_csv('ie0304.csv',skiprows=342,
names=['','','Indice de Producción Industrial'],
 na_values = {'Indice de Producción Industrial': ['NULL', '_']},
 usecols=range(3))
Datosdeproducionindustrial=Archivodeproducionindustrial.drop( ['','',], axis=1)
#Creación de un dataframe de fechas de la misma longuitud que el dataframe abierto
f6=len(Datosdeproducionindustrial)
fechaproducionindustiral=pd.date_range('31/03/2002',periods=f6, freq='M')
#Union de ambos dataframes
Datosdeproducionindustrial['fechas']=fechaproducionindustiral


#limpieza del archivo de convenios colectivos.
#Apertura del fichero y selección de los campos a estudiar.
Archivodeconvenioscolectivos= pd.read_csv('ie0406.csv',skiprows =246,
names = ['', '','Incremento.Salarial'],
usecols=range(3))
Datosdeconvenioscolectivos=Archivodeconvenioscolectivos.drop(['',''], axis=1)
#Creación de un dataframe de fechas de la misma longuitud que el dataframe abierto
f7=len(Archivodeconvenioscolectivos)
fechaconvenioscolectivos=pd.date_range('31/03/2002', periods=f7, freq='M')
#Union de ambos dataframes
Datosdeconvenioscolectivos['fechas']=fechaconvenioscolectivos


#fusion de archivos operando con un inner join, sobre la columna fecha nos quedaremos con
#los datos trimestrales.
Datostfg=pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge
                 (Contratostasas,DatosdeExportaciones, on= 'fechas',how='inner'),
                  Datosdeindicesdecompetitividad, on='fechas', how='inner'),
                  Datosdecosteslaborales, on='fechas', how='inner'),
                  Datosdeconvenioscolectivos, on='fechas', how='inner'),
                  Datosdeparodesglosdo, on='fechas', how='inner'),
                  Datosdeproducionindustrial, on='fechas', how='inner')

print(Datostfg)

#Exportación de los datos a un archivo xls.
Datostfg.to_excel('datostfg.xls')
#Exportación de los datos a un archivo csv.
Datostfg.to_csv('Datostfg.csv')
#Hasta aquí llega la primera parte del trabajo.


