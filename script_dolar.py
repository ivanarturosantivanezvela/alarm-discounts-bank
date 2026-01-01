import bcchapi
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

usuario = os.getenv("BCCH_USER")
password = os.getenv("BCCH_PASSWORD")

# Incluyendo credenciales explícitamente
datos = bcchapi.Siete(usuario, password)

dolar_diario = datos.cuadro(
    series=["F073.TCO.PRE.Z.D"],
    nombres=["dolar"],
    desde="2025-01-01",
    frecuencia="D",
    observado={
        "dolar": "last"   # valor observado del día
    }
)

dolar_diario = (
    dolar_diario
        .reset_index()
        .rename(columns={"index": "fecha"})
)

print(dolar_diario)