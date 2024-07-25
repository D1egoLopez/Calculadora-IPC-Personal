import sys
import os
main_directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_directory_path)
from fufu import *


def run ():
    url = 'https://www.mercadolibre.com.ar/star-nutrition-platinum-proteinas-platinum-whey-protein-polvo-pote-cookies-cream-unidad-1-1-908-g-908-g/p/MLA18710125?product_trigger_id=MLA18710123&quantity=1'

    csv_file ='Proteina.csv'
    to_csv_dict = {
        'FECHA':'',
        'PROTEINA':''
    }
    source = requests.get(url)

    soup = BeautifulSoup(source.content, 'html.parser')

    precio_papota = soup.find('span', class_='andes-money-amount__fraction')

    if precio_papota:
        print(precio_papota)
        to_csv_dict['PROTEINA'] = int(limpieza_strings(precio_papota.text))
        push_to_csv_simple(to_csv_dict,csv_file)