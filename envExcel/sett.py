from decouple import config

credencialesJson = {
    "type": config('GOOGLE_TYPE'),
    "project_id": config('GOOGLE_PROJECT_ID'),
    "private_key_id": config('GOOGLE_PRIVATE_KEY_ID'),
    "private_key": config('GOOGLE_PRIVATE_KEY').replace('\\n', '\n'), #Validamos los saltos de linia haciendo reemplazando los saltos falsos(strings) por reales.
    "client_email": config('GOOGLE_CLIENT_EMAIL'),
    "client_id": config('GOOGLE_CLIENT_ID'),
    "auth_uri": config('GOOGLE_AUTH_URI'),
    "token_uri": config('GOOLE_TOKEN_URI'),
    "auth_provider_x509_cert_url": config('GOOGLE_AUTH_PROVIDER_X509'),
    "client_x509_cert_url": config('GOOGLE_CLIENT_X509'),
    "universe_domain": config('GOOGLE_UNIVERSE_DOMAIN')
}