import requests

r=requests.get("https://reqres.in/api/users?page=2")
print(r)
#print(r.text)
#print(r.content)
#print(r.json())
json_response=r.json()
print(json_response['data'][5]) ###to get data from json
assert (json_response['data'][5]["email"]).endswith("reqres.in"), "email is not correct"  #validating email of one of these entry

