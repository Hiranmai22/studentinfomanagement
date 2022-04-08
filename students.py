import requests
import json
url = "http://localhost:3000/students/2"
payload = json.dumps({
    "id": 2,
      "first_name": "Kiran",
      "last_name": "Bala",
      "Courses Registered": "Mobile Technologies, Next generation",
      "Overall Grade": "80 %"
})
headers = {'Content-Type' : 'application/json'}
response = requests.request("PUT", url, headers=headers,data=payload)
print(response.text)
