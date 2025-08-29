# Sistema de Pagos para API Exnova

Este es el sistema de pagos que permite a los usuarios pagar $5 por acceso a la API de Exnova.

## Configuración

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Configura las variables de entorno:
```bash
export MERCADO_PAGO_ACCESS_TOKEN="tu_token_de_mercado_pago"
export PAYPAL_CLIENT_ID="tu_client_id_de_paypal"
export PAYPAL_CLIENT_SECRET="tu_client_secret_de_paypal"
export PAYPAL_MODE="sandbox"  # o "live" para producción
export SECRET_KEY="tu_clave_secreta_para_flask"
```

3. Ejecuta la aplicación:
```bash
python app.py
```

4. Abre tu navegador en `http://localhost:5000`

## Integración de Mercado Pago

1. Crea una cuenta en [Mercado Pago](https://www.mercadopago.com/)
2. Obtén tu Access Token desde el panel de desarrolladores
3. Configura las credenciales de producción

## Integración de PayPal

1. Crea una cuenta en [PayPal Developer](https://developer.paypal.com/)
2. Crea una aplicación REST API
3. Obtén Client ID y Client Secret
4. Configura para sandbox inicialmente

## Uso

- Los usuarios visitan la página principal
- Seleccionan método de pago (Mercado Pago o PayPal)
- Son redirigidos al procesador de pagos
- Después del pago exitoso, reciben una clave de licencia
- Pueden usar la clave para acceder a la API

## Notas de Seguridad

- En producción, usa HTTPS
- Almacena las claves de licencia en una base de datos segura
- Implementa validación adicional de pagos
- Monitorea transacciones sospechosas