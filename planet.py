from get_module    import get_nasa
import random

def get_photo(url):
    return get_nasa(url)['collection']['items'][0]['href']

def pull_planetas(eleccion, n):
    planetas = ['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune']
    url = f'https://images-api.nasa.gov/search?q={planetas[eleccion-1]}'       
    resultado = get_nasa(url)['collection']['item']
    elecciones = random.choices(resultado, k = n)

    nasa_id = [elemento['data'][0]['nasa_id'] for elemento in elecciones]
    descripcion = [elemento['data'][0]['description'] for elemento in elecciones]
    titulo =  [elemento['data'][0]['title'] for elemento in elecciones]
    foto =[get_photo(f'https://images-api.nasa.gov/asset/(id)') for id in nasa_id]

    return titulo, descripcion, foto

if __name__== '__main__':
    lista_titulos, descripcion, lista_pics = pull_planetas(2,3)
    print(lista_titulos)
    print(descripcion)
    print(lista_pics)