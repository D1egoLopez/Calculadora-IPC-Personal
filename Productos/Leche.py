from fufu import *

def run():
    csv_file = 'leche.csv'

    urls = {
        'DIA': "https://diaonline.supermercadosdia.com.ar/leche-descremada-la-serenisima-protein-1-lt-272382/p",
        'DISCO': "https://www.disco.com.ar/leche-uat-la-serenisima-proteina-1lt/p",
        'COTO': "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-protein-la-serenisina-botella-larga-vida-1l/_/A-00508911-00508911-200",
        'TOLEDO': "https://toledodigital.com.ar/storeview_jara/catalog/product/view/id/3912/category/1282/",
        'LA COOPE': "https://www.lacoopeencasa.coop/producto/leche-larga-vida-la-serenisima-descremada-50%25-mas-proteina-1lts/710007"
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

    listado_leches=[

    ]

    #DIA
    buscar_dia(urls['DIA'], listado_leches, to_csv_dict)

    #DISCO algo ta roto que habra que ver || Disco la concha de tu madre por que ahora no te pinta mostrarme el valor de la leche, dale amigo re gil, Moreno se enojaria >.<
    #Arreglada la wea, si se rompe de vuelta reviento el disco de guemes a piedrazos
    buscar_disco(urls['DISCO'], listado_leches, to_csv_dict)

    #COTO
    buscar_coto(urls['COTO'], listado_leches, to_csv_dict)

    # TOLEDO
    buscar_toledo(urls['TOLEDO'], listado_leches, to_csv_dict)

    #LA COPPE
    buscar_la_coope(urls['LA COOPE'], listado_leches, to_csv_dict)

    push_to_csv(listado_leches, to_csv_dict, csv_file)