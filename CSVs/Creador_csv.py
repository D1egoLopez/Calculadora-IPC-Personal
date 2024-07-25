import sys
import os
main_directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(main_directory_path)
from fufu import create_csv_with_headers

headers_c_tiendas = ['FECHA', 'DIA', 'DISCO', 'COTO', 'TOLEDO', 'LA COOPE', 'PRECIO PROMEDIO']
header_s_tiendas = []
create_csv_with_headers("leche", headers_c_tiendas)
create_csv_with_headers("Aceite Girasol", headers_c_tiendas)
create_csv_with_headers('Arroz', headers_c_tiendas)
create_csv_with_headers("Proteina", ['FECHA', 'PROTEINA'])
create_csv_with_headers("Creatina", ['FECHA', 'CREATINA'])
create_csv_with_headers("Youtube", ['MES', 'YOUTUBE'])
create_csv_with_headers("Crunchyroll", ['MES', 'Crunchyroll'])