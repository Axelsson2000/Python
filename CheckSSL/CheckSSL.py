import OpenSSL
import ssl, socket
from datetime import datetime

Domain = "volvo.com"
cert=ssl.get_server_certificate((Domain, 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
x509.get_notAfter()

#E = x509.get_notAfter() #Ger ett udda format

FormateradTid = datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')

print("NotAfter", FormateradTid)