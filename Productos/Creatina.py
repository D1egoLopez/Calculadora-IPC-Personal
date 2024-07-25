import sys
import os
main_directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_directory_path)
from fufu import *


def run ():
    url = 'https://www.mercadolibre.com.ar/creatina-monohidratada-star-nutrition-300-gr-doypack/p/MLA36978779#reco_item_pos=1&reco_backend=best-seller&reco_backend_type=low_level&reco_client=highlights-rankings&reco_id=59d55db1-8a42-4d06-9eb2-2cdfe8e620c3'

    csv_file ='Creatina.csv'
    to_csv_dict = {
        'FECHA':'',
        'CREATINA':''
    }
    source = requests.get(url)

    soup = BeautifulSoup(source.content, 'html.parser')

    precio_papota = soup.find('span', class_='andes-money-amount__fraction')

    if precio_papota:
        print(precio_papota.text)
        to_csv_dict['CREATINA'] = int(limpieza_strings(precio_papota.text))
        push_to_csv_simple(to_csv_dict,csv_file)