import threading
import Productos.Leche as letche
import Productos.Aceite_Girasol as girasol
import Productos.Arroz as arroz
import Productos.Creatina as crea
import Productos.Proteina as papot

def run_arroz():
     arroz.run
def run_letche():
     letche.run()
def run_girasol():
     girasol.run()

papot.run()

# thread1 = threading.Thread(target=letche.run)
# thread2 = threading.Thread(target=girasol.run)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()