from datetime import datetime
from urllib import response
import requests

USERNAME="jalaudinaaja"
TOKEN="afsdfjlsadf;ajf"

GRAPH_ID="graph1"
pixela_end_point="https://pixe.la/v1/users"
user_params={
    'token':TOKEN,
    'username':USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixela_end_point,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_end_point}/{USERNAME}/graphs"

graph_config={
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai",   
}

headers={
    "X-USER-TOKEN":TOKEN,
}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixcel_creation_endpont=f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH_ID}"

# today=datetime.now()
today=datetime(year=2022,month=7,day=20)
date=today.strftime("%Y%m%d")
pixel_data={
    "date":date,
    # "quantity":"10.5",
    "quantity":"20.5",
    
}

# response=requests.post(url=pixcel_creation_endpont,json=pixel_data,headers=headers)
# print(response.text)

put_url=f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

put_data={
    "quantity":"6.5",
}
# response=requests.put(url=put_url,json=put_data,headers=headers)

# for delete
response=requests.delete(url=put_url,headers=headers)

print(response.text)