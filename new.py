import cv2 as cv
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df=pd.read_csv(r'D:\Downloads\Cricket_Batsman_Ranker\Cricket.Runs.csv',encoding='latin')
df3=pd.read_csv(r'D:\Downloads\Cricket_Batsman_Ranker\Cricket.Runs.csv',encoding='latin')
df[['start_of_career','end_of_career']]=df['Span'].str.split('-',n=1,expand=True)
df['start_of_career']=pd.to_numeric(df['start_of_career'])
df['end_of_career']=pd.to_numeric(df['end_of_career'])
df['Experience(in years)']=df['end_of_career']-df['start_of_career']
df1=df
df1['HS']=df1['HS'].str.replace('*','')
df1['HS']=df1['HS'].astype(int)
df1.drop(columns=['Player','Span','end_of_career','start_of_career'],axis=1,inplace=True)
df1= df1.to_numpy(dtype=np.float32)
## define criteria and apply kmeans() using opencv 
## The sample data must be a numpy array of np.float32 type
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center=cv.kmeans(df1,4,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)

def file_info(df4=df):
    info=df.info()
    print(info)
    print("Printing statistics")
    print(df.describe(include='all'))

def cluster_show(df3=df3):
     print("1.The potential greats\n2.The Elites\n3.The Legends\n4.The Smashers")
     choice=int(input("Enter which cluster you wanna see:"))
     match choice:
          case 1:
               A=df3[label==0].head()
               print(A)
          case 2:
               A=df3[label==1].head()
               print(A)
          case 3:
               A=df3[label==2].head()
               print(A)
          case 4:
               A=df3[label==3].head()
               print(A)
          case _:
               print ("f")        
def statistical_data(df3=df3,l=label.flatten()):
      print("1.Runs v/s Average\n2.Innings v/s Runs\n3.Runs v/s Strike rate")
      choice=int(input("Enter which cluster you wanna see:"))
      match choice:
          case 1:
           plt.figure(figsize=(10,6))
           sns.scatterplot(data=df3, x='Runs', y='Ave', hue=l, palette='Set1', s = 150)
           plt.title('Runs v/s Average')
           plt.show()
          case 2:
           plt.figure(figsize=(10,6))
           sns.scatterplot(data=df3, x='Inns', y='Runs', hue=l, palette='Set1', s = 150)
           plt.title('Innings v/s Runs')
           plt.show()
          case 3:
           plt.figure(figsize=(10,6))
           sns.scatterplot(data=df3, x='Runs', y='SR', hue=l, palette='Set1', s = 150)
           plt.title('Runs v/s Strike Rate')
           plt.show()
          case _:
              print("f") 

#cluster_show()
statistical_data()