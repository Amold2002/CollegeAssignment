
# #Assignment3
# import pandas as pd
# df = pd.read_csv("emp.csv")


# #Print the information of dataset
# # print(df)
# # print(df.columns)
# # print(df.shape)
# # print("\nFirst Five Rows\n",df.head().T)
# # print("\nLast Five Rows\n",df.tail().T)

# #Mean,Median,min,,max,std

# # print("The Mean of Salary : ",df['Salary'].mean())
# # # print("The Mode of Salary : ",df['Salary'].mode())
# # print("The Median of Salary : ",df['Salary'].median())
# # print("The min of Salary : ",df['Salary'].min())
# # print("The max of Salary : ",df['Salary'].max())
# # print("The std of Salary : ",df['Salary'].std())

# # #

# # columns=['Experience_Years','Age','Salary']
# # print('{:<20}{:<20}{:<15}{:<15}{:<15}{:<15}'.format("Columns","Mean","Median","Min","Max","STD"))
# # for column in columns:
# # 	m1,m3,m4,m5,m6=df[column].mean(),df[column].median(),df[column].min(),df[column].max(),df[column].std()
# # 	print('{:<20}{:<20}{:<15}{:<15}{:<15}{:<15}'.format(column,m1,m3,m4,m5,m6))
	
# # 	# print(column,m1,m3,m4,m5,m6)

# #

# import  matplotlib.pyplot as plt
# import numpy as np

# #print the categerical data 

# # columns=['Experience_Years','Age','Salary']
# # print('{:<20}{:<20}{:<20}{:<15}{:<15}{:<20}'.format("Columns","Mean","Median","Min","Max","STD"))
# # for column in columns:
# # 	a1=df[column].groupby(df['Gender']).mean()
# # 	a2=df[column].groupby(df['Gender']).median()
# # 	a3=df[column].groupby(df['Gender']).min()
# # 	a4=df[column].groupby(df['Gender']).max()
# # 	a5=df[column].groupby(df['Gender']).std()

# # 	print("\n+++++++++++++++++ ",  column,"++++++++++++++++=\n")
# # 	print('{:<20}{:<20}{:<20}{:<15}{:<15}{:<20}'.format("Female",a1[0],a2[0],a3[0],a4[0],a5[0]))
# # 	print('{:<20}{:<20}{:<20}{:<15}{:<15}{:<20}'.format("Male",a1[1],a2[1],a3[1],a4[1],a5[1]))


# #Representation of  categorical data into graphical formate

# print("Representation of data in graphical formate")
# X=['mean','median','min','max','std']
# column=['Experience_Years','Age','Salary']
# df1 = pd.DataFrame(columns=['mean','median','min','max','std'])
# for var in column:
# 	df1['mean']=df[var].groupby(df['Gender']).mean()
# 	df1['median']=df[var].groupby(df['Gender']).median()
# 	df1['min']=df[var].groupby(df['Gender']).min()
# 	df1['max']=df[var].groupby(df['Gender']).max()
# 	df1['std']=df[var].groupby(df['Gender']).std()
# 	X_axis = np.arange(len(X))

# 	plt.bar(X_axis-0.2,df1.iloc[0],0.4,label = 'Female')
# 	plt.bar(X_axis+0.2,df1.iloc[1],0.4,label = 'Male')

# 	plt.xticks(X_axis,X)
# 	plt.xlabel('Statistical Information')
# 	plt.ylabel(var)
# 	plt.title('Statistical Information')
# 	plt.legend()
# 	plt.show()

# choice=1

