#Task 2
import json
import os

filename = "json_file.json"

try:
    with open(filename, "r") as file:
        data = json.load(file)
        data = json.dumps(data, indent=4)
        print(f"[{filename}]: \n {data}")
except Exception as Error:
    print("Error: ", Error)
    os.system('pause')


    