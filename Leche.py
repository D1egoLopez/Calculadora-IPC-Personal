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
precio = precio_producto_soup(urls['dia'], 'span', 'vtex-product-specifications-1-x-specificationValue vtex-product-specifications-1-x-specificationValue--first vtex-product-specifications-1-x-specificationValue--last')
if precio:
    int_precio = int(recorte_strings(limpieza_strings(precio.text)))
    print('Agregando precio de DIA', int_precio)
    listado_leches.append(int_precio)

#DISCO
driver.get(urls['disco'])
#tengo que esperar 5sg porque disco es re gracioso, asi tipo categoria humor, se jijea el tipazo
WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "discoargentina-store-theme-2t-mVsKNpKjmCAEM_AMCQH"))
    )
precio = driver.find_elements(By.CLASS_NAME, "discoargentina-store-theme-2t-mVsKNpKjmCAEM_AMCQH")
if precio:
    for i in precio:
        if bool(i.text):
            int_precio = int(limpieza_strings(i.text))
            print('Agregando precio de DISCO', int_precio)
            listado_leches.append(int_precio)

#COTO
driver.get(urls['coto'])
precio = driver.find_elements(By.CSS_SELECTOR, "span.atg_store_newPrice")
if precio:
    for i in precio:
        if bool(i.text):
            int_precio = int(recorte_strings(limpieza_strings(i.text)))
            #saca simbolo pesos TO-DO sacar tambien centavos y puntos/comas DONE
            print('Agregando precio de COTO', int_precio)
            listado_leches.append(int_precio)

# TOLEDO
precio = precio_producto_soup(urls['toledo'], 'span', "price" )
if precio:
    int_precio = int(recorte_strings(limpieza_strings(precio.text)))
    print('Agregando precio de TOLEDO', int_precio)
    listado_leches.append(int_precio)

#LA COPPE
driver.get(urls['la_coope'])
WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.precio.precio-detalle'))
    )
precio = driver.find_elements(By.CSS_SELECTOR, 'div.precio.precio-detalle')
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
