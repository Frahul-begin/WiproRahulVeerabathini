import requests

url = "https://api.restful-api.dev/objects"
response = requests.get(url)

print(response.status_code)
print(response.json())

#post request
posturl = "https://api.restful-api.dev/objects"

body1= {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

r1 = requests.post(posturl,json = body1)
print("post status code:", r1.status_code)
print(r1.json())

#PUT_Request
put_url = "https://api.restful-api.dev/objects/ff8081819782e69e019be4130bcc2ee3"
put_body ={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}

r2 = requests.put(put_url,json = put_body)
print("put status code:", r2.status_code)
print(r2.json())

#Patch Request
patch_url = "https://api.restful-api.dev/objects/ff8081819782e69e019be4130bcc2ee3"
patch_body ={
   "name": "Apple MacBook Pro 16 (Updated Name)"
}

r3 = requests.patch(patch_url,json = patch_body)
print("patch status code:", r3.status_code)
print(r3.json())