import requests
import json
import data as d

def get_nasa(url):
     return json.loads(requests.get(url).text)

if __name__ == '__main__':
     url = f'https://api.nasa.gov/planetary/apod?count=10&api_key={d.API_KEY}'  
     print(get_nasa(url))
