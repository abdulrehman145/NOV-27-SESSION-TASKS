import requests

url="https://jsonplaceholder.typicode.com/posts"
 
response=requests.get(url)

if response.status_code==(200):
    data=requests.get(url).json()
    print("API data is loaded successfully")
    print(data)
else:
    print("failed to load data")
