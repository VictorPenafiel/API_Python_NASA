import webbrowser
import time
import os

def show_pics(html,nombre):
    with open(f'{nombre}.html','w') as f:
        f.write(html)
    print('Las fotos se mostrarán en tu Navegador...')
    time.sleep(2)
    webbrowser.open(f'{nombre}.html')
    time.sleep(5)
    os.remove(f'{nombre}.html')

if __name__ == '__main__':
    from apod import pull_fotos
    from html_module import create_html_pic
    dict = pull_fotos(2)
    html = create_html_pic(dict)
    show_pics(html, 'apod')