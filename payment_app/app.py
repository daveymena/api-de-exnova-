from flask import Flask, render_template, request, redirect, url_for, flash
import mercadopago
import paypalrestsdk
import os
import uuid

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key_here')

# Configurar Mercado Pago
mp = mercadopago.SDK(os.environ.get('MERCADO_PAGO_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN'))

# Configurar PayPal
paypalrestsdk.configure({
    "mode": os.environ.get('PAYPAL_MODE', 'sandbox'),  # sandbox or live
    "client_id": os.environ.get('PAYPAL_CLIENT_ID', 'YOUR_CLIENT_ID'),
    "client_secret": os.environ.get('PAYPAL_CLIENT_SECRET', 'YOUR_CLIENT_SECRET')
})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pay', methods=['POST'])
def pay():
    payment_method = request.form.get('payment_method')
    amount = 5.00  # $5

    if payment_method == 'mercadopago':
        return create_mp_payment(amount)
    elif payment_method == 'paypal':
        return create_paypal_payment(amount)
    else:
        flash('Método de pago no válido')
        return redirect(url_for('index'))

def create_mp_payment(amount):
    preference_data = {
        "items": [
            {
                "title": "Acceso a API Exnova",
                "quantity": 1,
                "unit_price": amount
            }
        ],
        "back_urls": {
            "success": url_for('payment_success', _external=True),
            "failure": url_for('payment_failure', _external=True),
            "pending": url_for('payment_pending', _external=True)
        },
        "auto_return": "approved"
    }

    preference_response = mp.preference().create(preference_data)
    preference = preference_response["response"]

    return redirect(preference["init_point"])

def create_paypal_payment(amount):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": url_for('payment_success', _external=True),
            "cancel_url": url_for('payment_failure', _external=True)
        },
        "transactions": [{
            "amount": {
                "total": str(amount),
                "currency": "USD"
            },
            "description": "Acceso a API Exnova"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    else:
        flash('Error al crear el pago con PayPal')
        return redirect(url_for('index'))

@app.route('/payment/success')
def payment_success():
    # Aquí puedes generar una clave de licencia o proporcionar el enlace de descarga
    license_key = str(uuid.uuid4())
    # Guardar la clave en una base de datos o archivo
    return render_template('success.html', license_key=license_key)

@app.route('/payment/failure')
def payment_failure():
    flash('El pago no se completó correctamente')
    return redirect(url_for('index'))

@app.route('/payment/pending')
def payment_pending():
    flash('El pago está pendiente de aprobación')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)