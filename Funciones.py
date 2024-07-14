from bs4 import BeautifulSoup
import requests
import csv

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

def csv_stuff(nombre_archivo=str, tiendas=list, precios=list, avg=int):
    csv_file_name = nombre_archivo + ".csv"
    csv_headers = []
    tiendas = tiendas
    csv_headers[0] = ['Fecha']
    l = 1
    for i in tiendas:
        l=+1
        csv_headers[l] = i
    csv_headers.append('Precio Promedio')
    with open(csv_file_name, mode = 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)
        writer.writeheader()





