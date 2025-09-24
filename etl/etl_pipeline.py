import pandas as pd
from sqlalchemy import create_engine

#Extraction pipeline
print('Data is gotten from local repository...........')
url_repo= pd.read_csv(r"C:/Users/abdulmuiz.adewale/postgresql/git_collab/etl-sales-data/data/raw_sales.csv")
print(f"Extracted {len(url_repo)} rows and {len(url_repo.columns)} columns")

#Transformation and cleaning pipelines

#---changing the column to lower cases and adding underscore in place of spaces
url_repo.columns= [col.lower() for col in url_repo.columns]
url_repo.columns= [col.replace(' ', '_') for col in url_repo.columns]

#---filling the null values in price with mean value of price
url_repo['price'].fillna(url_repo['price'].mean(), inplace=True)

#Adding a new column total_sales
url_repo['total_sales']= url_repo['quantity'] * url_repo['price']
url_repo['total_sales']= url_repo['total_sales'].round(2)
#url_repo['total_sales']= url_repo['total_sales'].map('{:.2f}'.format).astype(float)
print(url_repo.head())

#saved the cleaned data to local repository
url_repo.to_csv(r"C:/Users/abdulmuiz.adewale/postgresql/git_collab/etl-sales-data/data/cleaned_sales.csv", index=False)
print(f'Extracted {len(url_repo)} rows and {len(url_repo.columns)} columns and \nETL process is completed')

