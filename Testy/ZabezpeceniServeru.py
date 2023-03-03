import ssl
import socket
import datetime

HOSTS = ["www.example.com"]
PORT = 443

def test_security(host, port):
    print(f"Testování zabezpečení pro {host}:{port}...")
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
        s.connect((host, port))
        cert = s.getpeercert()
        print(f"\tPodporované protokoly: {cert['protocol']}")
        print(f"\tPodporované šifrovací algoritmy: {cert['cipher']}")
        print(f"\tDélka klíče: {cert['bits']} bitů")
        cert_expire_date = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
        print(f"\tPlatnost certifikátu do: {cert_expire_date}")
        if cert_expire_date < datetime.datetime.now():
            print("\t\tVarování: Certifikát je neplatný nebo expirovaný!")
        print()

for host in HOSTS:
    test_security(host, PORT)
