from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
#from Funciones import avg

urls = {
    'dia': "https://diaonline.supermercadosdia.com.ar/leche-descremada-la-serenisima-protein-1-lt-272382/p",
    'disco': "https://www.disco.com.ar/leche-uat-la-serenisima-proteina-1lt/p",
    'coto': "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-protein-la-serenisina-botella-larga-vida-1l/_/A-00508911-00508911-200",
    'toledo': "https://toledodigital.com.ar/storeview_jara/catalog/product/view/id/3912/category/1282/",
    'la_coope': "https://www.lacoopeencasa.coop/producto/leche-larga-vida-la-serenisima-descremada-50%25-mas-proteina-1lts/710007"
}

clases = {
    'dia': "vtex-product-specifications-1-x-specificationValue vtex-product-specifications-1-x-specificationValue--first vtex-product-specifications-1-x-specificationValue--last",
    'disco': "discoargentina-store-theme-2t-mVsKNpKjmCAEM_AMCQH",
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

def limpieza_strings(in_str=str):
    out_str = in_str.replace(',', '').replace('.', '').replace('$', '')
    return out_str
def recorte_strings(in_str=str):
    out_str = in_str[:-2]
    return out_str
def URL_setter(url):
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    return soup
def precio_producto_soup(url=str, elemento=str, clase=str):
    soup = URL_setter(url)
    precio = soup.find(elemento, class_=clase)
    return precio
def avg(precios=list):
    return sum(precios) / len(precios)
def precio_producto_diver_by_class(url=str, clase=str):
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, clase))
    )
    precio = driver.find_elements(By.CLASS_NAME, clase)
    return precio
def precio_producto_driver_by_css(url=str, clase=str, element=str):
    driver.get(url)
    eleclase = element + "." + clase
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, eleclase))
    )
    precio = driver.find_elements(By.CSS_SELECTOR, eleclase)
    return precio

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--ignore-certificate-errors")
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

listado_leches=[

]

#DIA
precio = precio_producto_soup(urls['dia'], 'span', clases['dia'])
if precio:
    int_precio = int(recorte_strings(limpieza_strings(precio.text)))
    print('Agregando precio de DIA', int_precio)
    listado_leches.append(int_precio)

#DISCO
precio = precio_producto_diver_by_class(urls['disco'], clases['disco'])
if precio:
    for i in precio:
        if bool(i.text):
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

driver.close()
precio_promedio = avg(listado_leches)

print(Tiendas)
print(listado_leches)
print('Precio promedio: $ ', precio_promedio)
