import random
from data import API_KEY
from get_module import get_nasa

def pull_fotos(n, total = 50, api =API_KEY):
  url = f'https://api.nasa.gov/planetary/apod?count={total}&api key={api}'
  resultado = get_nasa(url)
  pool_fotos = [elemento for elemento in resultado if elemento['media_type']=='image']
  
  return random.choices(pool_fotos, k = n)
  
  if __name__=='__main__':
    print(pull_fotos(2))