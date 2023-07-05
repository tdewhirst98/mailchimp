from mailchimp_marketing import Client
import json
import csv
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("api_key")
server = os.environ.get('server')
list_id= os.environ.get('list_id')

# THIS IS THE APPLICATION THAT WORKS
mailchimp = Client()
mailchimp.set_config({
  "api_key": api_key,
  "server": server
})



csvFilePath = '/Users/torindewhrst/Desktop/mailchimp/mailchimp_data_dump.csv'
jsonFilePath = '/Users/torindewhrst/Desktop/mailchimp/mailchimp_email_subscription.json'


with open(csvFilePath, "r") as f:
    reader = csv.reader(f)
    next(reader)
    contacts = {"contacts": []}
    for row in reader:
        contacts["contacts"].append({"operation_id": row[0], "time_in": row[1], "time_out": row[2], "email": row[3], "pasword_hash": row[4], "status": row[5], "tags": row[6], })
        

with open(jsonFilePath, 'w') as f:
 json.dump(contacts, f, indent=4)


with open(jsonFilePath) as json_file:
    data = json.load(json_file)

operation_id = data['contacts'][0]['operation_id']
email_address = data['contacts'][0]['email']
subscription_status = data['contacts'][0]['status']

one_contact = [
    {
        "op_id": operation_id,
        "email": email_address,
        "status": subscription_status
    }
]


# BELOW WE ARE ADDDING 99 CONTACTS FROM JSON
for all_contacts in data['contacts'][0:99]:
    op_id = all_contacts['operation_id' [:99]]
    email = all_contacts['email'[:99]]
    status = all_contacts['status' [:99]]



    member_info = [
        {
        "op_id": op_id,
        "email_address": email,
        "status": status,
    },
   ]



    operations = []
    for item in member_info:
        operation = {
        "method": "POST",
        "path": f"/lists/{list_id}/members",
        "body": json.dumps({
            "operation_id": item["op_id"],
            "email_address": item["email_address"],
            "status": item["status"],
                    })
                }
        operations.append(operation)

        print(operations)


        payload = {
                "operations": operations
            }

        response = mailchimp.batches.start(payload)
        print(response)

