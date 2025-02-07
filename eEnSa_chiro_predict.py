
#Script to send molecule structures to the eEnSa Chironomid Model Endpoint and retrive results
#contact: erik.gilberg@bayer.com

import pandas as pd
import requests
import json
import os

# Constants
API_URL = 'https://api.prodknime.dywopla.int.bayer.com/deployments/rest:b9c027e0-5371-49ec-9d33-174e66fd55f4/execution?reset=false&timeout=-1'
CSV_FILE = 'input_data.csv'  # Change this to your CSV file path
OUTPUT_FILE = 'output.csv'    # Output file for results
CONFIG_FILE = 'configuration.json'  # Configuration file path

print(f"eEnSa Chironomid Acute Tox - Only for Test Use!")

# Load username and password from configuration file
with open(CONFIG_FILE, 'r') as config_file:
    config = json.load(config_file)
    USERNAME = config['username']
    PASSWORD = config['password']

# Read the CSV file
data = pd.read_csv(CSV_FILE)

# Prepare the payload
structures = []
for index, row in data.iterrows():
    structures.append({
        "id": row['id'],
        "smiles": row['smiles']
    })

payload = {
    "predict": {
        "structures": structures
    }
}

# Make the POST request
response = requests.post(
    API_URL,
    headers={
        'accept': 'application/vnd.mason+json',
        'Content-Type': 'application/json'
    },
    json=payload,
    auth=(USERNAME, PASSWORD)
)

# Prepare a list to hold the output data
output_data = []

# Check if the request was successful
if response.status_code == 200:
    response_json = response.json()
    
    # Extracting the required information
    output_values = response_json.get('outputValues', {}).get('json-output', [])
    
    for output in output_values:
        id_value = output.get('id')
        predicted_pEC50 = output.get('predicted pEC50(chiro_normalized)')
        sd_pEC50 = output.get('SD_pEC50(chiro_normalized)')
        predicted_EC50 = output.get('predicted_EC50_ugL')
        sd_EC50 = output.get('SD_EC50_ugL')
        similarity = output.get('similarity')
        
        # Append the results to the output data list
        output_data.append({
            "ID": id_value,
            "Predicted pEC50": predicted_pEC50,
            "SD pEC50": sd_pEC50,
            "Predicted EC50 (ug/L)": predicted_EC50,
            "SD EC50 (ug/L)": sd_EC50,
            "Similarity": similarity
        })
else:
    print(f"Error: {response.status_code}, {response.text}")

# Create a DataFrame and save it to CSV
output_df = pd.DataFrame(output_data)
output_df.to_csv(OUTPUT_FILE, index=False)

print(f"Results have been written to {OUTPUT_FILE}.")