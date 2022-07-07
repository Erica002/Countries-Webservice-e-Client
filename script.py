import requests
import app

url = "http://127.0.0.1:8090/countries"

def get():
    response = requests.get(url)
    print(response.json())

def insert():
    insert = {"name": "South Korea", "capital": "Seul", "area": 100000}
    response = requests.post(url, json=insert)
    print(response.json())

def get_country(id):
    url = f"http://127.0.0.1:8090/countries/{id}"
    response = requests.get(url)
    print(response.json())

def put(id):
    put = {"name": "South Korea", "capital": "Seul", "area": 100210}
    url = f"http://127.0.0.1:8090/countries/{id}"
    response = requests.put(url, json=put)
    print(response.json())

def delete(id):
    url = f"http://127.0.0.1:8090/countries/{id}"
    response = requests.delete(url)
    print(response)
    
get()
insert()
get_country(1)
put(4)
delete(1)