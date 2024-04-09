import json
import urllib
import requests

where = urllib.parse.quote_plus("""
{
    "Gender": "female"
}
""")
url = 'https://parseapi.back4app.com/classes/Complete_List_Names?limit=5000&keys=Name&where=%s' % where
headers = {
    'X-Parse-Application-Id': 'zsSkPsDYTc2hmphLjjs9hz2Q3EXmnSxUyXnouj1I', # This is the fake app's application id
    'X-Parse-Master-Key': '4LuCXgPPXXO2sU5cXm6WwpwzaKyZpo3Wpj4G4xXK' # This is the fake app's readonly master key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need

# Extracting only the "Name" values
names = [entry["Name"] for entry in data["results"]]

# Writing names to a text file
with open("../data/female_names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
