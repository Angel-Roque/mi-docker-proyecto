import os
import platform
import getpass
import datetime
import json
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)
DATA_FILE = "registros.json"

def recolectar_info():
    """Función para recolectar información del sistema."""
    info = {
        "sistema": platform.system(),
        "version": platform.version(),
        "usuario": getpass.getuser(),
        "ruta": os.getcwd(),
        "fecha_hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return info

def guardar_registro(info):
    """Guardar registro en JSON."""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                datos = json.load(f)
        else:
            datos = []
        datos.append(info)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2)
    except Exception as e:
        print("Error al guardar registro:", e)

@app.route("/", methods=["GET"])
def index():
    """Mostrar último registro del sistema."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            datos = json.load(f)
            ultimo = datos[-1] if datos else {}
    else:
        ultimo = {}

    info_texto = json.dumps(ultimo, indent=2)

    return render_template_string(f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Último Registro del Sistema</title>
<style>
body{{font-family:Arial,sans-serif;margin:20px;background:#f9f9f9;color:#333}}
h1,h2{{text-align:center;color:#2563eb}}
pre{{background:#f3f4f6;padding:20px;border-radius:8px;overflow:auto;white-space:pre-wrap;word-wrap:break-word}}
</style>
</head>
<body>
<h1>Info Sistema</h1>
<h2>Último registro</h2>
<pre>{info_texto}</pre>
</body>
</html>
""")

@app.route("/recibir", methods=["POST"])
def recibir():
    """Recibir información vía POST y guardarla."""
    info = request.get_json()
    if info:
        guardar_registro(info)
        return jsonify({"status": "ok", "mensaje": "Información recibida"})
    return jsonify({"status": "error", "mensaje": "No se recibió información"}), 400

if __name__ == "__main__":
    # Recolectar info al iniciar el servidor y guardarla
    info = recolectar_info()
    guardar_registro(info)
    print("Información recopilada al iniciar el servidor:")
    for k, v in info.items():
        print(f"{k}: {v}")
if __name__=="__main__":

    app.run(host="0.0.0.0",port=5001,debug=True)
