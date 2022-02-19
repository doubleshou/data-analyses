from os.path import isfile
import sys

import pandas as pd


def sas2csv(read_file, save_file):
    assert isfile(read_file), "The file does not exist."
    assert read_file.lower().endswith(".xpt"), "The file has no .xpt (SAS) extension."

    try:
        sas_file = pd.read_sas(read_file)
        sas_file.to_csv(save_file, index=False)
    except Exception as e:
        print("An error occurred during conversion.")


if __name__ == "__main__":
    try:
        READ_FILE = sys.argv[1]
        SAVE_FILE = sys.argv[2]
    except (IndexError, NameError) as e:
        print("Not enough arguments.")
    else:
        sas2csv(READ_FILE, SAVE_FILE)
