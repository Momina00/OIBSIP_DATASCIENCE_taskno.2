import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
plt.style.use('dark_background')
df1= pd.read_csv(r"C:\Users\hp\Desktop\_python_journey\oaisis_infobyte_internship_on_data_science\Unemployment Analysis wit python\Unemployment in India.csv",sep='\t')

df2= pd.read_csv(r"C:\Users\hp\Desktop\_python_journey\oaisis_infobyte_internship_on_data_science\Unemployment Analysis wit python\Unemployment_Rate_upto_11_2020.csv")

#STANDARDIZED THE COLUMNS,,,REMOVE SPACES,% AND BRACES TO AVOID BUGG
df1.columns = df1.columns.str.strip().str.replace(' ','_').str.replace('(','').str.replace(')','').str.replace('%','')
df2.columns = df2.columns.str.strip().str.replace(' ','_').str.replace('(','').str.replace(')','').str.replace('%','')

#ALIGNING THE COLUMNS TO ENSURE SAME ORDER, PREVENT MERGE ERRORS,MAKE DATASETS STRUCTURALLY SIMILAR
df2 = df2[df1.columns]

#COMBINE DATASETS
df = pd.concat([df1,df2])

#DROP DUPLICATES SINCE 2020 DATA MIGHT OVERLAP AND CREATE ERROR IN ANALYSIS OF DATA
df.drop_duplicates(inplace=True)
df = df.reset_index(drop=True)

# NOW LETS DO TIME-SERIES ANALYSIS,CONVERTING STRING DATE INTO REAL DATETIME FORMAT SO THAT OUR DATE BECOMES TIME-OBJECT
df['Date'] = pd.to_datetime(df['Date'],dayfirst=True)
df = df.sort_values(by='Date')

#why? because Time series must be in order(april shown before jan, NOT PROPER DATA), NOW EXTRACT YEAR AND MONTH
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

#"WHAT HAPPENED IN 2020/(COVID),,ANY MONTHLY PATTERN?"

#FIRST VISUALIZATION
# plt.figure(figsize = (10,5))
# sns.lineplot(x = 'Date', y = 'Estimated_Unemployment_Rate_', data=df)
# plt.title("UNEMPLOYMENT TREND ANALYSIS WITH COVID PERIOD HIGHLIGHTED")
 
 #COVID COMPARISON,INSIGHT OF THE SPIKE IN THE GRAPH
pre_covid = df[df['Date'] < '2020-03-01']
covid = df[df['Date']>= '2020-03-01']

#CONVERT YOUR GRAPH INTO NUMBERS
print(pre_covid['Estimated_Unemployment_Rate_'].mean())
print(covid['Estimated_Unemployment_Rate_'].mean())

# plt.show()
plt.figure(figsize = (10,5))
sns.lineplot(x='Date',y='Estimated_Unemployment_Rate_',hue = 'Area',data = df)

#HIGHLIGHT COVID PERIOD
plt.axvspan('2020-03-01','2020-06-30',color = 'red', alpha = 0.2)
plt.text(pd.to_datetime('2019-06-01'), 15,"PRE-COVID PERIOD")
plt.text(pd.to_datetime('2020-04-01'), 15,"COVID PERIOD")
plt.show()
