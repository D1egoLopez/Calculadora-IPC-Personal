from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fufu import *

urls = {
    'dia': "https://diaonline.supermercadosdia.com.ar/leche-descremada-la-serenisima-protein-1-lt-272382/p",
    'disco': "https://www.disco.com.ar/leche-uat-la-serenisima-proteina-1lt/p",
    'coto': "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-protein-la-serenisina-botella-larga-vida-1l/_/A-00508911-00508911-200",
    'toledo': "https://toledodigital.com.ar/storeview_jara/catalog/product/view/id/3912/category/1282/",
    'la_coope': "https://www.lacoopeencasa.coop/producto/leche-larga-vida-la-serenisima-descremada-50%25-mas-proteina-1lts/710007"
}

clases = {
    'dia': "vtex-product-specifications-1-x-specificationValue vtex-product-specifications-1-x-specificationValue--first vtex-product-specifications-1-x-specificationValue--last",
    'disco': "discoargentina-store-theme-1dCOMij_MzTzZOCohX1K7w",
    'coto': "atg_store_newPrice",
    'toledo': "price",
    'la_coope': "precio.precio-detalle"
}
#Crea la lista de tiendas en mayusculas para agregar al csv
def Lista_tiendas(urls):
    tienditas = []
    for i in urls:
        tienditas.append(i)
    Tiendotas = [i.upper() for i in tienditas]
    return Tiendotas

Tiendas = Lista_tiendas(urls)

#cambiar tiendas a que se agregue cuando encuentra un precio, DISCO y la re concha de tu madre



# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--log-level=3")
# chrome_options.add_argument("--ignore-certificate-errors")
# driver = webdriver.Chrome(options=chrome_options)

listado_leches=[

]

#DIA
precio = precio_producto_soup(urls['dia'], 'span', clases['dia'])
if precio:
    int_precio = int(recorte_strings(limpieza_strings(precio.text)))
    print('Agregando precio de DIA', int_precio)
    listado_leches.append(int_precio)



#DISCO algo ta roto que habra que ver || Disco la concha de tu madre por que ahora no te pinta mostrarme el valor de la leche, dale amigo re gil, Moreno se enojaria >.<
#Arreglada la wea, si se rompe de vuelta reviento el disco de guemes a piedrazos
precio = precio_producto_diver_by_class_cgt(urls['disco'], clases['disco'])
if precio:
    for i in precio:
        print(i.text, 'viva peron')
        int_precio = int(limpieza_strings(i.text))
        print('Agregando precio de DISCO', int_precio)
        listado_leches.append(int_precio)

#COTO
precio = precio_producto_driver_by_css(urls['coto'], clases['coto'], 'span')
if precio:
    for i in precio:
        if bool(i.text):
            int_precio = int(recorte_strings(limpieza_strings(i.text)))
            #saca simbolo pesos TO-DO sacar tambien centavos y puntos/comas DONE
            print('Agregando precio de COTO', int_precio)
            listado_leches.append(int_precio)

# TOLEDO
precio = precio_producto_soup(urls['toledo'], 'span', clases['toledo'] )
if precio:
    int_precio = int(recorte_strings(limpieza_strings(precio.text)))
    print('Agregando precio de TOLEDO', int_precio)
    listado_leches.append(int_precio)

#LA COPPE
precio = precio_producto_driver_by_css(urls['la_coope'], clases['la_coope'], "div")
if precio:
    for i in precio:
        if bool(i.text):
            int_precio = int(recorte_strings(limpieza_strings(i.text)))
            print('Agregando precio de LA COPPE', int_precio)
            listado_leches.append(int_precio)

precio_promedio = avg(listado_leches)

print(Tiendas)
print(listado_leches)
print('Precio promedio: $ ', precio_promedio)
