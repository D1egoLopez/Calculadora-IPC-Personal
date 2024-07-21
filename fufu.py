from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import csv
import pandas as pd
import datetime

chrome_options = Options()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--silent") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chromedriver_path = os.path.join('webdriver', 'chromedriver.exe')
service = Service(chromedriver_path)
urls = {
    'DIA': '',
    'DISCO':'',
    'COTO':'',
    'TOLEDO':'',
    'LA COOPE':''
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

def precio_producto_driver_by_class(url=str, clase=str):
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, clase))
    )
    precio = driver.find_elements(By.CLASS_NAME, clase)
    driver.close
    return precio

def precio_producto_driver_by_css(url=str, clase=str, element=str):
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    eleclase = element + "." + clase
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, eleclase))
    )
    precio = driver.find_elements(By.CSS_SELECTOR, eleclase)
    driver.close
    return precio

def precio_profucto_driver_by_ID(url=str, ID=str):
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.ID, ID))
    )
    precio = driver.find_elements(By.ID, ID)
    driver.close
    return precio

def precio_producto_driver_by_class_cgt(url=str, clase=str):
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 30).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, clase))
    )
    precio = driver.find_elements(By.CLASS_NAME, clase)
    driver.close
    return precio

def create_csv_with_headers(nombre_archivo=str, headers=list):
    dir = 'CSVs'
    csv_file_name = os.path.join(dir, nombre_archivo + ".csv")
    with open(csv_file_name, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

def add_data_row_csv(csv_file = str, precios_dict = dict):
    df = pd.read_csv(csv_file)
    new_row = {col: precios_dict.get(col, ' ') for col in df.columns}
    new_row_df = pd.DataFrame([new_row])
    df = pd.concat([df, new_row_df], ignore_index=True)
    df.to_csv(csv_file, index=False)

    print("Updating " + csv_file)
    print(df)

def buscar_dia(url = str, lista_precios = list, csv_dict = dict):
    print('Ejecutando DIA')
    Super = 'DIA'
    clase = 'vtex-product-specifications-1-x-specificationValue vtex-product-specifications-1-x-specificationValue--first vtex-product-specifications-1-x-specificationValue--last'
    precio = precio_producto_soup(url, 'span', clase)
    if precio:
        int_precio = int(recorte_strings(limpieza_strings(precio.text)))
        print('Agregando precio de DIA: ',  int_precio)
        lista_precios.append(int_precio)
        csv_dict[Super] = int_precio

def buscar_disco(url = str, lista_precios = list, csv_dict = dict):
    print('Ejecutando DISCO')
    Super = 'DISCO'
    clase = 'discoargentina-store-theme-1dCOMij_MzTzZOCohX1K7w'
    clase_oferta = 'discoargentina-store-theme-2t-mVsKNpKjmCAEM_AMCQH'
    oferta=1
    try:
        precio = precio_producto_driver_by_class_cgt(url, clase)
        if precio:
            precioo = precio[0]
            if bool(precioo.text):
                int_precio = int(limpieza_strings(precioo.text))
                print('Agregando precio de DISCO', int_precio)
                lista_precios.append(int_precio)
                csv_dict[Super] = int_precio
                oferta=0
        if oferta!=0:
            precio_oferta = precio_producto_driver_by_class_cgt(url, clase_oferta)
            if precio_oferta:
                if bool(precio_oferta[0].text):
                    int_precio = int(limpieza_strings(precio_oferta[0].text))
                    print('Agregando precio de DISCO en oferta', int_precio)
                    lista_precios.append(int_precio)
                    csv_dict[Super] = int_precio
    except StaleElementReferenceException:
        print("Element became stale, retrying...")
        # Retry or handle appropriately
        buscar_disco(url, lista_precios, csv_dict)

def buscar_coto(url = str, lista_precios = list, csv_dict = dict):  
    print('Ejecutando COTO')
    Super = 'COTO'
    clase = 'atg_store_newPrice'
    clase_oferta ='price_regular_precio'
    oferta=1
    precio = precio_producto_driver_by_css(url, clase, 'span')
    if precio:
        for i in precio:
            if bool(i.text):
                oferta = 0
                int_precio = int(recorte_strings(limpieza_strings(i.text)))
                print('Agregando precio de COTO', int_precio)
                lista_precios.append(int_precio)
                csv_dict[Super] = int_precio
                print('No hay oferta')
    if oferta != 0:
        print('Hay oferta')
        precio_oferta = precio_producto_driver_by_css(url, clase_oferta, 'span')
        if precio_oferta:
            if bool(precio_oferta[0].text):
                int_precio = int(recorte_strings(limpieza_strings(precio_oferta[0].text)))
                print('Agregando precio de COTO en oferta', int_precio)
                lista_precios.append(int_precio)
                csv_dict[Super] = int_precio

def buscar_toledo(url = str, lista_precios = list, csv_dict = dict):
    print('Ejecutando TOLEDO')
    Super = 'TOLEDO'
    clase = 'price'
    precio = precio_producto_soup(url, 'span', clase)
    if precio:
        int_precio = int(recorte_strings(limpieza_strings(precio.text)))
        print('Agregando precio de TOLEDO: ',  int_precio)
        lista_precios.append(int_precio)
        csv_dict[Super] = int_precio

def buscar_la_coope(url = str, lista_precios = list, csv_dict = dict):
    print('Ejecutando LA COOPE')
    Super = 'LA COOPE'
    clase = 'precio.precio-detalle'
    clase_oferta =''
    precio = precio_producto_driver_by_css(url, clase, 'div')
    if precio:
        if bool(precio[0].text):
            int_precio = int(recorte_strings(limpieza_strings(precio[0].text)))
            print('Agregando precio de LA COOPE', int_precio)
            lista_precios.append(int_precio)
            csv_dict[Super] = int_precio
        else:
            precio_oferta = precio_producto_driver_by_css(url, clase_oferta, 'div')
            if precio_oferta:
                for i in precio_oferta:
                    if bool(i.text):
                        int_precio = int(recorte_strings(limpieza_strings(i.text)))
                        print('Agregando precio de LA COOPE en oferta', int_precio)
                        lista_precios.append(int_precio)
                        csv_dict[Super] = int_precio

def push_to_csv(lista=list, csv_dict = dict, csv_file = str):
    dir = 'CSVs'
    csv_file_path = os.path.join(dir, csv_file)
    prec_promedio = "PRECIO PROMEDIO"
    frecha = "FECHA"
    precio_promedio = avg(lista)
    csv_dict[prec_promedio] = precio_promedio
    dait = datetime.datetime.now()
    dait_formateated = dait.strftime("%d/%m/%Y")
    csv_dict[frecha] = dait_formateated
    print('Agregando nueva DATA: ', csv_dict)
    add_data_row_csv(csv_file_path,csv_dict)
    print(lista)
    print('Precio promedio: $ ', precio_promedio)
