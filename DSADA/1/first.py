di = {
    "Rollno":[1,2,3,4,5],
    "Name":['Amol','Yesh','Rohan','Mohan','Suraj'],
    "Marks":['First','Destincation','Second','First','Second']
}

import pandas as pd
#load the dictonary into pandas 
df=pd.DataFrame(di);

#print the .cvs form dictonary
print(df)
print("#################################################################")

#find the row and column of dictonary
print(df.shape)
print("#################################################################")
#To print all colums
print(df.columns)
print("#################################################################")
#To print all columns and its coreesponding data type
print(df.dtypes)
print("#################################################################")
#To convert the data type of Rollno  int64 to int32
print(df.astype({'Rollno':"int32"}).dtypes)
print("#################################################################")
#To convert the data type of Rollno  object to string
print(df.astype({'Name':"string"}).dtypes)
print("#################################################################")
#To convert the multiple data type
print(df.astype({"Name":"string","Rollno":"int32"}).dtypes)
print("#################################################################")

#To replace the object into int64
df['Marks'].replace(["Destincation","First","Second"],[0,1,2],inplace=True)

print(df)
print("#################################################################")
#To check the datatype of column
print(df.dtypes)
print("#################################################################")
#To change the data type int32 to category
df['Marks']=df['Marks'].astype('category')

print(df.dtypes)
print("#################################################################")
#To encode 
df['Marks']=df['Marks'].cat.codes
print(df)



