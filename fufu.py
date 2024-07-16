from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--ignore-certificate-errors")
#chrome_options.add_argument("--headless")


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
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, clase))
    )
    precio = driver.find_elements(By.CLASS_NAME, clase)
    driver.close
    return precio
def precio_producto_driver_by_css(url=str, clase=str, element=str):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    eleclase = element + "." + clase
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, eleclase))
    )
    precio = driver.find_elements(By.CSS_SELECTOR, eleclase)
    driver.close
    return precio

def precio_profucto_driver_by_ID(url=str, ID=str):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.ID, ID))
    )
    precio = driver.find_elements(By.ID, ID)
    driver.close
    return precio

def precio_producto_diver_by_class_cgt(url=str, clase=str):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, clase))
    )
    precio = driver.find_elements(By.CLASS_NAME, clase)
    driver.close
    return precio