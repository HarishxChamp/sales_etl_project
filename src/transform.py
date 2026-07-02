import pandas as pd

from src.logger import log_info

def transform_data(df):
    log_info("transforming data has started ")
    df= df.drop_duplicates() 
    log_info("duplicate data just had droped out")
    df=df.dropna()
    log_info("droped non a null vales ")
    return df