import socket, ssl
import OpenSSL

hostname='volvo.se'
port=443

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, server_hostname=hostname)
ssl_sock.connect((hostname, port))
ssl_sock.close()
print("ssl connection Done")

cert = ssl.get_server_certificate((hostname, port))
# OpenSSL
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
pk = x509.get_pubkey()
print(x509.get_notAfter())
print(x509.get_notBefore())
print(pk)

#xyz = pk.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
#print(xyz)