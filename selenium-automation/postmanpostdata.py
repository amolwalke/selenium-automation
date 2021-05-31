import requests
import json

#mydata= open("data.json","r").read()

resp=requests.post("https://reqres.in/api/register",data=json.loads(open("data.json","r").read())) ####load data from json file and post 
print(resp)
print(resp.json())
#assert resp.json() ["job"]=="leader" , "error"
print(resp.json()['token'])