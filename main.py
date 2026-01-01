import bcchapi
from dotenv import load_dotenv
import os

load_dotenv()

usuario = os.getenv("BCCH_USER")
password = os.getenv("BCCH_PASSWORD")

# Incluyendo credenciales explícitamente
siete = bcchapi.Siete(usuario, password)

print(siete.buscar("antofagasta"))