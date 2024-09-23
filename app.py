from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Usuarios registrados
usuarios = {
    'juan': 'admin',
    'pepe': 'user'
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        precio_por_tarros = 9000
        total_sin_descuento = tarros * precio_por_tarros

        # Calcular descuento
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template('result.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    mensaje = ""
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        if usuario == 'juan' and contraseña == 'admin':
            mensaje = f'Bienvenido administrador {usuario}'
        elif usuario == 'pepe' and contraseña == 'user':
            mensaje = f'Bienvenido usuario {usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

        return render_template('login.html', mensaje=mensaje)

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
