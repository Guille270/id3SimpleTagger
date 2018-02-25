import os
from mutagen.easyid3 import EasyID3

ruta = raw_input("EN: Write the name of the folder / ES: Escribe el nombre de la carpeta   ")


files = os.listdir(ruta)

for i in files:
	tag = EasyID3(str(ruta) + "/" + str(i))
	tag['album'] = ruta
	tag.save(v2_version=3)
