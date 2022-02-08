from get_module import get_nasa
import data as d
from datetime import date, timedelta

fecha_ayer = str(date.today() - timedelta(days=1))

def pull_earth(fecha=fecha_ayer, api = d.API_KEY):
    y, m, d = fecha.split('-')

    url1 = f'https://api.nasa.gov/EPIC/api/natural/date/{fecha} api_key={api}'
    get_url1 = get_nasa(url1)

    photo_id = [elemento['image'] for elemento in get_url1]
    time = [elemento['date'] for elemento in get_url1]

    url2 = f'https://api.nasa.gov/EPIC/archive/natural/{y}/{m}{d}/png/'
    end = f'.png?api_key={api}'

    return [ url2 + id + end for id in photo_id], time

if __name__== '__main__':
    print(fecha_ayer)
    fotos, horas = pull_earth()
    print(fotos)
    print(horas)
