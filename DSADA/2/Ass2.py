import pandas as pd
df=pd.read_csv("exams.csv")
print(df)

#find out the first five record of the document
# print(df.head())
#find out the last five record of the document
# print(df.tail())

#find out the sum of all blank value in the document
# print(df.isna().sum())

#assign the value to reading score column have 0th index 
# df['reading score'][0] = None

#find out the sum of all blank value in the document
# print(df.isna().sum())

#find out the how many columns in the document
# print(df.columns)

#rename the column names in the document 
df = df.rename(columns={'gender':'Gender','math score':'MathScore','reading score':'ReadingScore','writing score':'WritingScore'})

#print the data
# print(df)

#print the random record in the document 
# print(df.sample())

#describe the document like max,min,25%,50%,75%
# print(df.describe())

#to work with the seaborn we need to import these libary 
import numpy as pd
import seaborn as sns1
import matplotlib.pyplot as plt1
import seaborn as sns2
import matplotlib.pyplot as plt2

#To plot the graph of ReadingScore column 
# sns.boxplot(df["ReadingScore"])

#To show the graph
# plt.show()

#print the hiehest and lowest allowed ReadingScore 
# print("Highest Allowed: ",df["ReadingScore"].mean()+3*df["ReadingScore"].std())
# print("Lowest Allowed: ",df["ReadingScore"].mean()-3*df["ReadingScore"].std())

#113 24

#assign the value to ReadingScore column have 10th index
# 					or
# plot the outlier in graph

# df["ReadingScore"][10]=120
# sns.boxplot(df["ReadingScore"])
# plt.show()
# import sklearn.preprocessing as RobustScaler
# df['ReadingScore']=(df['ReadingScore']-df['ReadingScore'].mean())/(df['ReadingScore'].quantile(0.75)-df['ReadingScore'].quantile(0.25))
# print('\n Robust Scaling \n\n')
# sns.boxplot(df["ReadingScore"])
# plt.show()

#plot the graph
# sns.boxplot(df["ReadingScore"])
# plt.show()

#remove the  outlier from graph
# df[(df['ReadingScore'] > 113 ) | (df['ReadingScore'] < 40)]


# sns.boxplot(df["ReadingScore"])
# plt.show()

# df=df[(df['ReadingScore'] <= 113)]

#group the Gender and print its persentage
# list = df[['Gender','ReadingScore']].groupby('Gender').mean()
# print(list)


# sns.boxplot(df['ReadingScore'],df['WritingScore'])
# plt.show()




# import seaborn as sns

#To see the outliers
# sns1.boxplot(x='Gender', y='ReadingScore', data=df)
# plt1.show()

# remove the outlier from dataSet in 2D
# sns1.boxplot(x='Gender', y='ReadingScore', data=df,showfliers=False)
# plt1.show()



# remove the outlier from dataSet in 1D
sns1.boxplot(df['ReadingScore'],showfliers=False)
plt1.show()










