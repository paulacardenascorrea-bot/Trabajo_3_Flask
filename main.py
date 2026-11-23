
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = None
    estado = None
    error = None

    if request.method == "POST":
        try:
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])

            if not all(10 <= nota <= 70 for nota in [nota1, nota2, nota3]):
                error = "Las notas deben estar entre 10 y 70."
            elif not 0 <= asistencia <= 100:
                error = "La asistencia debe estar entre 0 y 100."
            else:
                promedio = round((nota1 + nota2 + nota3) / 3, 1)

                if promedio >= 40 and asistencia >= 75:
                    estado = "APROBADO"
                else:
                    estado = "REPROBADO"

        except (ValueError, KeyError):
            error = "Ingresa valores numéricos válidos."

    return render_template(
        "ejercicio1.html",
        promedio=promedio,
        estado=estado,
        error=error
    )


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombre_mayor = None
    cantidad = None
    error = None

    if request.method == "POST":
        nombres = [
            request.form.get("nombre1", "").strip(),
            request.form.get("nombre2", "").strip(),
            request.form.get("nombre3", "").strip()
        ]

        if not all(nombres):
            error = "Debes ingresar los tres nombres."
        elif len(set(nombre.lower() for nombre in nombres)) != 3:
            error = "Los tres nombres deben ser diferentes."
        else:
            nombre_mayor = max(nombres, key=len)
            cantidad = len(nombre_mayor)

    return render_template(
        "ejercicio2.html",
        nombre_mayor=nombre_mayor,
        cantidad=cantidad,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
