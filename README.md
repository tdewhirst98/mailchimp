#Mailchimp  API

#Step 1: Install Packages

''' bash
pip install mailchimp-marketing python-dotenv

#Step 2: Set up Enviroment Variables

''' bash 
API_KEY=your-mailchimp-api-key
SERVER=your-mailchimp-server
LIST_ID=your-mailchimp-list-id



#Step 3: nsure that your CSV file containing the data you want to import is located at the specified path.
Run the Python script mailchimp_importer.py.

''' bash 
python mailchimp_importer.py


The script will read the CSV file, convert the data into JSON format, and then post the JSON data to your Mailchimp account.


#STEP 4:
You can adjust the following variables in the script to suit your needs:

 - csvFilePath: Path to the CSV file containing the data to be imported.
 - jsonFilePath: Path to save the JSON file before posting it to Mailchimp.
 - Mailchimp API key, server, and list ID should be set as environment variables in the .env file.

