import getpass
import sys

#Usamos getpass que es mñas fiable en entornos Linux
usuario = getpass.getuser()

print(f"--- Diagnóstico de Entorno ---")
print(f"Felicidades, {usuario}!")
print(f"Sistema Operativo:{sys.platform}")
print(f"Versión de Python:{sys.version.split()[0]}")
print(f"Ruta del ejecutable:{sys.executable}")
print(f"--------------------------------")
