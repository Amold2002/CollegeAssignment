import pandas as pd 
df = pd.read_csv('abc.csv')

print(df)

#Find the number of column and row 
# print(df.shape)

#Find the all columns
# print(df.columns)

#Find all data types
# print(df.dtypes)

#change the data type
# print(df.astype({'ssc_p':'float64'}).dtypes)

#replace the column
# print(df['status'].replace({'Placed','Not Placed'},[0,1],inplace=True))

#head function by default print the 5 first record
# print(df.head())

#find the first 10 values of document
# print(df.head(10))

#head function by default print the 5 last record
# print(df.tail())

#Find the last 10 record in document
# print(df.tail(10))

# print(df['gender'])

# to print the count of particular colums
# print(df['gender'].count())

#To print the particular columns
# print(df['gender'])

#To see the count of status 
# print(df['status'].count())

#It return the true or false if value is null then return true 
# print(df.isna())

#to see sum of all null values in columns
# print(df.isna().sum())

#it return the specific column with value true or false S
# print(df['status'].isna())

#print the info of the column 
# print(df.info())

# print the document 
# print(df)

# To set the 0th value of status is zero or null
# df['status'][0]=None

#To find the all null values in the all document
# print(df.isna().sum())

#To find the particular column null values 
# print(df['salary'].isna().sum())

#change the name of column gender to Gender 
# print(df.rename(columns={'gender':'Gender'}))

#To change the multiple column name 
# print(df.rename(columns={'gender':'Gender','sl_no':'Serial_No'}))




















