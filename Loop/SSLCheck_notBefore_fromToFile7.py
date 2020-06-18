from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json
import re
from datetime import date
today = date.today()

IndataDomain = open('C:\\Users\\LST\\Documents\\Python\\loop\\indatadomain.txt', 'r') 

# Opening file 
IndataDomain = open('C:\\Users\\LST\\Documents\\Python\\loop\\indatadomain.txt', 'r') 
count = 0
  
# Using for loop 
for line in IndataDomain: 
    count += 1

    domain = ("{}".format(line.strip()))
    port = '443'
    context = ssl.create_default_context()

    reversed_dns = socket.gethostbyaddr(domain)


    with socket.create_connection((domain, port)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            #print(ssock.version())
            CertInfoALL = json.dumps(ssock.getpeercert())   
            #notBefore
            notBeforepattern = "notBefore(.*?)," #Hittar text mellan "notBefore" & ","
            notBeforesubstring = re.search(notBeforepattern, CertInfoALL).group(0) #Grupp(0) skriver även ut notbefore, det gör inte group(1)
            #notAfter
            notAfterpattern = "notAfter(.*?)," #Hittar text mellan "notBefore" & ","
            notAftersubstring = re.search(notAfterpattern, CertInfoALL).group(0) #Grupp(0) skriver även ut notbefore, det gör inte group(1)
            
            
            #print("Date:" , today, "; Domain:" , domain,";", notBeforesubstring,";" , notAftersubstring) #Skriv ut på skärm för test
            print("ReverseDNS:", reversed_dns,"; Date:" , today, ";" ,domain,";", notBeforesubstring,";", notAftersubstring) #Skriv ut på skärm för test
            SSLresult = ("ReverseDNS:", reversed_dns,"; Date:" , today, ";" ,domain,";", notBeforesubstring,";", notAftersubstring) #Det som skall skivas till fil
        
    #Skriv till fil SSL
    SSLfile = open("C:\\Users\\LST\\Documents\\Python\\loop\\SSLresult.txt","a") #append mode 
    SSLfile.write(str(SSLresult)) #om inte str är med skriv onödiga saker i filen senare
    SSLfile.write("\n") #new_line = "\n" 
    SSLfile.close() 


