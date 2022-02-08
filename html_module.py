def create_html_pic(lista_dict):

    acum = ''
    for l in lista_dict:
        acum += f''' <h1>{l['title']}</h1>
        <p>{l['date']}</p>
        <img src = "{l['url']}">
        <p>{l['explanation']}</p>
        '''

    html = f'''
    <html>
    <head>
    </head>
        <body>
        {acum}
        </body>
    </htmml>'''

    return html

def create_html_earth(lista_fotos, lista_horas):

    acum=''
    for lf, lh in zip(lista_fotos, lista_horas):
        acum += f''' <p>{lh}</p>
        <img src = "{lf}"> width='50%'>
        '''

    html = f'''
    <html>
    <head>
    </head>
        <body>
            {acum}
        </body>
    </htmml>'''

    return html

def create_html_planet(lista_titulos, lista_descripciones, lista_fotos):

    acum=''
    for lt,ld, lf in zip(lista_titulos, lista_descripciones, lista_fotos):
        acum += f''' <h1>{lt}</h1>
        <img src = "{lf}" width='50%'>
        <p>{ld}</p>
        '''

    html = f'''
    <html>
    <head>
    </head>
        <body>
            {acum}
        </body>
    </htmml>'''

    return html



if __name__ == '__main__':
    from apod import pull_fotos
    from planet import pull_planetas
    from show import show_pics
    from earth import pull_earth
    
    dict = pull_fotos(2)
    html =(create_html_pic(dict))
    show_pics(html,'apod')
    

    titulos, descripciones, fotos = pull_planetas(2,5)
    html = create_html_planet(titulos, descripciones, fotos)
    show_pics(html,'planets')

    fotos, horas = pull_earth()
    html = create_html_earth(fotos,horas)
    show_pics(html,'earth')