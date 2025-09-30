from flask import Flask, render_template_string
import platform, os, getpass, datetime, json

app = Flask(__name__)
DATA = "registros.json"

@app.route("/")
def index():
    
    info ={
        "Sistema operativo": platform.system() + " " + platform.release(),
        "Version ": platform.python_version(),
        "Fecha y hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Usuario": getpass.getuser(),
        "Ruta de ejecución": os.getcwd()
    }

    
    info_texto = json.dumps(info, indent=2)

    
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

if __name__ == "__main__":
    app.run(debug=True)

