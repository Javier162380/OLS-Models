#--encoding utf-8 --#
from pandas import read_csv,DataFrame
import statsmodels.api as sm
from statsmodels.formula.api import ols
from ast import literal_eval
import statsmodels.stats.api as sms 
from  numpy import ma
import codecs

#open,clean and store of data
with codecs.open('data.csv', "r",encoding='utf-8', errors='ignore') as fdata:
	data=fdata
	iterdata=list(data)
	cleandata=iterdata[1:]
	emptylist=[]

	for i in cleandata:
		
		diccionary={}
		line=i.replace("\r\n","")
		diccionary['date']=line.split(';')[0]
		diccionary['competitiveness_index']=float(line.split(';')[1].replace(',','.'))
		diccionary['unemployment_rate']=float(line.split(';')[2].replace(',','.'))
		diccionary['travellers_index']=float(line.split(';')[3].replace(',','.'))
		diccionary['exports_rate']=float(line.split(';')[4].replace(',','.'))
		diccionary['employee_cost']=float(line.split(';')[5].replace(',','.'))
		diccionary['cement_consumption']=float(line.split(';')[6].replace(',','.'))
		emptylist.append(diccionary)


#All aviable data
df=DataFrame.from_records(data=emptylist)
#df = df[df.competitiveness_index != ""]
#df = df.astype(float)

#independent variable
competitiveness_index=df.pop('competitiveness_index')
#dependent variable
unemployment_rate=df.pop('unemployment_rate')
travellers_index=df.pop('travellers_index')
exports_rate=df.pop('exports_rate')
employee_cost=df.pop('employee_cost')
cement_consumption=df.pop('cement_consumption')

#MCO model
competitiveness=ols('competitiveness_index ~ travellers_index+cement_consumption+employee_cost+unemployment_rate',data=df)
results=competitiveness.fit()
#models results
print(results.summary())

#correlation_analysis
correlation=ma.corrcoef([travellers_index,cement_consumption,employee_cost,unemployment_rate])
print(correlation)