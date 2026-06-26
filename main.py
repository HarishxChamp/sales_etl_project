from src.config_reader import load_config
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
config=load_config()
source_file=config["source_file"]
destination_file=config["destination_file"]
data=extract_data(source_file)