from get_module import get_nasa
from data import API_KEY
from datetime import date, timedelta

fecha_ayer = str(date.today() - timedelta(days=1)) # Calcular la fecha de ayer, convirtiendola en un string

def pull_earth (fecha = fecha_ayer, api =API_KEY): # Funcion que recibe una fecha y una api
    y, m, d = fecha.split('-')                      # Divide el string en 3 partes: año, mes, dia

    url = f'https://api.nasa.gov/EPIC/api/natural/date/{fecha}?api_key={api}'
    get_url = get_nasa(url)

    photo_id = [elemento['image'] for elemento in get_url]
    time = [elemento['date'] for elemento in get_url]

    url = f'https://api.nasa.gov/EPIC/archive/natural/{y}/{m}/{d}/png/'
    end = f'.png?api_key={api}'
    get_url = get_nasa(url)
    
    return [ url + id + end for id in photo_id], time

if __name__== '__main__':
    fecha_ayer = pull_earth()
    print(fecha_ayer)
    