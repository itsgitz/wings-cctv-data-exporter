#!/usr/bin/env python3

import pandas as pd
import sys

def excel_to_json(args):
    excel_path = None

    try:
        excel_path = args[1]
    except Exception as e:
        print("Excel file path cannot be empty!")
        print("Error:", e)
        return
 
    excel_data = pd.read_excel(excel_path, sheet_name='cctv')
    converted_to_json = excel_data.to_json()

    return converted_to_json

def write_to_json_file(args, data):
    output_json_path = None

    try:
        output_json_path = args[2]
    except Exception as e:
        print("Output file for JSON cannot be empty!")
        print("Error:", e)

        return

    try:
        f = open(output_json_path, 'w')
        f.write(data)
        f.close()
    except Exception as e:
        print("Error:", e)

def main(): 
    # Convert from excel to json
    json_data =  excel_to_json(sys.argv)

    # Write to json file
    write_to_json_file(sys.argv, json_data)

if __name__ == "__main__":
    main()
