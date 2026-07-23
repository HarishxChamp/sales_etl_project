from .logger import log_info


def load_data(df, output_file):

    log_info("Load Stage Started")

    df.to_csv(output_file, index=False)

    log_info("Output File Created")

    return "Data Loaded Successfully"