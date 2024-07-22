import sys
import os
main_directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_directory_path)
from fufu import *

def run():
    csv_file = 'Arroz.csv'
    urls = {
        'DIA': 'https://diaonline.supermercadosdia.com.ar/arroz-monovarietal-corto-molinos-ala-1-kg-264264/p',
        'DISCO': 'https://www.disco.com.ar/arroz-en-grano-molinos-ala-1-kg/p',
        'COTO': 'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-arroz-varietal-corto-molinos-ala-1-kg/_/A-00576353-00576353-200'
    }
    to_csv_dict = {
        'FECHA':'',
        'DIA':'',
        'DISCO':'',
        'COTO':'',
        'TOLEDO':'',
        'LA COOPE':'',
        'PRECIO PROMEDIO': ''
    }
    listado_arroz = [

    ]
    buscar_dia(urls['DIA'],listado_arroz, to_csv_dict)
    buscar_disco(urls['DISCO'],listado_arroz, to_csv_dict)
    buscar_coto(urls['COTO'],listado_arroz, to_csv_dict)
    push_to_csv(listado_arroz,to_csv_dict,csv_file)

    