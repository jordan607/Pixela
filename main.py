import requests
from datetime import datetime



todaysdate = datetime.now()

pixela_endpoint = "https://pixe.la/v1/users"

# create user -------------------------------
user_params = {
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# create graph--------------------------------------------

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
headers = {
    "X-USER-TOKEN":token
}
graph_config={
    "id":id,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"momiji",

}

# response = requests.post(url=graph_endpoint, json= graph_config, headers= headers)
# print(response.text)


# Adding value to graph----------------------------------------------------
input_graph_config = {
    "date":todaysdate.strftime("%Y%m%d"),
    "quantity": input("How many Km did you cycle today? ")
}

response = requests.post(url=f"{graph_endpoint}/{id}",json=input_graph_config,headers=headers)
print(response.text)

# modifying a pixel------------------------------------

modify_graph_config = {
    "quantity": "9"
}

# response = requests.put(url=f"{graph_endpoint}/{id}/{input_graph_config['date']}", json=modify_graph_config,headers = headers)
# print(response.text)


# Delete a pixel----------------------------------------

# response = requests.delete(url=f"{graph_endpoint}/{id}/{input_graph_config['date']}", headers = headers)
# print(response.text)
