import requests
import re

url = "https://www.example.com"
response = requests.get(url)
if response.status_code == 200:
    print("Webový server je dostupný.")

    # Kontrola použití HTTPS
    if response.url.startswith('https://'):
        print("Webový server používá HTTPS.")
    else:
        print("Webový server nepoužívá HTTPS.")



    requests.packages.urllib3.disable_warnings()

    response = requests.get(url, verify=True)

    # Check the SSL/TLS version
    if response.connection.version == requests.packages.urllib3.util.ssl.PROTOCOL_TLSv1_2:
        print("TLS 1.2 is used for SSL/TLS encryption.")
    else:
        print("TLS 1.2 is not used for SSL/TLS encryption.")




    payload = "SELECT * FROM users WHERE name = 'admin' AND password = 'password';"
    response = requests.post(url, data=payload)
    if re.search("error", response.text, re.IGNORECASE):
        print("Webový server je zranitelný vůči SQL injection.")
    else:
        print("Webový server není zranitelný vůči SQL injection.")
else:
    print("Webový server není dostupný.")
