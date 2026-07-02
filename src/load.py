import pandas as pd 
from logger import log_info
def load_data(df, output_file):
    log_info("load stage stared")
    df.to_csv(output_file,index=False)
    log_info("log operation completed")
    return processcompleted 