import requests
import os

def extract(url="https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv", 
            file_path="data/airline-safety.csv"):
    print("Starting extraction process...")

    if not os.path.exists("data"):
        print("Creating directory 'data'")
        os.makedirs("data")
    else:
        print("Directory 'data' already exists")
    
    print(f"Sending request to {url}...")
    r = requests.get(url)
    
    # status code of the response
    print(f"HTTP Status Code: {r.status_code}")
    
    # Check if the request was successful
    if r.status_code == 200:
        print(f"Request successful! Saving content to {file_path}...")
        
        with open(file_path, 'wb') as f:
            f.write(r.content)
        print(f"File saved successfully at {file_path}")
    else:
        print(f"Failed to download file. Status code: {r.status_code}")
    
    return file_path

extract()
