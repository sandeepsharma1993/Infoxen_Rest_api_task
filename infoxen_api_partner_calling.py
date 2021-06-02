import requests
import json
Base_url = 'http://127.0.0.1:8000/'
end_point='api/'
def create_resource():


    new_entry={
    'Address':'Delhi',
    'Person_Name':'Sandeep',
    'Contact':9875767576,
    'Verified_Status':True,
    'Business_Name':'Software Point'
    }
    r=requests.post(Base_url+end_point,data=json.dumps(new_entry))
    print(r.status_code)
    # print(r.text)
    print(r.json())

def get_details():
    r= requests.get(Base_url+end_point)
    data =r.json()
    print(r.status_code)
    print(data)
#create_resource()
get_details()
