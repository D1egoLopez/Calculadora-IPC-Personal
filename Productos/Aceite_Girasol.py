from fufu import *

def run():
    csv_file = 'Aceite Girasol.csv'

    urls = {
        'DIA': 'https://diaonline.supermercadosdia.com.ar/aceite-de-girasol-cocinero-900-ml-48605/p',
        'DISCO':'https://www.disco.com.ar/aceite-de-girasol-cocinero-900-ml/p',
        'COTO':'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-aceite-girasol--cocinero---botella-900-ml/_/A-00183553-00183553-200',
        'TOLEDO':'https://toledodigital.com.ar/storeview_jara/catalog/product/view/id/1762/s/aceite-de-girasol/',
        'LA COOPE':'https://www.lacoopeencasa.coop/producto/aceite-de-girasol-cocinero-900cm3/874906'
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

    listado_girasol = [

    ]

    buscar_dia(urls['DIA'], listado_girasol, to_csv_dict)
    buscar_disco(urls['DISCO'], listado_girasol, to_csv_dict)
    buscar_coto(urls['COTO'], listado_girasol, to_csv_dict)
    buscar_toledo(urls['TOLEDO'], listado_girasol, to_csv_dict)
    buscar_la_coope(urls['LA COOPE'], listado_girasol, to_csv_dict)
    push_to_csv(listado_girasol, to_csv_dict, csv_file)



