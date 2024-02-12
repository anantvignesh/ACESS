import json
import os

import requests
from bs4 import BeautifulSoup, SoupStrainer


class Helper:
    def __init__(self):
        pass

    def load_config(self, configPath = "./config.json"):

        # Load the JSON config file
        with open(configPath, 'r') as file:
            config = json.load(file)

        # Set environment variables
        for key, value in config.items():
            os.environ[key.upper()] = str(value)

        print("Environment variables set.")

    def get_text_from_url(self, url):
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Use BeautifulSoup to parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract all text from the page
            text = soup.get_text(separator='\n', strip=True)

            return text
        else:
            return "Failed to retrieve the webpage"

    def get_filtered_text_from_url(self, url):
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Define the parts of the document to focus on
            strainer = SoupStrainer(['h1', 'p'])

            # Use BeautifulSoup to parse the HTML content, focusing on h1 and p tags
            soup = BeautifulSoup(response.text, 'html.parser', parse_only=strainer)

            # Extract text from the filtered elements
            text = '\n'.join(element.get_text(strip=True) for element in soup)

            return text
        else:
            return "Failed to retrieve the webpage"

    def update_dataframe_and_save_to_csv(self, new_row, csv_filename):
        """
        Updates a Pandas DataFrame with a new row (list of 3 elements) and writes it to a CSV file.
    
        :param new_row: List of 3 elements to be added as a new row in the DataFrame.
        :param csv_filename: The name of the CSV file to write the DataFrame to.
        """
        # Check if the CSV file exists
        if os.path.exists(csv_filename):
            # Load the existing CSV into a DataFrame
            df = pd.read_csv(csv_filename)
        else:
            # Create a new DataFrame with column names if CSV doesn't exist
            df = pd.DataFrame(columns=['Column1', 'Column2', 'Column3'])
        
        # Append the new row to the DataFrame
        new_df = pd.DataFrame([new_row], columns=df.columns)
        df = pd.concat([df, new_df], ignore_index=True)
        
        # Save the updated DataFrame back to CSV
        df.to_csv(csv_filename, index=False)

        print("Saved!")