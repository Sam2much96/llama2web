import requests

# Define the base URL of the API
base_url = "ec2-51-20-53-10.eu-north-1.compute.amazonaws.com:8080"  # Update with the actual API URL

headers={'Accept': 'application/json','Content-Type': 'application/json'}

# Example 1: Making a GET Request
# Example 1: Making a POST Request
data = {"prompt": "who is naruto uzumaki?",'msg': None, 'type': "dict"}
response = requests.post(url=f"http://{base_url}/v1", headers=headers, json=data, timeout=10)
if response.status_code == 200:
    # Successful response
    data = response.json()
    print(data)
else:
    # Handle the error response
    print(f"Error: {response.status_code}")
    print(response.json())

