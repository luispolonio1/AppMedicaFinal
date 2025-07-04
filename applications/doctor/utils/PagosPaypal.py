import base64
import requests

PAYPAL_CLIENT_ID = 'AcbsbRcDmtknpJC2JJZ2upQ2DdkcihDaYw2Ckv69TxALnpnvzD1ug_O6foGXwry-soGMZkdXVOtB15io'
PAYPAL_CLIENT_SECRET = 'EJJJ4-CXLY5uN_HaY71qhVuJnH7Ydyf-z0_x3s2hreP8kN74H9hVTpwsL2civuhFwlpTWkdACuyIdduI'
BASE_URL = 'https://api-m.sandbox.paypal.com'

def generateAccessToken():
    if not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
        raise ValueError("PAYPAL_CLIENT_ID and PAYPAL_CLIENT_SECRET must be set")
        
    auth = f"{PAYPAL_CLIENT_ID}:{PAYPAL_CLIENT_SECRET}"
    auth = base64.b64encode(auth.encode()).decode('utf-8')
    
    response = requests.post(
        "https://api-m.sandbox.paypal.com/v1/oauth2/token",
        data={'grant_type': 'client_credentials'},
        headers={"Authorization": f"Basic {auth}"}
    )
    data = response.json()
    if response.status_code != 200:
        raise Exception(f"Failed to get access token: {response.status_code} {data}")
    return data['access_token']

def createPago(valor):
    try:
        access_token = generateAccessToken()
        url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": str(valor)
                    }
                }
            ]
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        if response.status_code != 201:
            raise Exception(f"Failed to create order: {response.status_code} {data}")
        return data
    except Exception as e:
        print(f"Error creating payment: {e}")
        return None

def capture_order(order_id):
    try:
        access_token = generateAccessToken()
        # CORREGIDO: Usar f-string para insertar el order_id
        url = f"https://api-m.sandbox.paypal.com/v2/checkout/orders/{order_id}/capture"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.post(url, headers=headers)
        data = response.json()
        
        # CORREGIDO: El status code para capture debería ser 201
        if response.status_code not in [200, 201]:
            raise Exception(f"Failed to capture order: {response.status_code} {data}")
        return data
    except Exception as e:
        print(f"Error capturing order: {e}")
        raise e