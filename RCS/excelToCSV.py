import pandas as pd
import os
import re

def find_excel_filenames():
    suffix=".xlsx"
    # List all filenames in the specified directory
    filenames = os.listdir()
    # Return only those that end with the specified suffix
    return [filename for filename in filenames if filename.endswith(suffix)]

def excel_to_csv(filenames, path):
    head_string ="charitydata-107881872RR0001-"
    for filename in filenames:
        print(f"processing {filename}")
        try:
            tail_string = filename.split(head_string, 1)[1]
            suffix_index = tail_string.find(".")
            suffix=tail_string[0:suffix_index]
            name = f"{path}RCS-{suffix}.csv"
            # print(name)
            df = pd.read_excel(filename)
            df.to_csv(name)
            print(f"writing {name}")
        except UnicodeDecodeError as e:
            print(f"Unicode error in {filename}: {e}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")


def main():
    out_path = '../cleaned_data/divisionBudgets/'
    filenames = find_excel_filenames()
    excel_to_csv(filenames, out_path)


if "__main__":
    main()

