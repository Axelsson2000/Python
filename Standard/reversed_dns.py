import socket

reversed_dns = socket.gethostbyaddr('dataman.se')
# ('crawl-203-208-60-1.googlebot.com', ['1.60.208.203.in-addr.arpa'], ['203.208.60.1'])

print(reversed_dns[0])
# 'crawl-203-208-60-1.googlebot.com'