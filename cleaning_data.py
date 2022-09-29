import janitor as ja
import pandas as pd
# create data

stocks = {"CompanyNam":["Roku","Google",pd.NA],
          "DATE": ["20202912","20202313",pd.NA],
          "STOCK Price": ["300","1700",pd.NA],
          "DIvidend":[pd.NA,pd.NA,pd.NA]}

stocks_df= pd.DataFrame.from_dict(stocks)
print(stocks_df)

# Delete a column from the Dataframe. Say 'DIvidend'
del stocks_df['DIvidend']
print(stocks_df)

# Drop Row that have empty values in columns
stocks_df= stocks_df.dropna(subset=["DATE","STOCK Price"])
print(stocks_df)


# CÁCH 2: SỬ DỤNG API
stocks_df= (
    pd.DataFrame(stocks)
    .drop(columns="DIvidend")
    .dropna(subset=['DATE','STOCK Price'])
)
print(stocks_df)

#CÁCH 3: SỬ DỤNG PYJANITOR
stocks_df1= pd.DataFrame.from_dict(stocks)
stocks_df1=stocks_df1.clean_names().remove_empty()
print(stocks_df1)