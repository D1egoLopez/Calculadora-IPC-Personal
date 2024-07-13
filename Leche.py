from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By


dia =  "https://diaonline.supermercadosdia.com.ar/leche-descremada-la-serenisima-protein-1-lt-272382/p"
disco = "https://www.disco.com.ar/leche-uat-la-serenisima-proteina-1lt/p"
coto = "https://www.cotodigital3.com.ar/sitios/cdigi/producto/-leche-protein-la-serenisina-botella-larga-vida-1l/_/A-00508911-00508911-200"
toledo = "https://toledodigital.com.ar/storeview_jara/catalog/product/view/id/3912/category/1282/"
la_coope = "https://www.lacoopeencasa.coop/producto/leche-larga-vida-la-serenisima-descremada-50%25-mas-proteina-1lts/710007"


# Initialize Chrome WebDriver
driver = webdriver.Chrome()
#agregar opcion para que no abra navegador

## Hacer funcion que deje solo numeros en los precios y los convierta en ints para luego hacer cuentas


listado_leches=[

]
# Posiblemente no se use esta funcion
def D_URL_setter(url):
    D_source = driver.get(url)
    D_soup = BeautifulSoup(D_source, 'html.parser')
    return D_soup
#viva peron
def URL_setter(url):
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    return soup

#temp
def has_at_least_one_character(input_string):
    return bool(input_string)

#DIA
soup = URL_setter(dia)
precio = soup.find('span', class_="vtex-product-specifications-1-x-specificationValue vtex-product-specifications-1-x-specificationValue--first vtex-product-specifications-1-x-specificationValue--last")
#print(precio)
listado_leches.append(precio.text)

#DISCO TO-DO --> usar selenium para extraer como con COTO

# soup = URL_setter(disco)
# precio = soup.find('div', class_="discoargentina-store-theme-1dCOMij_MzTzZOCohX1K7w")
# print(precio.text)
#listado_leches.append(precio)

#COTO
driver.get(coto)
precio = driver.find_elements(By.CSS_SELECTOR, "span.atg_store_newPrice")
driver.close
for i in precio:
   if bool(i.text):
      #saca simbolo pesos TO-DO sacar tambien centavos y puntos/comas
      temp_str = i.text
      print("dada", temp_str[1:]) 
      listado_leches.append(temp_str[1:])
   
print(listado_leches)
