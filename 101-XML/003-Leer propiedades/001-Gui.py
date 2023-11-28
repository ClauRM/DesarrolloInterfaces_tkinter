#abrir ventana cmd, ejecutar pip install bs4
from bs4 import BeautifulSoup

archivo = open("interfaz.xml","r")
contenido = archivo.read()
xml = BeautifulSoup(contenido,"lxml")

for campo in xml.find_all("campo"):
    print(campo)
    tipo = campo.get("tipo")
    print(tipo)