# while(choice==1):
# 	print("################### Statistic ####################")
# 	print("1) Print the Information of the Employee DataSet")
# 	print("2) Print the Mean , Median ,Min, Max,std of diffrent column in dataset")
# 	print("3) print the categerical data  ")
# 	print("4) Representation of  categorical data into graphical formate ")
# 	print("5) Exit")
# 	print("Enter the Choice : ")
# 	choice = input()
# 	if choice==1:print("Case 1") 	
# 	elif choice==2:print("Case 2") 
# 	elif choice==3:print("Case 3") 
# 	elif choice==4:print("Case 4") 	
# 	elif choice==5:print("Exit Success")
# 	else:print("Please enter correct choice")
# 	print("Do you want to continue ")


	
import pandas as pd
df = pd.read_csv("iris.csv")


# #Print the information of dataset
# print(df)
# print(df.columns)
# print(df.shape)
# print("\nFirst Five Rows\n",df.head().T)
# print("\nLast Five Rows\n",df.tail().T)

# #Mean,Median,min,,max,std

# print("The Mean of PetalLengthCm : ",df['PetalLengthCm'].mean())
# # print("The Mode of PetalLengthCm : ",df['PetalLengthCm'].mode())
# print("The Median of PetalLengthCm : ",df['PetalLengthCm'].median())
# print("The min of PetalLengthCm : ",df['PetalLengthCm'].min())
# print("The max of PetalLengthCm : ",df['PetalLengthCm'].max())
# print("The std of PetalLengthCm : ",df['PetalLengthCm'].std())

# # #

# columns=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
# print('{:<20}{:<20}{:<15}{:<15}{:<15}{:<15}'.format("Columns","Mean","Median","Min","Max","STD"))
# for column in columns:
# 	m1,m3,m4,m5,m6=df[column].mean(),df[column].median(),df[column].min(),df[column].max(),df[column].std()
# 	print('{:<20}{:<20}{:<15}{:<15}{:<15}{:<15}'.format(column,m1,m3,m4,m5,m6))
	
	# print(column,m1,m3,m4,m5,m6)

# #

import  matplotlib.pyplot as plt
import numpy as np

# #print the categerical data 

# columns=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
# print('{:<20}{:<20}{:<20}{:<15}{:<15}{:<20}'.format("Columns","Mean","Median","Min","Max","STD"))
# for column in columns:
# 	a1=df[column].groupby(df['Species']).mean()
# 	a2=df[column].groupby(df['Species']).median()
# 	a3=df[column].groupby(df['Species']).min()
# 	a4=df[column].groupby(df['Species']).max()
# 	a5=df[column].groupby(df['Species']).std()

# 	print("\n+++++++++++++++++ ",  column,"++++++++++++++++=\n")
# 	print('{:<20}{:<20}{:<20}{:<15}{:<15}{:<20}'.format("Iris-setosa",a1[0],a2[0],a3[0],a4[0],a5[0]))
# 	print('{:<20}{:<20}{:<20}{:<15}{:<15}{:<20}'.format("Iris-versicolor",a1[1],a2[1],a3[1],a4[1],a5[1]))
# 	print('{:<20}{:<20}{:<20}{:<15}{:<15}{:<20}'.format("Iris-virginica",a1[1],a2[1],a3[1],a4[1],a5[1]))


# #Representation of  categorical data into graphical formate

print("Representation of data in graphical formate")
X=['mean','median','min','max','std']
column=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
df1 = pd.DataFrame(columns=['mean','median','min','max','std'])
for var in column:
	df1['mean']=df[var].groupby(df['Species']).mean()
	df1['median']=df[var].groupby(df['Species']).median()
	df1['min']=df[var].groupby(df['Species']).min()
	df1['max']=df[var].groupby(df['Species']).max()
	df1['std']=df[var].groupby(df['Species']).std()
	X_axis = np.arange(len(X))

	plt.bar(X_axis-0.2,df1.iloc[0],0.4,label = 'Iris-setosa')
	plt.bar(X_axis+0.2,df1.iloc[1],0.4,label = 'Iris-versicolor')

	plt.xticks(X_axis,X)
	plt.xlabel('Statistical Information')
	plt.ylabel(var)
	plt.title('Statistical Information')
	plt.legend()
	plt.show()
