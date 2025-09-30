import os, platform, getpass, datetime, requests

# Recolectar información del sistema
info = {
    "sistema": platform.system(),
    "version": platform.version(),
    "usuario": getpass.getuser(),
    "ruta": os.getcwd(),
    "fecha_hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

print(" Información recopilada:")
for k, v in info.items():
    print(f"{k}: {v}")

# Enviar al servidor Flask
try:
    r = requests.post("http://127.0.0.1:5000/recibir", json=info)
    print("\n Respuesta del servidor:", r.json())
except Exception as e:
    print("No se pudo conectar al servidor:", e)
